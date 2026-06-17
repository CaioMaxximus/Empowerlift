from fastapi import FastAPI
from repositories.quotes_repository import QuotesReposoitory
from routers.quotes import router as quotes_router

QuotesReposoitory.init_quotes("")
api = FastAPI()
api.include(quotes_router)



# @api.get('/')
# async def index():
#     return {"message" : "Salut!!"}


# @api.get('/user/{user_name}')
# async def get_user(user_name : str):
#     return {"message": f"vc escolheu o user {user_name}"}

