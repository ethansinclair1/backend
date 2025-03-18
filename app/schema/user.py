from bson import ObjectId
from pydantic import BaseModel, EmailStr

from app.schema.collection_id.document_id import DocumentId
from app.utils.helpers import partial_model
from beanie import Document, Indexed


class UserBase(BaseModel):
    first_name: str
    last_name: str
    hashed_password: str
    email: EmailStr


class UserCreate(UserBase):
    pass


@partial_model
class UserUpdate(UserBase):
    pass


class User(UserBase, DocumentId):

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }


class UserDocument(User, Document):
    firebase_uid: Indexed(str, unique=True)


    class Settings:
        name = "users"
        bson_encoders = {ObjectId: str}
