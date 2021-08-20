from pydantic import BaseModel, Field
from model.PyObjectId import PyObjectId
from bson import ObjectId


class WorkerDto(BaseModel):
    name: str
    email: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
            }
        }


class WorkerModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    email: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
            }
        }