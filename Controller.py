
from Extract import Extract
from Transform import Transform
from Load import Load
from Show import Show

from Cocktails import Cocktail
from typing import List

class Controller:

    cocktails: List[Cocktail]

    def _extract(self) -> None:
        self.extract = Extract()

        self.cocktails = self.extract.extract_data()
        print(self.cocktails[0].strDrink)

    def _transform(self) -> None:        
        self.transform = Transform( self.cocktails )

        self.category = self.transform.filter_by_category()
        print(self.category)

        self.alcoholic = self.transform.filter_by_alcoholic()
        print(self.alcoholic)

        self.glass = self.transform.filter_by_glass()
        print(self.glass)

        self.ingredients = self.transform.filter_by_ingredients()
        print(self.ingredients)

    def _load(self) -> None:
        self.load = Load()

        self.load.load_to_csv(self.category, ["Category", "Amount of Cocktails"], 'cocktails_by_category.csv')

        self.load.load_to_csv(self.alcoholic, ["Alcoholic", "Amount of Cocktails"], 'cocktails_by_alcoholic.csv')

        self.load.load_to_csv(self.glass, ["Glass", "Amount of Cocktails"], 'cocktails_by_type_of_glass.csv')

        self.load.load_to_csv(self.ingredients, ["Ingredients", "Amount of Cocktails"], 'cocktails_by_ingredient.csv')

    def _create_visuals(self):

        self.show = Show()

        self.show.histogram(self.category, "Cocktails by category", "Category", "Amount of cocktails")

        self.show.histogram(self.alcoholic, "Cocktails by alcoholic", "Alcoholic", "Amount of cocktails")

        self.show.histogram(self.glass, "Cocktails by glass", "Glass", "Amount of cocktails")

        self.show.histogram(self.ingredients, "Cocktails by ingredient", "Ingredients", "Amount of cocktails")

        pass

    def execute(self):
        print("This is the main function.")

        self._extract()

        if self.cocktails is None:
            print("ERORR: No data available from the API. Please try again.")
            return

        self._transform()

        self._load()

        self._create_visuals()

ETL = Controller()
ETL.execute()