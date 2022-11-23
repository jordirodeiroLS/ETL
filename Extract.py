
import Constants
from Cocktails import Cocktail
from pip._vendor import requests
import datetime
from typing import List

class Extract:

    def extract_data(self) -> List[Cocktail]:

        print("Data extraction function")

        self.cocktails=[]

        for _ in range(Constants.NUM_COCKTAILS):

            data = requests.get(url=Constants.API_URL)

            # print(data.json().keys()) # ['drinks']
            # print( type(data.json()['drinks']) ) # list
            # print( type(data.json()['drinks'][0]) ) # dict
            # print( data.json()['drinks'][0] ) # actual keys
            
            if (data.raise_for_status() is None):
                print("Obtained data")
                cocktail = self.create_cocktail(data)
                self.cocktails.append(cocktail)

        return self.cocktails

# TODO: Add cache of the API information (save to file)

    def create_cocktail(self, data) -> Cocktail:

        ingr = {}

        for count in range(15):
            if data.json()['drinks'][0]['strIngredient' + str(count + 1)] is not None and data.json()['drinks'][0]['strMeasure' + str(count + 1)] is not None:
                ingr[ data.json()['drinks'][0]['strIngredient' + str(count + 1)] ] = data.json()['drinks'][0]['strMeasure' + str(count + 1)]

        print("INGR")
        print(ingr)

        date:datetime.date = None
        if data.json()['drinks'][0]['dateModified'] is not None:
            date = datetime.datetime.strptime(data.json()['drinks'][0]['dateModified'], '%Y-%m-%d %H:%M:%S' )
        #date = datetime.datetime.strptime( '1996-12-23 15:32:45' , '%Y-%m-%d %H:%M:%S' )

        cocktail = Cocktail( 
            data.json()['drinks'][0]['idDrink'],
            data.json()['drinks'][0]['strDrink'],
            data.json()['drinks'][0]['strCategory'],
            data.json()['drinks'][0]['strIBA'],
            data.json()['drinks'][0]['strAlcoholic'],
            data.json()['drinks'][0]['strGlass'],
            data.json()['drinks'][0]['strInstructions'],
            data.json()['drinks'][0]['strDrinkThumb'],
            ingr,
            date)
        return cocktail