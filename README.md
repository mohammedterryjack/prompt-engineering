# Prompt Engineering

```
pip install prompt_engineering
```
## Language Models (APIs)

```python
from prompt_engineering import api
```

*Note: cache is enabled by default for all api calls. To allow for different responses, turn off cache*

---
### Jurassic (AI21Studio)
```python
@api(endpoint="https://api.ai21.com/studio/v1/j1-large/complete", key=YOUR_AI21_KEY, hyperparameters=dict(temperature=.6), cache=False)
def jurassic(data:dict) -> str:
    return data['completions'][0]['data']['text']
```

---

### GPT3 (OpenAI)
```python
@api(endpoint="https://api.openai.com/v1/engines/text-davinci-002/completions", key=YOUR_OPENAI_KEY, hyperparameters=dict(temperature=.6),cache=False)
def gpt3(data:dict) -> None:
    return data['choices'][0]['text']

```
---

### GPTJ (OxAPI)

```python
@api(endpoint='https://api.oxolo.com/api/v1/model/nlp/gpt-j-6b/v1/inference', key=YOUR_OXAPI_KEY, hyperparameters=dict(temperature=.6, eos_words =["\n", "###"]),cache=False)
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
from prompt_engineering import list_tasks

list_tasks()
```
```
(
 'autocomplete',
 'autocomplete_analogy',
 'autocomplete_logical',
 'topic_classification',
 'sentiment_analysis',
 'simplification',
 'summarisation',
 'elaboration',
 'horror_story',
 'hashtags',
 'grammar_correction',
 'translate_to_csv',
 'translate_to_teaser',
 'translate_to_german',
 'translate_to_french',
 'translate_to_spanish',
 'translate_to_japanese',
 'translate_to_python',
 'translate_from_french',
 'translate_from_python',
 'translate_from_emoji',
 'question_answering',
 'question_answering_javascript',
 'query_csv'
)
```
---

```python
from prompt_engineering import task

@task('autocomplete_analogy')
def generate_analogy(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))
```

```python
generate_analogy(prompt="Marriage")
```
> "Marriage is like a bridge. It is built to connect two places"

---

```python
@task('autocomplete_logical')
def predict_consequence(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))
```

```python
predict_consequence(prompt="Marriage")
```
> "Result: A happy couple"


```python
predict_consequence(prompt="Mary went to night school")
```
> "Result: Mary got a degree"


```python
predict_consequence(prompt="I fell off my bike")
```
> "Result: I got hurt"

---

```python
@task('translate_to_python')
def python_generator(prompt:str) -> str:
    return gptj(dict(prompt=prompt))
```

```python
python_generator(prompt="calculate the sum of even numbers from 4 to 40")
```
> "sum(x for x in range(4,41,2))\n"

```python
sum(x for x in range(4,41,2))
```
> 418

---
***Example 4: Chatbot***

```python
from prompt_engineering import chatbot
```
*Note: `@chatbot` dynamically updates the prompt with the conversation so far so that the model can have a better contextual awareness and refer to things mentioned previously in the conversation*

```python
from prompt_engineering import list_chatbots
```
```
(
 'friend',
 'ecommerce',
 'javascript_expert'
)
```
```python
@chatbot("friend")
def chitchat(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))

while True:
    chitchat(prompt=input(">"))
```
> You: what are you doing?
>> Max: Just chatting with you!

> You: thats kinda boring
>> Max: I don't think so. I enjoy talking to you.

> You: do you now
>> Max: Yes, I do. You're very friendly and easy to talk to.

> You: thanks - you too
>> Max: You're welcome.

> You: my name is Mohammed
>> Max: It's nice to meet you, Mohammed.

> You: thanks
>> Max: You're welcome.

> You: whats my name?
>> Max: Your name is Mohammed.

> You: yes thats right
>> Max: I'm glad I could help.

---
***Example 5: Advanced (Question Answering on a Table)***
```python
from prompt_engineering import to_csv

table = to_csv(
    data=[
        dict(fruit="apple",count=1,colour="red"),
        dict(fruit="banana",count=2,colour="yellow"),
        dict(fruit="mango",count=0,colour="orange")
    ],
    column_names=("fruit","count","colour"),
    delimiter="|"
)
```
```
fruit|count|colour
apple|1|red
banana|2|yellow
mango|0|orange
```


```python
gptj(dict(prompt=f'{table}\nWhat is the yellow fruit?'))
```
> "It is mango."

```python
@task("query_csv")
def query_table(prompt:str) -> str:    
    return gptj(dict(prompt=prompt))
```

```python
query_table(prompt=f'{table}\nWhat is the yellow fruit?')
```
> "A: Banana"

---
***Example 6: Advanced (NLU)***

```python
from prompt_engineering import from_csv

@task("topic_classification")
def intent_classification(prompt:str) -> str:
    return gpt3(dict(prompt=prompt))

@task("translate_to_csv")
def slot_extraction(prompt:str) -> str:    
    return gpt3(dict(prompt=prompt))

def nlu(prompt:str) -> dict:
    intent = intent_classification(prompt)
    slots = slot_extraction(prompt)
    return dict(
        Intent = intent.lstrip('The topic of this article is:'),
        Slots = from_csv(lines=slots.strip().split('\n'), delimiter="|")
    )
```

```python
nlu("Can i book a table at a Bento or Sushi restaurant for Friday please")
```

```json
{
  "Intent": "Food",
  "Slots": [
    {
      "Restaurant type": "Bento or Sushi",
      "Date": "Friday"
    }
  ]
}
```
---

## ChangeLog
- 0.0.6 @chatbot added for dynamic prompts which enable contextual dialogues
- 0.0.5 more prompts added. from_csv method added. nlu example
- 0.0.4 more prompts added
- 0.0.3 to_csv method added. cache flag added to @api
- 0.0.2 more prompts added
- 0.0.1 initial release

---
## TODO
- [x] complete all prompts