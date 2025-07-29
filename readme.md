# 📄 Adobe India Hackathon 2025 –  Submission

---

## 🧠 Round 1A – PDF Outline Extractor

### 🎯 Objective
Extract a clean, structured outline from raw PDFs including:
- Title  
- Headings: H1, H2, H3  
- Page numbers  

### 🛠️ Approach
- Used **PyMuPDF** to extract text and analyze font size & structure.  
- Title is inferred from the largest text on page 1.  
- Headings are classified as H1, H2, H3 based on relative font sizes and formatting.  
- Output format adheres strictly to the required JSON structure.  

### 📦 Output Example
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## 🧑‍💼 Round 1B – Persona-Based Insight Extractor

### 🎯 Objective
Given a **persona** and **job-to-be-done**, identify the most relevant sections from multiple PDFs.

### 🛠️ Approach
- Simulated keyword and intent matching to evaluate persona relevance to document content.  
- Ranked and returned the most relevant sections with summary and metadata.  
- Designed to support future integration of lightweight language models (e.g. MiniLM, TinyBERT).  

### 📦 Output Format
```json
{
  "persona": "UX Researcher",
  "task": "Understand design trends",
  "timestamp": "2025-07-29T10:30:00Z",
  "documents": ["design-guide.pdf", "ui-ux-insights.pdf"],
  "sections": [
    {
      "title": "Modern UI Trends",
      "page": 12,
      "document": "design-guide.pdf",
      "rank": 1,
      "summary": "Discusses flat design, neumorphism, and accessibility best practices."
    },
    {
      "title": "User Research Patterns",
      "page": 3,
      "document": "ui-ux-insights.pdf",
      "rank": 2,
      "summary": "Explores qualitative research, A/B testing, and feedback loops."
    }
  ]
}
```

---

## 🧪 How to Run

### 🐳 Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-insight-extractor .
```

### ▶️ Run Docker Container
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-insight-extractor
```

---

## 📁 Repo Structure
```
.
├── main.py                   # Core logic for Round 1A / 1B
├── Dockerfile                # Container configuration
├── requirements.txt          # Python dependencies
├── input/                    # Place input PDFs here
├── output/                   # Output JSON will be generated here
├── README.md                 # This file
└── approach_explanation.md   # Detailed methodology
```

---

## ✅ Constraints Compliance
- ✅ Offline (no network access)  
- ✅ Runtime < 10 seconds (Round 1A)  
- ✅ Model size < 200MB (1A), < 1GB (1B)  
- ✅ CPU-only AMD64 environment  

---

## 🙌 Thank You
Looking forward to contributing to document intelligence innovation!
