from typing import Dict
from requests import post

from prompt_engineering.prompts import PROMPTS, CHAT_PROMPTS, PROMPT_ERROR, CHAT_ERROR

def example(input:str,target:str,example_delimiter:str="\n###\n",input_target_delimiter:str="\n") -> callable:
    def _(api_call:callable) -> callable:
        def modify_prompt(prompt:str, *args, **kwargs) -> Dict[str,str]:
            prompt = f"{input}{input_target_delimiter}{target}{example_delimiter}{prompt}"
            if not prompt.endswith(input_target_delimiter):
                prompt += input_target_delimiter
            return api_call(prompt, *args, **kwargs)
        return modify_prompt 
    return _

def description(instruction:str,delimiter:str="\n###\n") -> callable:
    def _(api_call:callable) -> callable:
        def modify_prompt(prompt:str, *args, **kwargs) -> Dict[str,str]:
            prompt = f"{instruction}{delimiter}{prompt}"
            return api_call(prompt, *args, **kwargs)
        return modify_prompt 
    return _

def task(task_name:str) -> callable:
    def _(api_call:callable) -> callable:
        def modify_prompt(prompt:str, *args, **kwargs) -> Dict[str,str]:
            assert task_name in PROMPTS, PROMPT_ERROR.format(task_name=task_name)
            task_data = PROMPTS.get(task_name,dict())
            example_delimiter = task_data.get('example_delimiter')
            input_target_delimiter = task_data.get('input_target_delimiter')
            for x,y in task_data.get('examples'):
                prompt = f"{x}{input_target_delimiter}{y}{example_delimiter}{prompt}"
            description = task_data.get('description')
            if description is not None:
                prompt = f"{description}{example_delimiter}{prompt}"
            prompt += input_target_delimiter
            return api_call(prompt, *args, **kwargs)
        return modify_prompt 
    return _

def chatbot(task_name:str) -> callable:
    def _(api_call:callable) -> callable:
        def modify_prompt(prompt:str, *args, **kwargs) -> Dict[str,str]:
            assert task_name in CHAT_PROMPTS, CHAT_ERROR.format(task_name=task_name)
            task_data = CHAT_PROMPTS.get(task_name,dict())
            description = task_data.get('description')
            delimiter = task_data.get('delimiter')
            system_prefix = task_data.get('system_prefix')
            if description is not None:
                contextual_prompt = f"{description}{delimiter}{delimiter}Conversation:{delimiter}"
            chat_history = task_data.get('chat_history')
            chat_history.append(f"{task_data.get('user_prefix')}{prompt}")
            contextual_prompt += delimiter.join(chat_history) 
            contextual_prompt +=  f"{delimiter}{system_prefix}"
            reply = api_call(contextual_prompt, *args, **kwargs)
            reply = f"{system_prefix}{reply.strip()}"
            chat_history.append(reply)
            return reply 
        return modify_prompt 
    return _

def api(endpoint:str, key:str, hyperparameters:dict, cache:bool=True) -> callable:
    def _(process_response_json:callable) -> callable:
        def call_endpoint(data:dict,memory:dict=dict()) -> None:
            payload = hyperparameters
            payload.update(data)
            prompt = payload.get('prompt')
            if prompt not in memory or not cache:
                response = post(endpoint, json=payload, headers={
                    'Content-Type':'application/json',
                    'Authorization':f'Bearer {key}'
                })
                result =  process_response_json(data=response.json()) if response.ok else response.reason
                memory[prompt] = result
            return memory.get(prompt)
        return call_endpoint
    return _