from fastapi import FastAPI
import uvicorn

app=FastAPI()
 
@app.get("/")
async def welcome():
    return {"message":"Hello Word"}

@app.post("/create")
async def create_user():
    pass



if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)