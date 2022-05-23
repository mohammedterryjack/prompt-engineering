PROMPTS = dict(
    autocomplete=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter=""),
    autocomplete_analogy=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    autocomplete_logical=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    conditional_nlg=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    topic_classification=dict(
        description=None,
        examples=[
            (
                "An international team of astronomers has obtained the clearest images yet of the merger of two distant clusters of galaxies, calling it one of the most powerful cosmic events ever witnessed.",
                "The topic of this article is: Science and Technology"
            ),
            (
                "AP - A car bomb exploded early Sunday near a U.S. military convoy on the road leading to Baghdad's airport, Iraqi police said, and a witness said two Humvees were destroyed.",
                "The topic of this article is: World"
            ),
            (
                "The former Argentine football star, Diego Armando Maradona, traveled on Monday to Cuba to continue his treatment against his addiction to drugs.",
                "The topic of this article is: Sports"
            ),
            (
                "Duke Energy Corp. reports third-quarter net income of  $389 million, or 41 cents per diluted share, sharply above earnings of  $49 million, or 5 cents per diluted share, in the same period last year.",
                "The topic of this article is: Business"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    intent_classification=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    sentiment_analysis=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    slot_extraction=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    summarisation=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    elaboration=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    hashtags=dict(
        description="The following is a list of companies and the categories they fall into. Provide a list for each of the companies!",
        examples=[
            (
                "Facebook",
                "#Social media, #Technology."
            ),
            (
                "LinkedIn",
                "#Social media, #Technology, #Enterprise, #Careers."
            ),
            (
                "Uber",
                "#Transportation, #Technology, #Marketplace."
            ),
            (
                "Unilever",
                "#Conglomerate, #Consumer Goods."
            ),
            (
                "Mcdonalds",
                "#Food, #Fast Food, #Logistics, #Restaurants."
            ),
            (
                "FedEx",
                "#Logistics, #Global Delivery Network."
            ),
            (
                "PayPal",
                "#Social, #Internet, #Payments, #Financial Services."
            ),
            (
                "TicTok",
                "#Social media, #Technology, #Online Video."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter=": "
    ),
    simplification=dict(
        description="The following sentences contain business jargon. Rewrite them using simple words.",
        examples=[
            (
                "The fund managers hope to increase yields by taking on leverage.",
                "Simple: The fund managers hope to get more return on their investments by borrowing money."
            ),
            (
                "I need to finish due diligence on this company before I can decide.",
                "Simple: I need to finish background research on this company before I can decide."
            ),
            (
                "Can you please get this document over the wall?",
                "Simple: Can you please send this document?"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_table=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    translate_to_python=dict(
        description='Write a Python program for the instructions given',
        examples=[
            (
                'calculate the sum of all positive integers smaller than 8.',
                'sum(x for x in range(8))'
            ),
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_javascript=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    translate_from_table=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    translate_from_python=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    translate_from_emojis=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    question_answering=dict(
        description='I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".',
        examples=[
            (
                "What is human life expectancy in the United States?",
                "A: Human life expectancy in the United States is 78 years."
            ),
            (
                "Who was president of the United States in 1955?",
                "A: Dwight D. Eisenhower was president of the United States in 1955."
            ),
            (
                "What is the square root of banana?",
                "A: Unknown"
            ),
            (
                "How does a telescope work?",
                "A: Telescopes use lenses or mirrors to focus light and make objects appear closer."
            ),
            (
                "Where were the 1992 Olympics held?",
                "A: The 1992 Olympics were held in Barcelona, Spain."
            ),
            (
                "How many squigs are in a bonk?",
                "A: Unknown"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    query_table=dict(
        description="Answer questions about the table.",
        examples=[
            (
                '''Name | Birth place | Age | Personality | Friend
Jane | Germany | 10 | Extroverted | Mike
Mary | London | 200 | Introverted | Mohammed
Edwardo | Spain | 30 | Extroverted | Ricardo
Marina | Italy | 33 | Introverted | Saanvi''',
                '''Who is the oldest?
A: Mary

Where is Edwardo from?
A: Spain

Where is Mike from?
A: None

How old is the person whose friend is Saanvi?
A: 33

Who lives in Italy?
A: Marina'''
            ),
            (
                '''Ship Name | Color | Total Passengers | Status | Captain
Symphony | White | 7700 | Active | Mike
Wonder | Grey | 7900 | Under Construction | Anna
Odyssey | White | 5800 | Active | Mohammed
Quantum | White | 5700 | Active | Ricardo
Mariner | Grey | 4300 | Active | Saanvi''',
                '''Which active ship carries the most passengers?
A: Symphony

What is the color of the ship whose captain is Saanvi?
A: Grey

How many passengers does Ricardo's ship carry?   
A: 5700'''
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    chatbot=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n")
)

list_tasks = lambda : tuple(PROMPTS.keys())
ERROR_MESSAGE = "'{task_name}' is an unrecognised task. Try one of the following:\n" + '\n'.join(list_tasks())