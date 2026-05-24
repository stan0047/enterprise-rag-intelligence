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

user_role = input("Enter role (HR / Finance / Engineering / Admin): ")

query = input("Enter your question: ")

results = vectorstore.similarity_search_with_score(query, k=3)

authorized_docs = []

confidence_scores = []

for doc, score in results:

    if has_access(user_role, doc.metadata):

        authorized_docs.append(doc)

        confidence = round(1 / (1 + score), 2)

        confidence_scores.append(confidence)

if len(authorized_docs) == 0:

    print("\nACCESS DENIED")
    exit()

context = ""

for i, doc in enumerate(authorized_docs):

    context += f"\n[Document {i+1}]\n"

    context += doc.page_content

    context += "\n"

average_confidence = f"{round(sum(confidence_scores) / len(confidence_scores), 2) * 100}%"

answer = f"""
================================================

ENTERPRISE RAG RESPONSE

================================================

User Role:
{user_role}

Question:
{query}

------------------------------------------------

Grounded Answer:

{context}

------------------------------------------------

Confidence Score:
{average_confidence}

------------------------------------------------

Sources:
"""

sources = set()

for doc in authorized_docs:

    source = doc.metadata.get("source", "unknown")

    sources.add(source)

for source in sources:

    answer += f"\n- {source}"

print(answer)