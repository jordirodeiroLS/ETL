
from Extract import Extract
from Transform import Transform

from Cocktails import Cocktail
from typing import List

class Controller:

    cocktails: List[Cocktail]

    def _extract(self):
        self.extract = Extract()

        self.cocktails = self.extract.extract_data()
        print(self.cocktails[0].strDrink)

    def _transform(self):        
        self.transform = Transform( self.cocktails )

        self.category = self.transform.filter_by_category()
        print(self.category)

        self.alcoholic = self.transform.filter_by_alcoholic()
        print(self.alcoholic)

        self.glass = self.transform.filter_by_glass()
        print(self.glass)

        self.ingredients = self.transform.filter_by_ingredients()
        print(self.ingredients)


    def execute(self):
        print("This is the main function.")

        self._extract()

        if self.cocktails is None:
            print("ERORR: No data available from the API. Please try again.")
            return

        self._transform()


ETL = Controller()
ETL.execute()