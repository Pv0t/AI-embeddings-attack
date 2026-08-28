import requests

WEAVIATE_URL = "http://localhost:8080"

response = requests.get(f"{WEAVIATE_URL}/v1/schema")
response.raise_for_status()

schema = response.json()

# Extract all collection (class) names
collections = [c["class"] for c in schema.get("classes", [])]

print("Collections:", collections)
