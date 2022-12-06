
from typing import List, Dict
from Cocktails import Cocktail


class Transform:

    def __init__(self, cocktails) -> None:
        self.cocktails: List[Cocktail] = cocktails

    def filter_by_structure(self, element_list: List[str]) -> Dict[str, int]:
        data: Dict[str, int] = {}

        for element in element_list:
            if element in data:
                data[element] += 1
            else:
                data[element] = 1

        return data

    # Group by "strCategory"
    def filter_by_category(self) -> Dict[str, int]:

        categories: List[str] = []
        for cocktail in self.cocktails:
            categories.append(cocktail.strCategory)

        return self.filter_by_structure(categories)

    # Group by strAlcoholic
    def filter_by_alcoholic(self) -> Dict[str, int]:

        alcoholic: List[str] = []
        for cocktail in self.cocktails:
            alcoholic.append(cocktail.strAlcoholic)

        return self.filter_by_structure(alcoholic)

    # Group by strGlass
    def filter_by_glass(self) -> Dict[str, int]:

        glass: List[str] = []
        for cocktail in self.cocktails:
            glass.append(cocktail.strGlass)

        return self.filter_by_structure(glass)

    # How many drinks require each ingredient
    def filter_by_ingredients(self) -> Dict[str, int]:

        ingredients: List[str] = []
        for cocktail in self.cocktails:
            keysList:str = [key for key in cocktail.ingredients]
            ingredients = ingredients + keysList

        return self.filter_by_structure(ingredients)
