from crypt import methods

from flask import Blueprint, jsonify, abort

from app.models.user import UserModel
from app.schema import user as user_schema

router = Blueprint("users", __name__, url_prefix="/users")
user_model = UserModel()

@router.route("/<string:user_id>", methods=["GET"])
async def get_user(user_id: str):
    user = await user_model.get(user_id)
    if not user:
        abort(400, description="User not found")
    return jsonify(user_schema.User(**user.model_dump())), 200

