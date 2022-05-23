PROMPTS = dict(
    autocomplete=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter=""),
    autocomplete_analogy=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    autocomplete_logical=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    conditional_nlg=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    topic_classification=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
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
        examples=[],
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
    question_answering=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    query_table=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n"),
    chatbot=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter="\n")
)

list_tasks = lambda : tuple(PROMPTS.keys())
ERROR_MESSAGE = "'{task_name}' is an unrecognised task. Try one of the following:\n" + '\n'.join(list_tasks())