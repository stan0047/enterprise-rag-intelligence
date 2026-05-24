from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.ingest import final_docs
from app.rbac import has_access

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    final_docs,
    embedding_model
)

vectorstore.save_local("faiss_index")

print("FAISS vector database created successfully")

query = "Who handles payroll?"

results = vectorstore.similarity_search(query, k=3)

print("\nTop Results:\n")

user_role = "HR"

print(f"\nCurrent User Role: {user_role}")

for doc in results:

    if has_access(user_role, doc.metadata):

        print("===================")
        print(doc.page_content)
        print(doc.metadata)

    else:

        print("===================")
        print("ACCESS DENIED")
        print(doc.metadata)