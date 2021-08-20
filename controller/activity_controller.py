from fastapi import APIRouter
from model.activity_model import ActivityModel
from config import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

worker_activity_route = APIRouter(
    prefix="/activity",
    tags=["activity"]
)


@worker_activity_route.post("", response_description="Add new worker activity", response_model=ActivityModel)
async def create_worker_activity(activity: ActivityModel):
    activity_model = jsonable_encoder(activity)
    new_activity = await db["Api_Examen"].insert_one(activity_model)
    return_activity = await db["Api_Examen"].find_one({"_id": new_activity.inserted_id})
    return JSONResponse(content=return_activity)


@worker_activity_route.get("", response_description="return", response_model=List[ActivityModel])
async def get_worker_activity():
    activity = await db["Api_Examen"].find().to_list(15)
    return activity