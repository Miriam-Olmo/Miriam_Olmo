import requests as rq



def get_data(url):
    response = rq.get(url)
    data = response.json()
    print(data)


get_data('https://swapi.info/api/people')    