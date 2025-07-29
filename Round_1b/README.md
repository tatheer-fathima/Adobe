# Adobe India Hackathon 2025 – Round 1B

## Objective
Extract relevant sections based on persona and job-to-be-done.

## Run Instructions

### Build Docker Image
```
docker build --platform linux/amd64 -t persona-doc-extractor:latest .
```

### Run Docker Container
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none persona-doc-extractor:latest
```