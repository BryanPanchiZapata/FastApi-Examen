from pydantic import BaseModel, Field
from model.PyObjectId import PyObjectId
from bson import ObjectId
from model.worker_model import WorkerDto, WorkerModel
from typing import List

class ActivityModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    description: str = Field(...)
    workers: List[WorkerModel] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Seguridad informatica",
                "description": "La seguridad informática, también conocida como ciberseguridad o seguridad de tecnología de la información",
                "workers": [
                    {
                        "name": "Jane Doe",
                        "email": "jdoe@example.com",
                    }
                ]
            }
        }