
import Constants
from Cocktails import Cocktail
from pip._vendor import requests

class Extract:

    def extract_data(self):

        print("Data extraction function")

        self.cocktails=[]

        for _ in range(Constants.NUM_COCKTAILS):

            data = requests.get(url=Constants.API_URL)

            # print(data.json().keys()) # ['drinks']
            # print( type(data.json()['drinks']) ) # list
            # print( type(data.json()['drinks'][0]) ) # dict
            # print( data.json()['drinks'][0].keys() ) # actual keys
            
            # ['idDrink', 'strDrink', 'strDrinkAlternate', 'strTags', 'strVideo', 'strCategory', 
            # 'strIBA', 'strAlcoholic', 'strGlass', 'strInstructions', 'strInstructionsES', 
            # 'strInstructionsDE', 'strInstructionsFR', 'strInstructionsIT', 'strInstructionsZH-HANS', 
            # 'strInstructionsZH-HANT', 'strDrinkThumb', 'strIngredient1', 'strIngredient2', 
            # 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 
            # 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 
            # 'strIngredient13', 'strIngredient14', 'strIngredient15', 'strMeasure1', 'strMeasure2', 
            # 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 
            # 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 
            # 'strMeasure15', 'strImageSource', 'strImageAttribution', 'strCreativeCommonsConfirmed', 'dateModified']

            if (data.raise_for_status() is None):
                print("Obtained data")
                cocktail = self.create_cocktail(data)
                self.cocktails.append(cocktail)

        return self.cocktails

    def create_cocktail(self, data) -> Cocktail:
        cocktail = Cocktail( data.json()['drinks'][0]['strDrink'] )
        return cocktail
