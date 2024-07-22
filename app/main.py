from fastapi import FastAPI
from app.api.internal_router import internal_router
app = FastAPI()

app.include_router(internal_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
