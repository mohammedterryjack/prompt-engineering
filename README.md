# Prompt Engineering

```
pip install prompt_engineering
```
## Language Models (APIs)

```python
from prompt_engineering import api
```
---
### Jurassic (AI21Studio)
```python
@api(endpoint="https://api.ai21.com/studio/v1/j1-large/complete", key=YOUR_AI21_KEY, hyperparameters=dict(temperature=.6))
def jurassic(data:dict) -> str:
    return data['completions'][0]['data']['text']
```

---

### GPT3 (OpenAI)
```python
@api(endpoint="https://api.openai.com/v1/engines/text-davinci-002/completions", key=YOUR_OPENAI_KEY, hyperparameters=dict(temperature=.6))
def gpt3(data:dict) -> None:
    return data['choices'][0]['text']

```
---

### GPTJ (OxAPI)

```python
@api(endpoint='https://api.oxolo.com/api/v1/model/nlp/gpt-j-6b/v1/inference', key=YOUR_OXAPI_KEY, hyperparameters=dict(temperature=.6, eos_words =["\n", "###"]))
def gptj(data:dict) -> None:
    return data['results'][0]
```

---

***Example 1: Without Prompts***

```python
jurassic(dict(prompt="this is a"))
```
> " 16 year old, 5'3\", 115 lb female.\n"

```python
gpt3(dict(prompt="this is a"))
```
> " test\n\nThis is a test."

```python
gptj(dict(prompt="this is a"))
```

> " picture that my friend took for us. we are happy that he took the camera and the time to take pics of our day"
---

---
***Example 2: With Custom Prompts***

```python
gpt3(dict(prompt='equation: 4*4'))
```
>  "* 4 * 4 * 4"


```python
from prompt_engineering import example, description

@example('equation: 3*3','answer: 9')
@example('equation: 2*2','answer: 4')
@example('equation: 5*5','answer: 25')
@description('calculate the equation given')
def calculator(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))
```

```python
calculator(prompt='equation: 4*4')
```
> "answer: 16"

---
***Example 3: With Prepared Prompts***

```python
gptj(dict(prompt="calculate the sum of even numbers from 4 to 40"))
```
>  " and add it to the sum of odd numbers from 4 to 40.\n"


```python
from prompt_engineering import task

@task('translate_to_python')
def python_generator(prompt:str) -> str:
    return gptj(dict(prompt=prompt))

```

```python
python_generator(prompt="calculate the sum of even numbers from 4 to 40")
```
> "sum(x for x in range(4,41,2))\n"

---
***Example 4: Advanced Prompts***
```python
from prompt_engineering import format_table

@task("query_table")
def query_table(prompt:str) -> str:    
    return gpt3(dict(prompt=prompt))
```
```python
table = dict(
    name=["Majd","Oliver","Annie"],
    favourite_food=["Pizza","Salad","Soup"],
    gender=["Male","Male","Female"],
)
print(query_table(f"{format_table(table)}\nWho likes salad?"))
```
> "A: Oliver"

---
```python
from prompt_engineering import list_tasks

list_tasks()
```
```
('autocomplete', 'autocomplete_analogy', 'autocomplete_logical', 'conditional_nlg', 'topic_classification', 'intent_classification', 'sentiment_analysis', 'slot_extraction', 'summarisation', 'elaboration', 'hashtags', 'simplification', 'translate_to_table', 'translate_to_python', 'translate_to_javascript', 'translate_from_table', 'translate_from_python', 'translate_from_emojis', 'question_answering', 'query_table', 'chatbot')
```
---

## ChangeLog
- 0.0.1 initial release