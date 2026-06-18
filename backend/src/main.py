from fastapi import FastAPI
from .repositories.quotes_repository import QuotesReposoitory
from .routers.quotes import router as quotes_router
from pathlib import Path    
from fastapi.middleware.cors import CORSMiddleware




ACTUAL_PATH = Path(__file__).resolve()

QUOTES_PATH = ACTUAL_PATH.parent.parent
QUOTES_PATH = QUOTES_PATH  / "quotes.csv"
print("========",flush=True)
print(QUOTES_PATH,flush=True)


QuotesReposoitory.init_quotes(QUOTES_PATH)
api = FastAPI()
api.include_router(quotes_router)

origins = [
    "http://localhost:3000",    #React (Create React App)
    "http://localhost:5173",   
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,          
    allow_methods=["*"],             
    allow_headers=["*"],            
)