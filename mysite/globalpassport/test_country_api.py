import requests
import urllib
from urllib.request import urlretrieve


def test_api():
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/GB"
    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "d60eca41e9msh28b55b48d2ff106p197cd0jsn0f40789fc5db"
        }
    response = requests.request("GET", url, headers=headers)
    print(response.text)



def download_flag():
    url = "http://commons.wikimedia.org/wiki/Special:FilePath/Flag%20of%20Russia.svg"
    urlretrieve(url, "Russia.jpg")


def main():
    test_api()
    download_flag()


main()


# def urban_dictionary(search_term):
#     url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
#     querystring = {"term":search_term}
#     headers = {
#         'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
#         'x-rapidapi-key': "d60eca41e9msh28b55b48d2ff106p197cd0jsn0f40789fc5db"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring).json()
#     definitions = response['list']
