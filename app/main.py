from fastapi import FastAPI

from app.api.v1.endpoints import user, expense

app = FastAPI()
app.include_router(user.router)
app.include_router(expense.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}