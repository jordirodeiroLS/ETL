
#@app.route('/get_image')
#def get_image():
#    if request.args.get('type') == '1':
#       filename = 'ok.gif'
#    else:
#       filename = 'error.gif'
#    return send_file(filename, mimetype='image/gif')

    # Observatory Service

# Import framework
from flask import Flask
from flask import send_file
from flask_restful import Resource, Api
from Controller import Controller

import mimetypes

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Observatory(Resource):
    def get(self):

        self.controller = Controller()
        self.controller.execute()

        #filename = "data/Cocktails_by_ingredient.png"
        filename = "data/complete_info.csv"

        # For MIME types
        mime = mimetypes.MimeTypes().guess_type(filename)[0]
        print(mime)
        return send_file(filename, mimetype = mime)


# Create routes
api.add_resource(Observatory, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)