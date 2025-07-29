import json
import os
from datetime import datetime

def process_documents(input_dir):
    result = {
        "metadata": {
            "input_documents": [],
            "persona": "Example Persona",
            "job_to_be_done": "Summarize key insights",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": [],
        "subsection_analysis": []
    }

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            doc_name = filename
            result["metadata"]["input_documents"].append(doc_name)
            # Simulate section extraction
            result["extracted_sections"].append({
                "document": doc_name,
                "page": 1,
                "section_title": "Sample Section Title",
                "importance_rank": 1
            })
            result["subsection_analysis"].append({
                "document": doc_name,
                "page": 1,
                "refined_text": "This is a refined insight from the section."
            })

    return result

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    output_path = os.path.join(output_dir, "output.json")

    result = process_documents(input_dir)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()