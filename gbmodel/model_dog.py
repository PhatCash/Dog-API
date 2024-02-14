"""
HTTP request with GET:
https://dog.ceo/dog-api/
"""
from .Model import Model
import requests

class model(Model):
    def __init__(self):
        self.base_url = 'https://dog.ceo/api'
      
    def breeds(self):
        """
        Request for all breeds
        :return: A JSON object
        """
        response = requests.get(f"{self.base_url}/breeds/list/all")
        return response.json()

    def a_breed(self, breed):
        """
        Request for a random image based on the breed, max 10
        :param breed: String
        :return: A JSON object with image URLs
        """
        response = requests.get(f"{self.base_url}/breed/{breed}/images/random/10")
        return response.json()
