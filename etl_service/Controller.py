
from Extract import Extract
from Transform import Transform
from Load import Load
from Show import Show

from Cocktails import Cocktail
from typing import List

# Import framework
from flask import Flask
from flask import send_file
from flask_restful import Resource, Api

import mimetypes

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class Controller(Resource):

    cocktails: List[Cocktail]

    def _extract(self) -> None:
        self.extract = Extract()

        self.cocktails = self.extract.extract_data()

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

        self.load.load_to_csv(self.category, ["Category", "Amount_of_Cocktails"], 'cocktails_by_category.csv')

        self.load.load_to_csv(self.alcoholic, ["Alcoholic", "Amount_of_Cocktails"], 'cocktails_by_alcoholic.csv')

        self.load.load_to_csv(self.glass, ["Glass", "Amount_of_Cocktails"], 'cocktails_by_glass.csv')

        self.load.load_to_csv(self.ingredients, ["Ingredients", "Amount_of_Cocktails"], 'cocktails_by_ingredient.csv')

        self.load.create_csv("complete_info.csv")
        self.load.append_to_csv(self.category, ["Category&", "Amount_of_Cocktails"], 'complete_info.csv', 'w')
        self.load.append_to_csv(self.alcoholic, ["Alcoholic&", "Amount_of_Cocktails"], 'complete_info.csv', 'a')
        self.load.append_to_csv(self.glass, ["Glass&", "Amount_of_Cocktails"], 'complete_info.csv', 'a')
        self.load.append_to_csv(self.ingredients, ["Ingredients&", "Amount_of_Cocktails"], 'complete_info.csv', 'a')

    def _create_visuals(self):

        self.show = Show()

        self.show.histogram(self.category, "Cocktails_by_category", "Category", "Amount_of_cocktails")

        self.show.histogram(self.alcoholic, "Cocktails_by_alcoholic", "Alcoholic", "Amount_of_cocktails")

        self.show.histogram(self.glass, "Cocktails_by_glass", "Glass", "Amount_of_cocktails")

        self.show.histogram(self.ingredients, "Cocktails_by_ingredient", "Ingredients", "Amount_of_cocktails")

        pass

    def get(self):
        print("This is the main function.")

        self._extract()

        if self.cocktails is None:
            print("ERORR: No data available from the API. Please try again.")
            return

        self._transform()

        self._load()

        self._create_visuals()

        filename = "data/complete_info.csv"
        mime = mimetypes.MimeTypes().guess_type(filename)[0]
        print(mime)
        return send_file(filename, mimetype = mime)


# Create routes
api.add_resource(Controller, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)