import requests, json

query = """
{
  Get {
    DocChunk(limit: 1) {
      _additional { vector }
    }
  }
}
"""

r = requests.post("http://localhost:8080/v1/graphql", json={"query": query})
vec = r.json()["data"]["Get"]["DocChunk"][0]["_additional"]["vector"]
print("Vector length:", len(vec))
