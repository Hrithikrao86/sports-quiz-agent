import json
import chromadb
from chromadb.utils import embedding_functions


def get_chroma_client():
  
    return chromadb.PersistentClient(path="./chroma_db")


def get_collection():
  
    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    return collection


def load_data():
  

    collection = get_collection()

   
    if collection.count() > 0:
        print(f"Database already contains {collection.count()} facts.")
        return

    with open("./data/sports_facts.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    documents = []
    metadatas = []
    ids = []

    for index, item in enumerate(data):
        documents.append(item["fact"])
        metadatas.append({"sport": item["sport"]})
        ids.append(str(index))

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print("✅ Data inserted successfully!")


def query_facts(sport, query_text, n_results=3):


    collection = get_collection()

    results = collection.query(
        query_texts=[query_text],
        n_results=n_results,
        where={"sport": sport}
    )

    return results["documents"][0]