import pandas as pd
import numpy as np
import openai
import os
from replit import db, database
from scripts.data_generation import create_embedding


def cosine_similarity(a, b):
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# search through the recycling wiki for text similar to the given query
def search_recycling_wiki(query, df, openai_api_key, n=5, pprint=True):
  df["Embedding"] = df["Embedding"].apply(eval).apply(np.array)
  print("Creating embedding for " + query)
  query_embedding = create_embedding(query, openai_api_key)
  print("Running Cosine Similarity...")
  df["Similarity"] = df["Embedding"].apply(
    lambda x: cosine_similarity(x, query_embedding))

  results = (df.sort_values("Similarity", ascending=False).head(n))["Heading and Text"]
  if pprint:
    for r in results:
      print(r[:200])
      print()
  return results

def answer_with_gpt_4(query, data, from_number, openai_api_key):
  messages = [
    {"role" : "system", "content": "You are a very enthusiastic representative of Denver County who loves to teach people about recycling and composting! Your task is to answer questions from people over text. Given the following sections from the Denver City and County's Recycling page delimited by ```, answer the person's question using that information in a text-friendly way. You should always try to give a helpful answers that uses information from the text inside ```. But, if you are 100% unsure of the answer, say \"I'm sorry, I don't know how to help you with that.\" Use at most 30 words."}
  ]

  # Access prior chat from Replit DB, if it exists
  if from_number in db.keys():
    chat = db[from_number]
    for msg in chat:
      messages.append(database.to_primitive(msg))

  df = pd.read_csv(data)
  
  context = "```"
  wiki_search_str = " ".join(search_recycling_wiki(query, df, openai_api_key, pprint=False)).replace("\n", " ")
  context += wiki_search_str
  context += "```"

  context += " Query: {}".format(query)
  messages.append({"role" : "user", "content": context})

  print(context)

  print("Awaiting OpenAI's response...")
  response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages,
    temperature = 0
  )

  print("Total Tokens in this response: " + str(response['usage']['total_tokens']))

  return response['choices'][0]['message']['content']

#print(answer_with_gpt_4("Can I recycle dirty cardboard?", "data/co_recycling_data_with_embeddings.csv", '+14129797258', os.getenv("OPENAI_API_KEY")))