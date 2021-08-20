from fastapi import APIRouter
from model.worker_model import WorkerDto, WorkerModel
from config import db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

worker_route = APIRouter(
    prefix="/worker",
    tags=["worker"]
)

@worker_route.get("/", response_description="list of 15 worker", response_model=List[WorkerModel])
async def list_workers():
    workes = await db["examen"].find().to_list(15)
    return workes



@worker_route.post("/", response_description="Add new Worker", response_model=WorkerModel)
async def create_worker(worker: WorkerDto):
    worker_model = WorkerModel(name=worker.name, email=worker.email)
    worker_json = jsonable_encoder(worker_model)
    new_worker = await db["examen"].insert_one(worker_json)
    insert_worker = await db["examen"].find_one({"_id": new_worker.inserted_id})
    return JSONResponse(content=insert_worker)


