from src.data_loader import load_all_documents
from src.embeddings import EmbeddingPipeline
from src.vector_store import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    #To check If src/data_loader.py is working properly and loading all the documents
    # docs = load_all_documents("data")
    # print(f"Loaded {len(docs)} documents.")

    # To check If src/embeddings.py is working properly and generating embeddings
    # chunks = EmbeddingPipeline().chunk_documents(docs)
    # print(f"Split into {len(chunks)} chunks.")
    # chunk_vector = EmbeddingPipeline().embed_chunks(chunks)
    # print(f"Embeddings shape: {chunk_vector.shape}")

    store =  FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)

    store.load()
    # print(store.query("What is Blocking Technique?", top_k=3))

    rag_search = RAGSearch()
    query = "What is bitcoin?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Answer:", summary)