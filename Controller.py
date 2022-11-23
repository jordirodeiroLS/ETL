
from Extract import Extract
from Cocktails import Cocktail
from typing import List

class Controller:

    def __init__(self) -> None:
        self.extract = Extract()
        self.cocktails: List[Cocktail]

    def execute(self):
        print("This is the main function.")

        self.cocktails = self.extract.extract_data()
        print(self.cocktails[0].strDrink)


ETL = Controller()
ETL.execute()