from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hi, I am Shop-Genius an AI-powered retail assistant designed to provide a seamless shopping experience for users on Amazon."}