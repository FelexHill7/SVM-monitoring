import requests

SVM_SERVER = "http://127.0.0.1:5002"

if __name__ == "__main__":
    # Dummy MNIST input
    dummy_input = [0] * 784  # 784 zeros

    response = requests.post(
        f"{SVM_SERVER}/api/classify",
        json={"data": dummy_input}
    )

    print(response.status_code)
    print("Response:", response.json())