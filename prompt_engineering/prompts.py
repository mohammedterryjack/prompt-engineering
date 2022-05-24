from prompt_engineering.utils import to_csv

PROMPTS = dict(
    autocomplete=dict(description=None,examples=[],example_delimiter="\n###\n",input_target_delimiter=""),
    autocomplete_analogy=dict(
        description="Create an analogy for the word given",
        examples=[
            (
                "Questions",
                "Questions are like arrows in that they can be used to point out things that need to be fixed."
            ),
            (
                "Men",
                "Men are like a jungle. They are full of danger."
            ),
            (
                "Women",
                "Women are like flowers. They are beautiful to look at."
            ),
            (
                "AI",
                "AI is like the genie in Aladdin's lamp."
            ),
            (
                "Love",
                "Love is like fire. It burns but warms at the same time."
            ),
            (
                "Sex",
                "Sex is like food. A person needs it to live."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    autocomplete_logical=dict(
        description="Predict common sense results of the following actions.",
        examples=[
            (
                "I didn't water the plant for 3 weeks.",
                "Result: The plant died"
            ),
            (
                "I went to school.",
                "Result: I got a diploma."
            ),
            (
                "I left the AC on all day.",
                "Result: I got a high utility bill."
            ),
            (
                "I helped my neighbors when their car broke down.",
                "Result: My neighbors were grateful."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
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
    sentiment_analysis=dict(
        description="Classify the sentiment. Decide whether the sentiment is positive, neutral, or negative.",
        examples=[
            (
                "I loved the new Batman movie!",
                "Positive"
            ),
            (
                "I can't stand homework",
                "Negative"
            ),
            (
                "This sucks. I'm bored 😠",
                "Negative"
            ),
            (
                "I can't wait for Halloween!!!",
                "Positive"
            ),
            (
                "My cat is adorable ❤️❤️",
                "Positive"
            ),
            (
                "I hate chocolate",
                "Negative"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
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
    summarisation=dict(
        description=None,
        examples=[
            (
                "A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.",
                "A neutron star is the collapsed core of a massive supergiant star. These ultra-dense objects are incredibly fascinating due to their strange properties and their potential for phenomena such as extreme gravitational forces and a strong magnetic field."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n\nTl;dr "
    ),
    elaboration=dict(
        description=None,
        examples=[
            (
                "- Designed by Retrolicious\n- Stretch cotton fabric\n- Side pockets\n- Rainbow stripes print",
                "In a bold rainbow-striped print, made up of exceptionally vibrant hues, this outstanding skater dress from Retroliciousis on every spectrum of vintage-inspired style. Made from a stretchy cotton fabric and boasting a round neckline, a sleeveless fitted bodice, and a gathered flare skirt with handy side pockets, this adorable fit-and-flare dress is truly unique and so retro-chic."
            ),
            (
                "- Black canvas purse\n- Rainbow space print\n- Leather trim\n- Two securely-zipped compartments",
                "Take a bit of camp charm with you wherever you go with this black canvas purse! Adorned with a rainbow space motif print, black faux-leather trim, two securely-zipped compartments, and adjustable crossbody strap, this ModCloth-exclusive bag makes sure you command a smile wherever you wander."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    horror_story=dict(
        description="Creates two to three sentence short horror stories from a topic input",
        examples=[
            (
                "Breakfast",
                "He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton."
            ),
            (
                "Wind",
                "I was lying in bed, trying to get to sleep, when I heard the wind howling outside my window. It sounded like something was trying to get in."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
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
    grammar_correction=dict(
        description="Correct this to standard English:",
        examples=[
            (
                "She no went to the market.",
                "Correction: She didn't go to the market."
            ),
            (
                "he no go dentist no more",
                "Correction: he doesn't go to the dentist anymore."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_csv=dict(
        description="Slot extraction: Extract keywords and determine their type",
        examples=[
            (
                "Can i book a table for me and my husband tonight? Anything free at half nine?",
                to_csv(
                    data=[
                        dict(People="me and my husband",Date="tonight",Time="half nine")
                    ],
                    column_names=["People","Date","Time"],
                    delimiter="|"
                )
            ),
            (
                "Is there a table free in an hour?",
                to_csv(
                    data=[
                        dict(Time="in an hour",Date="today")
                    ],
                    column_names=["Time","Date"],
                    delimiter="|"
                )
            ),

            (
                "There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.",
                to_csv(
                    data=[
                        {"Fruit":"Neoskizzle","Color":"Purple","Flavor":"Sweet"},
                        {"Fruit":"Loheckle","Color":"Grayish blue","Flavor":"Tart"},
                        {"Fruit":"Pounit","Color":"Bright green","Flavor":"Savory"},
                        {"Fruit":"Loopnova","Color":"Neon pink","Flavor":"Cotton candy"},
                        {"Fruit":"Glowl","Color":"Pale orange","Flavor":"Sour and bitter"},
                    ],
                    column_names=["Fruit","Color","Flavor"],
                    delimiter="|"                    
                ),
            ),
            (
                "Judy has a 3 o'clock meeting at Walmart. Mike has a 2pm call with Sainsburys. Mary don't forget to collect your dry cleaning at 1pm sharp!",
                to_csv(
                    data=[
                        {"People":"Judy","Time":"3 O'clock","Location":"Walmart"},
                        {"People":"Mike","Time":"2pm","Location":"Sainsburys"},
                        {"People":"Mary","Time":"1pm", "Location":""}
                    ],
                    column_names=["People","Time","Location"],
                    delimiter="|"                    
                )
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_teaser=dict(
        description="Write a creative ad for the following product to run on Facebook aimed at parents:",
        examples=[
            (
                "Learning Room is a virtual environment to help students from kindergarten to high school excel in school.",
                "Are you looking for a way to help your child excel in school? Look no further than Learning Room! Our virtual environment is designed to help students from kindergarten to high school learn and grow. With our help, your child will be able to get ahead in school and achieve their academic goals."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_german=dict(
        description="Translate this into German:",
        examples=[
            (
                "What rooms do you have available?",
                "Welche Zimmer haben sie frei?"
            ),
            (
                "When he mentioned the corkscrew I thought he'd be pulling my leg",
                "Als er den Korkenzieher erwähnte dachte ich, er wollte mich verarschen"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_french=dict(
        description="Translate this into French:",
        examples=[
            (
                "What rooms do you have available?",
                "Quelles sont les chambres disponibles?"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_to_spanish=dict(
        description="Translate this into Spanish:",
        examples=[
            (
                "What rooms do you have available?",
                "¿Cuáles son las habitaciones disponibles?"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),    
    translate_to_japanese=dict(
        description="Translate this into Japanese:",
        examples=[
            (
                "What rooms do you have available?",
                "何室がありますか?"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),    
    translate_to_python=dict(
        description='Write a Python program for the instructions given',
        examples=[
            (
                'calculate the sum of all positive integers smaller than 8.',
                'sum(x for x in range(8))'
            ),
            (
                "check a word starts with a certain prefix?",
                "word.startswith(prefix)"
            ),
            (
                "make a delay for 10 seconds",
                "from time import sleep; sleep(10)"
            ),
            (
                "access the last element of list m",
                "m[-1]"
            ),
            (
                "sort a list q from high to low",
                "q.sort(reverse=True)"
            ),
            (
                "find the most common element of a list c",
                "from collections import Counter; Counter(c).most_common()"
            ),
            (
                "count the occurrences of an element m in list b",
                "b.count(m)"
            ),
            (
                "find the length of list b",
                "len(b)"
            ),
            (
                "convert a list of strings, b, into a list of integers",
                "list(map(int,b))"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_from_french=dict(
        description="Translate this into English:",
        examples=[
            (
                "Quelles sont les chambres disponibles?",
                "What rooms do you have available?"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    translate_from_python=dict(
        description="Explain what the python code does:",
        examples=[
            (
                '''def remove_common_prefix(x, prefix, ws_prefix): 
    x["completion"] = x["completion"].str[len(prefix) :] 
    if ws_prefix: 
        # keep the single whitespace as prefix 
        x["completion"] = " " + x["completion"] 
return x''',
                "A function that takes a dataframe and a prefix as input and returns a dataframe with the prefix removed from the completion column."
            ),
            (
                '''class Log:
    def __init__(self, path):
        dirname = os.path.dirname(path)
        os.makedirs(dirname, exist_ok=True)
        f = open(path, "a+")

        # Check that the file is newline-terminated
        size = os.path.getsize(path)
        if size > 0:
            f.seek(size - 1)
            end = f.read(1)
            if end != "\n":
                f.write("\n")
        self.f = f
        self.path = path

    def log(self, event):
        event["_event_id"] = str(uuid.uuid4())
        json.dump(event, self.f)
        self.f.write("\n")

    def state(self):
        state = {"complete": set(), "last": None}
        for line in open(self.path):
            event = json.loads(line)
            if event["type"] == "submit" and event["success"]:
                state["complete"].add(event["id"])
                state["last"] = event
        return state''',
                "The constructor creates a directory for the log file if it doesn't exist. The log() method writes a JSON-encoded event to the log file. The state() method returns a dictionary with the set of complete tasks and the most recent event."
            ),
            (
                '''def randomly_split_dataset(folder, filename, split_ratio=[0.8, 0.2]):
    df = pd.read_json(folder + filename, lines=True)
    train_name, test_name = "train.jsonl", "test.jsonl"
    df_train, df_test = train_test_split(df, test_size=split_ratio[1], random_state=42)
    df_train.to_json(folder + train_name, orient='records', lines=True)
    df_test.to_json(folder + test_name, orient='records', lines=True)
randomly_split_dataset('finetune_data/', 'dataset.jsonl')''',
                "Randomly split a dataset into train and test. The function doesn't return anything, it just saves the train and test datasets in the given folder."
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n\n"
    ),
    translate_from_emoji=dict(
        description="Convert emojis into text",
        examples=[
            (
                "👨👴🚗🕒",
                "Back to the Future"
            ),
            (
                "🤵🦇",
                "Batman"
            ),
            (
                "🚗🤖",
                "Transformers"
            )
        ],
        example_delimiter="\n###\n",
        input_target_delimiter="\n"
    ),
    question_answering=dict(
        description='I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".',
        examples=[
            (
                "How many moons does Mars have?",
                "A: Two, Phobos and Deimos."
            ),
            (
                "What's a language model?",
                "A: A language model is a statistical model that describes the probability of a word given the previous words."
            ),
            (
                "What is a statistical model?",
                "A: A statistical model is a model that describes the probability of an event occurring."
            ),
            (
                "Who is Alvan Muntz?",
                "A: Unknown"
            ),
            (
                "What is Kozar-09?",
                "A: Unknown"
            ),
            (
                "Who is George Lucas?",
                "A: George Lucas is American film director and producer famous for creating Star Wars."
            ),
            (
                "What is the capital of California?",
                "A: Sacramento."
            ),
            (
                "What orbits the Earth?",
                "A: The Moon."
            ),
            (
                "Who is Fred Rickerson?",
                "A: Unknown"
            ),
            (
                "What is an atom?",
                "A: An atom is a tiny particle that makes up everything."
            ),
            (
                "What is Devz9?",
                "A: Unknown"
            ),
            (
                "Who is Batman?",
                "A: Batman is a fictional comic book character."
            ),
            (
                "What is torsalplexity?",
                "A: Unknown"
            ),
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
    question_answering_javascript=dict(
        description='''This is a chatbot that can answer questions about JavaScript:

How do I combine arrays?
JavaScript chatbot: You can use the concat() method.
How do you make an alert appear after 10 seconds?
JavaScript chatbot: You can use the setTimeout() method.
''',
        examples=[],
        example_delimiter="",
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
    chatbot=dict(
        description='''The following is a text message conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
        
AI: What have you been up to?
You: Watching old movies.
AI: Did you watch anything interesting?
You: ''',
        examples=[],
        example_delimiter="",
        input_target_delimiter="\n"
    ),
    chatbot_ecommerce=dict(
        description=None,
        examples=[
            (
                "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\n",
                '''Conversation:
Hi, I have a question for you.
Max: Hi there, happy to help!'''
            ),
            (
                "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Male.\n\n",
                '''Conversation:
Hi, had a question
Max: Hi there, happy to help!
Is there no way to return a product? I got your blue T-Shirt size small but it doesn't fit.
Max: I'm sorry to hear that. Unfortunately we don't have a return policy. 
That's a shame. 
Max: Is there anything else i can do for you?

###'''
            ),
            (
                "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\n",
                '''Conversation:
Hi, I was wondering when you'll have the "Blue & White" t-shirt back in stock?
Max: Hi, happy to assist! We currently don't have it in stock. Do you want me to send you an email once we do?
Yes!
Max: Awesome. What's your email?
anc@gmail.com
Max: Great. I'll send you an email as soon as we get it.

###'''
            ),
            (
                "The following is a conversation between a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following are important points about the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\nUser gender: Female.\n\n",
                '''Conversation:
Hi, how much time does it take for the product to reach me?
Max: Hi, happy to assist! It usually takes 5 working days to reach you.
Got it! thanks. Is there a way to shorten that delivery time if i pay extra?
Max: I'm sorry, no.
Got it. How do i know if the White Crisp t-shirt will fit my size?
Max: The size charts are available on the website.
Can you tell me what will fit a young women.
Max: Sure. Can you share her exact size?

###'''
            )
        ],
        example_delimiter="\n",
        input_target_delimiter="\n"
    ),
)

list_tasks = lambda : tuple(PROMPTS.keys())
ERROR_MESSAGE = "'{task_name}' is an unrecognised task. Try one of the following:\n" + '\n'.join(list_tasks())