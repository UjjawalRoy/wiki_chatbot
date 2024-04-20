import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from generate_output.preprocess import tokenize_sent

from utils.constants import chroma_data_path, embedding_model_path, collection_name

vector_db_client = chromadb.PersistentClient(path=chroma_data_path)
model = SentenceTransformer(embedding_model_path)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=embedding_model_path)


def generate_embeddings(data):
    tokenized_sentences = tokenize_sent(input_string=data)
    embeddings = model.encode(tokenized_sentences)
    return embeddings


def create_vector_db(data):
    tokenized_sentences = tokenize_sent(input_string=data)
    collection = vector_db_client.create_collection(name=collection_name,
                                                    embedding_function=embedding_func,
                                                    metadata={"hnsw:space": "cosine"})
    collection.add(documents=tokenized_sentences, ids=[f"id{i}" for i in range(len(tokenized_sentences))])
    return 'Vector database successfully created!'
