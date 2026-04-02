import requests
import time

print("Sending classify request... (this may take a few minutes)")
start = time.time()
r = requests.post("http://127.0.0.1:5002/api/classify", json={"data": [0] * 784}, timeout=600)
elapsed = time.time() - start

print(f"Status: {r.status_code}")
print(f"Response: {r.json()}")
print(f"Wall-clock: {elapsed:.2f}s")

print("\nFetching /metrics ...")
m = requests.get("http://127.0.0.1:5002/metrics")
print(m.text)
