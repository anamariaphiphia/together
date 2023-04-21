import requests

def get_data():
    response = requests.get('https://api.github.com/')
    print(response)
    for url in response:
        try:
            if response == 200:
               return response

        except error as errorMsg:
            print("something went wrong")














