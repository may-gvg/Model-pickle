from flask import Flask, request
from flask_restx import Resource, Api

from ml_load import model1

app = Flask(__name__)
api = Api(app)

@api.route("/models/<string:model_id>")
class ModelAPI(Resource):

    def get(self, model_id):
        result = 0
        if int(model_id) == 1:
            result = model1()
            return {model_id: result}
        return {"error": "Model not found"}



if __name__ == "__main__":
    app.run(debug=False)
