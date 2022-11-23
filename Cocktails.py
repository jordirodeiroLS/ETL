
from dataclasses import dataclass
from typing import Dict
import datetime

@dataclass
class Cocktail:
    idDrink:  int
    strDrink: str
    strCategory: str
    strIBA: str
    strAlcoholic: str
    strGlass: str
    strInstructions: str
    strImage: str
    ingredients: Dict[ str, str ]
    dateModified: datetime.date



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