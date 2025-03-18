from flask import Blueprint

router = Blueprint("users", __name__, url_prefix="/users")


@router.route("/<string:user_id>", methods=["GET"])
async def get_user(user_id: str):
    pass
