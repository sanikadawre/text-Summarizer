# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware

from summarizer import getSummary  


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)



class Item(BaseModel):
    text_string : str


@app.post("/summarize/")
async def create_item(item: Item):
    try:
        return {"summary": getSummary(item.text_string)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the summarization API. Use the /summarize/ endpoint to summarize text."}

