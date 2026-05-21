import requests

updated_data = {
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_data
)

print(response.json())