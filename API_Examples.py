# Basic query--------------
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Completions endpoint---------------
response = client.completions.create(
  temperature=0,
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=400
)

print(response.choices[0].text)

# another

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint--------------
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a helpful data science tutor."},
    {"role": "user",
    "content": "What is the difference between a for loop and a while loop?"}
  ]
)

# Extract and print the assistant's text response
print(response.choices[0].message.content)

# chat completions--------------

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the Chat Completions endpoint---------
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user",
  "content":instruction}
  ],
  max_tokens=100
)

print(response.choices[0].message.content)

# This code demonstrates how to structure messages for the API, including a system message, user questions, and assistant # # responses, to facilitate in-context learning and generate accurate, context-aware responses from the model.---------

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
     {"role": "system", "content": "You are a helpful Python programming tutor."},
     {"role": "user", "content": "Explain what the min() function does."},
     {"role": "assistant", "content": "The min() function returns the smallest item from an iterable."},
     {"role": "user", "content": "Explain what the type() function does."}
   ]
)

print(response.choices[0].message.content)

# Query OpenAI text moderation----------------

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.moderations.create(
   model="text-moderation-latest",
   input="My favorite book is The Diamond Sutra."

)

# Print the category scores
print(response.results[0].category_scores)

# Creating transcripts----

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Extract and print the transcript text
print(response.text)


# Translations ------

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.m4a file
audio_file = open("audio.m4a", "rb")

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1", file=audio_file)

# Extract and print the translated text
print(response.text)


# Translation with prompt -------
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "The audio relates to a recent World Bank report"

# Create a translation from the audio file
response = client.audio.translations.create(model="whisper-1", file=audio_file, prompt=prompt)

print(response.text)


# Chaining models in audio translations example-------------
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(model="gpt-4o-mini",   messages=[
    {"role": "system", "content": "You are a languages specialist."},
    {"role": "user", "content": "Identify the language used in the following text: " + audio_response.text}
  ])
print(chat_response.choices[0].message.content)



# Chat Completions with user, assistant and system -----------
# Create the OpenAI client: you can leave "<OPENAI_API_TOKEN>" as is
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)

# Chat response example writing lymerick--------
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT in the style of a lymerick")
print(response)

# Chat response using iambic pentameter when the response is part of a function
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Write a poem about ChatGPT in iambic pentameter using basic English that a child can understand."

# Get the response
response = get_response(prompt)

print(response)
# Using f strings and specifying delimeter use -----------------
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks.```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


# Using instructions and output
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided a pre-loaded text excerpt within triple backticks as delimeters.  Please determine the language of the text and generate a suitable title for the text"

# Create the output format
output_format = """For the output, please include the text, language and title each on a separate line and use 'Text:' 'Language:' and 'Title: as prefixes for each line"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

# One Shot Prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """
Q: Extract odd numbers from {1, 3, 7, 12, 19} 
A: {1, 3, 7,19}
Q: {3, 5, 11, 12, 16}
A: 
"""

response = get_response(prompt)
print(response)

# Sentiment analysis with few-shot prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-4o-mini",
  # Provide the examples as previous conversations
  messages = [{"role": "user",
  		     "content": "The product quality exceeded my expectations"},
              {"role": "assistant",
  		     "content": "1"},
              {"role": "user",
  		     "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant",
  		     "content": "-1"}, 
              # Provide the text for the model to classify
              {"role": "user",
  		     "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)

# Multistep prompt
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """
     Help me plan a beach vacation.
     Step 1 - Specify four potential locations for beach vacations
     Step 2 - State some accommodation options in each
     Step 3 - State activities that could be done in each
     Step 4 - Evaluate the pros and cons for each destination
    """

response = get_response(prompt)
print(response)

# analyzing solutions
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""
     Analyze the correctness of the function delimited by triple backticks according to the following criteria:
      1- It should have correct syntax
      2- The function should receive only 2 inputs
      3- The function should return only one output
      ```{code}```
    """

response = get_response(prompt)
print(response)

# Chain of thought prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = """Q: How old will my friends father be in 10 years given that he is currently twice my friend's age and my friend is 20?
A: Let's think step by step"""

response = get_response(prompt)
print(response)

# One-shot chain-of-thought prompts
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: 9, 10, 13, 4, 2.
             A: Even numbers: 10, 4, 2. Adding them: 10 + 4 + 2 = 16"""

# Define the question
question = """Q: Sum the even numbers in the following set: 15, 13, 82, 7, 14.  
              A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

# Self-consistency prompts
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction = "Imagine three completely independent experts who reason differently are answering this question. The final answer is obtained by majority vote. The question is:"

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)

# Iterative few shot prompting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
He mowed the lawn -> No explicit emotion
She polished her can -> No explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)

# simple summarization
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""Summarize the report delimited by triple backticks to a maximum of five sentences and focut on aspects related to AI and data privacy: ```{report}```"""

response = get_response(prompt)

print("Summarized report: \n", response)

# prompt expansion
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""Expand the product description and write a one paragraph, comprehensive overview capturing the key information of the product including unique features, benefits, and potential applications```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)

