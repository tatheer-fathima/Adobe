# Adobe India Hackathon 2025 – Round 1A

## Objective
Extract Title, H1, H2, H3 headings from PDF and output structured JSON.

## Run Instructions
### Build Docker Image
```
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

### Run Docker Container
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline-extractor:latest
```