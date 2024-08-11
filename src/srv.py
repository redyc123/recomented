from langserve import add_routes
from fastapi import FastAPI
from logic.logic import logic
from langchain.schema.runnable import RunnableLambda
import uvicorn

app = FastAPI(title="Recomented System")

add_routes(
    app,
    RunnableLambda(logic.run),
    path="/logic/run",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
