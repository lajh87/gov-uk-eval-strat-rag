import chromadb
import json 
import os
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="inst/chromadb/")
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
  api_key=os.getenv("OPENAI_API_KEY"),
  model_name="text-embedding-ada-002"
  )

#client.delete_collection(name="eval_strat")
collection = client.get_or_create_collection(name="eval_strat", embedding_function=openai_ef)

with open("data/documents.json", encoding="utf8") as json_file:
  documents = json.load(json_file)
  json_file.close()

with open("data/meta.json", encoding="utf8") as json_file:
  meta = json.load(json_file)
  json_file.close()
  
with open("data/id.json", encoding="utf8") as json_file:
  ids = json.load(json_file)
  json_file.close()


collection.add(
    documents=documents,
    metadatas=meta,
    ids=ids
)

collection.query(
    query_texts=["bies"],
    n_results=10
)
