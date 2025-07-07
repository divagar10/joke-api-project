import requests
url="https://v2.jokeapi.dev/joke/Any"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    if data["type"]=="single":
        print("joke",data["joke"])
    else:
        print("setup",data["setup"])
        print("punchline",data["delivery"])