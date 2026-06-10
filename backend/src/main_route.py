from fastapi import FastAPI

api = FastAPI()


@api.get('/')
def index():
    return {"message" : "Salut!!"}


@api.get('/user/{user_name}')
async def get_user(user_name : str):
    return {"message": f"vc escolheu o user {user_name}"}