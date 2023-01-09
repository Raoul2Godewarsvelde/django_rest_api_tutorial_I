import pip._vendor.requests 

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/"

get_response = pip._vendor.requests.get(endpoint, json={"query": "Hello World!"})
print(get_response.text)
# print(get_response.json())
print(get_response.status_code)