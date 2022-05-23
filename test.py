from prompt_engineering import task, api


YOUR_OXAPI_KEY = "sk-kzaUhe2JvASLbLLRNpVRThQnO5wSIsrHAilpzWT0xeb1UDtX"
YOUR_OPENAI_KEY = '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'
YOUR_AI21_KEY = 'lMEAynZekTuO8xTvLgbqVoZpL1Qzia3I'

@api(endpoint="https://api.openai.com/v1/engines/text-davinci-002/completions", key=YOUR_OPENAI_KEY, hyperparameters=dict(temperature=.6))
def gpt3(data:dict) -> None:
    return data['choices'][0]['text']

@api(endpoint='https://api.oxolo.com/api/v1/model/nlp/gpt-j-6b/v1/inference', key=YOUR_OXAPI_KEY, hyperparameters=dict(temperature=.6, eos_words =["\n", "###"]))
def gptj(data:dict) -> None:
    return data['results'][0]

@api(endpoint="https://api.ai21.com/studio/v1/j1-large/complete", key=YOUR_AI21_KEY, hyperparameters=dict(temperature=.6))
def jurassic(data:dict) -> str:
    return data['completions'][0]['data']['text']

data = dict(prompt="this is a test")


from prompt_engineering.utils import format_table

@task("query_table")
def query_table(prompt:str) -> str:    
    return gptj(dict(prompt=prompt))


table = dict(
    name=["Majd","Oliver","Annie"],
    favourite_food=["Pizza","Salad","Soup"],
    gender=["Male","Male","Female"],
)
PROMPT = f"{format_table(table)}\nWho likes salad?"
print(gptj(dict(prompt=PROMPT)))
print(query_table(PROMPT))