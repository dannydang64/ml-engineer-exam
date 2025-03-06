from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is working!"}
