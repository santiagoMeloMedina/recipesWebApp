from typing import Any, Dict
import json
from flask import jsonify


def get_custom_response(code: int, body: Dict[str, Any]):
    return jsonify({"message": body}), code
