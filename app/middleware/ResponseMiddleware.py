from flask import jsonify, Response


def after_request(response: Response):
    response_json = response.get_json(silent=True) or {}

    response_data = {
        "status": response.status_code,
        "success": response.status_code < 400,
        "message": response_json.pop("message", None) if response.status_code < 400 else None,
        "data": response_json.pop("data", None) if response.status_code < 400 else None,
        "error": {
            "code": response.status_code,
            "message": response_json.pop("message", response.get_data(as_text=True))
        } if response.status_code >= 400 else None,
        "meta": response_json.pop("meta", {})
    }

    # Remove None values from response_data
    response_data = {key: value for key, value in response_data.items() if value is not None}

    response.set_data(jsonify(response_data).get_data())
    response.mimetype = "application/json"
    return response
