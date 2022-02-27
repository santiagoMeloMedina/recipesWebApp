from flask import Flask, request
from models import response
import logging
from services import recipes as recipes_service
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    return response.get_custom_response(**{"code": 204, "body": {}})


@app.route("/recipes", methods=["GET"])
def get_paged_recipes():
    result = {"code": 500, "body": {}}
    try:
        pager_params = (request.args.get("starting", 0), request.args.get("limit", 0))
        title = request.args.get("name", None)
        result.update(
            {
                "code": 200,
                "body": recipes_service.get_paged_recipes(
                    pager_params, title=title.lower()
                ),
            }
        )
    except Exception as e:
        logging.error(e)
    return response.get_custom_response(**result)


@app.route("/recipes/<ingredient>", methods=["GET"])
def get_paged_recipes_by_ingredient(ingredient: str):
    result = {"code": 500, "body": {}}
    try:
        pager_params = (request.args.get("starting", 0), request.args.get("limit", 0))
        result.update(
            {
                "code": 200,
                "body": recipes_service.get_paged_recipes(
                    pager_params, ingredient=ingredient
                ),
            }
        )
    except Exception as e:
        logging.error(e)
    return response.get_custom_response(**result)


if __name__ == "__main__":
    app.run(debug=int(sys.argv[3]), host=sys.argv[1], port=int(sys.argv[2]))
