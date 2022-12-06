
import Constants
from Cocktails import Cocktail
from pip._vendor import requests
import datetime
from typing import List

from Database import Database

class Extract:

    def extract_data(self) -> List[Cocktail]:

        self.cocktails : List[Cocktail] = []

        self.database = Database()
        new = self.database.first_init()
        self.database.connect_db()
        aux_cocktails = self.database.get_information_db_cocktails()
        aux_ingredients = self.database.get_information_db_ingredients()

        if new is False:
            self.dict_to_cocktails(aux_cocktails, aux_ingredients)
            return self.cocktails

        for _ in range(Constants.NUM_COCKTAILS):

            data = requests.get(url=Constants.API_URL)
            
            if (data.raise_for_status() is None):
                cocktail = self.create_cocktail(data)
                self.cocktails.append(cocktail)

        self.database.fill_db(self.cocktails)

        return self.cocktails

    def dict_to_cocktails(self, cocktails, ingredients):

        for item in cocktails:

            aux_ingredients = {}

            for ingr in ingredients:
                if ingr['idDrink'] == item['idDrink']:
                    aux_ingredients[ ingr["ingredient"] ] = ingr["quantity"]

            cocktail = Cocktail( 
                item['idDrink'],
                item['strDrink'].replace(" ", "_"),
                item['strCategory'].replace(" ", "_"),
                item['strIBA'],
                item['strAlcoholic'].replace(" ", "_"),
                item['strGlass'].replace(" ", "_"),
                "",
                item['strImage'],
                aux_ingredients,
                item['dateModified']
            )

            self.cocktails.append(cocktail)

    def create_cocktail(self, data) -> Cocktail:

        ingr = {}

        for count in range(15):
            if data.json()['drinks'][0]['strIngredient' + str(count + 1)] is not None and data.json()['drinks'][0]['strMeasure' + str(count + 1)] is not None:
                ingr[ data.json()['drinks'][0]['strIngredient' + str(count + 1)].replace(" ", "_") ] = data.json()['drinks'][0]['strMeasure' + str(count + 1)]

        date:datetime.date = None
        if data.json()['drinks'][0]['dateModified'] is not None:
            date = datetime.datetime.strptime(data.json()['drinks'][0]['dateModified'], '%Y-%m-%d %H:%M:%S' )

        cocktail = Cocktail( 
            data.json()['drinks'][0]['idDrink'],
            data.json()['drinks'][0]['strDrink'].replace(" ", "_"),
            data.json()['drinks'][0]['strCategory'].replace(" ", "_"),
            data.json()['drinks'][0]['strIBA'],
            data.json()['drinks'][0]['strAlcoholic'].replace(" ", "_"),
            data.json()['drinks'][0]['strGlass'].replace(" ", "_"),
            data.json()['drinks'][0]['strInstructions'],
            data.json()['drinks'][0]['strDrinkThumb'],
            ingr,
            date)
        return cocktail