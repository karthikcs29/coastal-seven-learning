import requests

while True:

    prompt = input("You: ")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    print("\nStatus Code:", response.status_code)

    data = response.json()

    print("\nFull Response:")
    print(data)

    if "response" in data:
        print("\nAI:", data["response"])
    else:
        print("\nNo 'response' key found.")