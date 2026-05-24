from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
import json
import os

documents = []

pdf_folder = "data/pdfs"

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        pdf_docs = loader.load()

        for doc in pdf_docs:
            doc.metadata["source_type"] = "pdf"

        documents.extend(pdf_docs)

csv_path = "data/csv/employees.csv"

df = pd.read_csv(csv_path)

for _, row in df.iterrows():
    text = f"""
    Employee ID: {row['employee_id']}
    Name: {row['name']}
    Department: {row['department']}
    Salary: {row['salary']}
    """

    documents.append({
        "page_content": text,
        "metadata": {
            "source": "employees.csv",
            "source_type": "csv",
            "department": row["department"]
        }
    })

json_path = "data/json/logs.json"

with open(json_path, "r") as f:
    logs = json.load(f)

for log in logs:
    text = f"""
    Timestamp: {log['timestamp']}
    Event: {log['event']}
    Severity: {log['severity']}
    """

    documents.append({
        "page_content": text,
        "metadata": {
            "source": "logs.json",
            "source_type": "json"
        }
    })

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

final_docs = []

for doc in documents:

    if isinstance(doc, dict):

        chunks = splitter.create_documents(
            [doc["page_content"]],
            metadatas=[doc["metadata"]]
        )

    else:

        chunks = splitter.split_documents([doc])

    final_docs.extend(chunks)

print(f"Total chunks created: {len(final_docs)}")

for doc in final_docs:
    print("\n====================")
    print(doc.page_content)
    print(doc.metadata)