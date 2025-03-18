from flask import Blueprint
from app.api.v1.endpoints.users import router as users_router
from app.api.v1.endpoints.auth import router as auth_router

router = Blueprint("v1", __name__, url_prefix="/api/v1")

router.register_blueprint(users_router)
router.register_blueprint(auth_router)