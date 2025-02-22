## Python

### Add env. variable in PowerShell:
```bash
$env:OPENAI_API_KEY = "<api_key>"
```

### Run the Python app:
```bash
streamlit run app.py
```

## Docker

### Build Docker image:

```bash
docker build -t ai-coder-app .
```

### Run Docker container:
```bash
docker run -p "8501:8501" -e "OPENAI_API_KEY=<api_key>" ai-coder-app
```

## Docker Compose

### Create _.env_ file in the base directory and add env. variable:
```
OPENAI_API_KEY=<api_key>
```

### Run Docker compose:
```bash
docker-compose up --build
```

### Stop Docker compose:
```bash
docker-compose down
```