from fastapi import FastAPI
import uvicorn
from fastapi.openapi.utils import get_openapi
from controller.worker_controller import worker_route
from controller.activity_controller import worker_activity_route

app = FastAPI(name="example")
app.include_router(worker_route)
app.include_router(worker_activity_route)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Examen",
        version="0.0.1",
        description="FastAPI",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80, access_log=True)