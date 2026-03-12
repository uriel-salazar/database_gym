from fastapi import FastAPI
import uvicorn

app=FastAPI()
 
@app.get("/")
async def welcome():
    return {"message":"Hello Word"}



if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)