from typing import Dict
from requests import post

from prompt_engineering.prompts import PROMPTS, ERROR_MESSAGE

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
            assert task_name in PROMPTS, ERROR_MESSAGE.format(task_name=task_name)
            task_data = PROMPTS.get(task_name,dict())
            example_delimiter = task_data.get('example_delimiter')
            input_target_delimiter = task_data.get('input_target_delimiter')
            for x,y in task_data.get('examples'):
                prompt = f"{x}{input_target_delimiter}{y}{example_delimiter}{prompt}"
            __description = task_data.get('description')
            if __description is not None:
                prompt = f"{__description}{example_delimiter}{prompt}"
            prompt += input_target_delimiter
            return api_call(prompt, *args, **kwargs)
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