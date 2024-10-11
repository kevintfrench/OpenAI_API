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
  "content": "The price of the product is really fair give its features"},
              {"role": "assistant", 
              "content": "positive"},
              {"role": "user", 
              "content": "____"},
              {"role": "____", "content": "____"},
              # Provide the text for the model to classify
              {"role": "____", "content": "____"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)