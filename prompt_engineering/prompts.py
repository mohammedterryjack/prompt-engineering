from prompt_engineering.utils import to_csv

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
    translate_to_csv=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
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
    translate_from_csv=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
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
    query_csv=dict(
        description="Answer questions about the table.",
        examples=[
            (
                to_csv(
                    data=[
                        {"Name":"Jane","Birth place":"Germany","Age":"10","Personality":"Extroverted","Friend":"Mike"},
                        {"Name":"Mary","Birth place":"London","Age":"200","Personality":"Introverted","Friend":"Mohammed"},
                        {"Name":"Edwardo","Birth place":"Spain","Age":"30","Personality":"Extroverted","Friend":"Ricardo"},
                        {"Name":"Jane","Birth place":"Germany","Age":"10","Personality":"Extroverted","Friend":"Ricardo"},
                        {"Name":"Marina","Birth place":"Italy","Age":"33","Personality":"Introverted","Friend":"Saanvi"},
                    ],
                    column_names=["Name","Birth place","Age","Personality","Friend"],
                    delimiter="|"
                ),
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
                to_csv(
                    data=[
                        {"Ship Name":"Symphony","Color":"White","Total Passengers":"7700","Status":"Active","Captain":"Mike"},
                        {"Ship Name":"Wonder","Color":"Grey","Total Passengers":"7900","Status":"Under Construction","Captain":"Anna"},
                        {"Ship Name":"Odyssey","Color":"White","Total Passengers":"5800","Status":"Active","Captain":"Mohammed"},
                        {"Ship Name":"Quantum","Color":"White","Total Passengers":"5700","Status":"Active","Captain":"Ricardo"},
                        {"Ship Name":"Mariner","Color":"Grey","Total Passengers":"4300","Status":"Active","Captain":"Saanvi"},
                    ],
                    column_names=["Ship Name","Color","Total Passengers","Status","Captain"],
                    delimiter="|"
                ),
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