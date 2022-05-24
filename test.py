from os import environ
from prompt_engineering import task, api

@api(endpoint="https://api.openai.com/v1/engines/text-davinci-002/completions", key=environ["OPENAI_KEY"], hyperparameters=dict(temperature=.6))
def gpt3(data:dict) -> None:
    return data['choices'][0]['text']

@api(endpoint='https://api.oxolo.com/api/v1/model/nlp/gpt-j-6b/v1/inference', key=environ["OXAPI_KEY"], hyperparameters=dict(temperature=.6, eos_words =["\n", "###"]))
def gptj(data:dict) -> None:
    return data['results'][0]

@api(endpoint="https://api.ai21.com/studio/v1/j1-large/complete", key=environ["AI21_KEY"], hyperparameters=dict(temperature=.6))
def jurassic(data:dict) -> str:
    return data['completions'][0]['data']['text']


@task("chatbot")
def bla(prompt:str) -> str:    
    print(prompt)
    return jurassic(dict(prompt=prompt))


PROMPT = "What do you think about marriage?"
#print(jurassic(dict(prompt=PROMPT)))
print(bla(PROMPT))