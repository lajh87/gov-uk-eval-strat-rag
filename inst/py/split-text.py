# Function loads all markdown files in a folder, chunks them based on defined length, then outputs the results as JSON
# 10 June 24

from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import json

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
  model_name="gpt-4",
  chunk_size=250,
  chunk_overlap=50)

# Load example document
documents = []
meta = []
directory = "data"
for file in  os.listdir(directory):
  filename = os.fsdecode(file)
  if filename.endswith(".md"): 
    with open(os.path.join(directory, filename)) as f:
      doc_in = f.read()
      new_doc = text_splitter.create_documents([doc_in])
      for doc in new_doc:
        documents = documents + [doc.page_content]
    
      for i, doc in enumerate(new_doc):
        new_meta = [{"filename": filename, "chunk": i}]
        meta = meta + new_meta

ident = []
for value in meta:
  ident.append(value["filename"]+"_"+str(value["chunk"]))

with open("data/documents.json", "w") as write_file:
    json.dump(documents, write_file, indent=4)
      
with open("data/meta.json", "w") as write_file:
    json.dump(meta, write_file, indent=4)

with open("data/id.json", "w") as write_file:
    json.dump(ident, write_file, indent=4)

