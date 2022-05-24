from os import environ
from prompt_engineering import task, api
from prompt_engineering.utils import to_csv

@api(endpoint="https://api.openai.com/v1/engines/text-davinci-002/completions", key=environ["OPENAI_KEY"], hyperparameters=dict(temperature=.6))
def gpt3(data:dict) -> None:
    return data['choices'][0]['text']

@api(endpoint='https://api.oxolo.com/api/v1/model/nlp/gpt-j-6b/v1/inference', key=environ["OXAPI_KEY"], hyperparameters=dict(temperature=.6, eos_words =["\n", "###"]))
def gptj(data:dict) -> None:
    return data['results'][0]

@api(endpoint="https://api.ai21.com/studio/v1/j1-large/complete", key=environ["AI21_KEY"], hyperparameters=dict(temperature=.6))
def jurassic(data:dict) -> str:
    return data['completions'][0]['data']['text']


@task("topic_classification")
def intent_classification(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))

@task("translate_to_csv")
def slot_extraction(prompt:str) -> str:    
    return gpt3(dict(prompt=prompt))

from prompt_engineering import from_csv

def nlu(prompt:str) -> dict:
    intent = intent_classification(prompt)
    slots = slot_extraction(prompt)
    return dict(
        Intent = intent.lstrip('The topic of this article is:'),
        Slots = from_csv(lines=slots.strip().split('\n'), delimiter="|")
    )

utterance = "Can i book a table at a Bento or Sushi restaurant for Friday please"
nlu(utterance)