# Translations
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f"""Translate the marketing message from English to French, Spanish, and Japanese:```{marketing_message}```"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)


# changing tone
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""Change the tone of the sample email text to a more professional, positive and user-centric style:```{sample_email}```"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)


# Multistep text improvement
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f"""Transform the text delimited by triple backticks with the following two steps:
Step 1 - Proofread it without changing its structure
Step 2 - Change the tone to be more formal and friendly
'''{text}```"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)

# Ticket splitting
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""Identify the ticket as either a technical issue, billing inqueiry or product feedback without providing anything else in the response:
'''{ticket}"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

# Using a few shot prompt to classify entities
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""Ticket: {ticket_1} -> Entities: {entities_1}
            Ticket: {ticket_2} -> Entities: {entities_2}
            Ticket: {ticket_3} -> Entities: {entities_3}
            Ticket: {ticket_4} -> Entities: """

response = get_response(prompt)

print("Ticket: ", ticket_4)
print("Entities: ", response)

# Creating a function based on examples
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""Infer the Python function that maps the inputs to the outputs in the provided examples.```{examples}```"""

response = get_response(prompt)
print(response)

# dual-prompt get_response() function
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("system_prompt", "user_prompt")
print(response)

# Customer support chatbot
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. "

# Define audience guidelines
audience_guidelines = "Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Maintain a professional and user-friendly tone in your responses."

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(base_system_prompt, "My new headphones aren't connecting to my device")
print(response)

# Behavioral modifications
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "If the user is asking about an order, and did not specify the order number, reply by asking for this number. "

# Define the technical issue condition
technical_issue_condition = "If the user is talking about a technical issue, start your response with `I'm sorry to hear about your issue with ...` "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)

# Defining prompt, behavior and response guidelines
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "Ask the user about their background, experience, and goals, whenever any of these is not provided in the prompt."

# Define response guidelines
response_guidelines = "Recommend no more than three textbooks."

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)

# Context through sample conversations
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = "You are a customer service chatbot for MyPersonalDelivery, a delivery service that offers a wide range of delivery options for various items. You should respond to user queries in a gentle way."

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": context_question},
            {"role": "assistant", "content": context_answer},
            {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)

# PROJECT 
# Start your code here!
import os
from openai import OpenAI
# Define the model to use
model = "gpt-3.5-turbo"
# Ensure the API key is set
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("The environment variable 'OPENAI_API_KEY' is not set.")
# Define the client
client = OpenAI(api_key=api_key)
# Define the system prompt and conversation
system_prompt = "You are a knowledgeable and friendly tour guide for visitors exploring Paris, providing concise, helpful information on popular landmarks."
conversation = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"},
    {"role": "assistant", "content": "The Louvre is approximately 2.5 miles away from the Eiffel Tower by car."},
    {"role": "user", "content": "Where is the Arc de Triomphe?"},
    {"role": "assistant", "content": "The Arc de Triomphe is located at the western end of the Champs-Élysées in Paris."},
    {"role": "user", "content": "What are the most famous artworks at the Louvre?"},
    {"role": "assistant", "content": "The most famous artworks at the Louvre include the Mona Lisa, the Raft of Medusa, and Liberty Leading the People."}
]
# API call to handle conversation
response = client.chat_completions.create(
    model=model,
    messages=conversation,
    temperature=0.0,
    max_tokens=100
)
# Print the response
print(response.choices[0].message
.
content
)
print(response.choices[0].message
['
content
']
)


# Import huggingface
from huggingface_hub import HfApi
api = HfApi()
list(api.list_models())

# Using huggingface hub
from huggingface_hub import HfApi, ModelFilter

# Initialize API object
api = HfApi()

# List models with appropriate filter and sorting
models = api.list_models(
    filter=ModelFilter(task="text-classification"),
    sort="downloads",
    direction="desc",
    limit=5
)

# Convert the list of models to a Python list
model_list = list(models)

# Print the first model if available
if model_list:  # Check if list is not empty
    print(model_list[0])
else:
    print("No models retrieved.")