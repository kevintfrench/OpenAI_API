# Basic query
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Completions endpoint
response = client.completions.create(
  temperature=0,
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  max_tokens=400
)

print(response.choices[0].text)

# another

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
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

# chat completions

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user",
  "content":instruction}
  ],
  max_tokens=100
)

print(response.choices[0].message.content)

# This code demonstrates how to structure messages for the API, including a system message, user questions, and assistant # # responses, to facilitate in-context learning and generate accurate, context-aware responses from the model.

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

# Query OpenAI text moderation

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Moderation endpoint
response = client.moderations.create(
   model="text-moderation-latest",
   input="My favorite book is The Diamond Sutra."

)

# Print the category scores
print(response.results[0].category_scores)

# 

