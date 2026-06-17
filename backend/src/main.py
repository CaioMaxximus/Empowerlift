from fastapi import FastAPI
from .repositories.quotes_repository import QuotesReposoitory
from .routers.quotes import router as quotes_router
from pathlib import Path    

ACTUAL_PATH = Path(__file__).resolve()

QUOTES_PATH = ACTUAL_PATH.parent.parent
QUOTES_PATH = QUOTES_PATH  / "quotes.csv"
print("========",flush=True)
print(QUOTES_PATH,flush=True)


QuotesReposoitory.init_quotes(QUOTES_PATH)
api = FastAPI()
api.include_router(quotes_router)


"/home/caiomaxx/Documentos/projetos/empowerlift/backend/quotes.csv"
# @api.get('/')
# async def index():
#     return {"message" : "Salut!!"}


# @api.get('/user/{user_name}')
# async def get_user(user_name : str):
#     return {"message": f"vc escolheu o user {user_name}"}

