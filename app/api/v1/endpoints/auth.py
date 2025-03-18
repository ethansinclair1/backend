from flask import Blueprint

router = Blueprint("auth", __name__, url_prefix="/auth")


@router.route("/login")
async def log_in():
    pass

@router.route("/sign-up")
async def sign_up():
    pass
