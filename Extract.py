
import Constants
from Cocktails import Cocktail
from pip._vendor import requests

class Extract:

    def extract_data(self):

        print("Data extraction function")

        self.cocktails=[]

        for _ in range(Constants.NUM_COCKTAILS):

            data = requests.get(url=Constants.API_URL)

            if (data.raise_for_status() is None):
                print("Obtained data")
                self.cocktails.append(data)

        return self.cocktails
