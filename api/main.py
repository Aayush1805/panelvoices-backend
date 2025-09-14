from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import voice
# from mangum import Mangum



app = FastAPI(
    title="Voice API",
    description="API to fetch audio files based on language",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(voice.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Voice API"}


# handler = Mangum(app)