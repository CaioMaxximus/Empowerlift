from fastapi import APIRouter
from src.services import quote_service
import random

router = APIRouter(
    prefix ='/quotes'
)

@router.get("")
async def get_random_quote():
    return  await quote_service.get_random_quote()
    # img_url  = ["https://images.unsplash.com/photo-1636123119035-461a4c1dea2b?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxMDA0NDQ5fDB8MXxzZWFyY2h8Mnx8cGF0dGVybiUyMHNpbGhvdWV0dGUlMjBjbGlmZiUyMG1hY3JvJTIwYmxhY2stYW5kLXdoaXRlfGVufDB8fHx8MTc4NDc0Mzk5MHww&ixlib=rb-4.1.0&q=85",
    #             "https://images.unsplash.com/photo-1776900221978-e7bca110b9ed?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    #             "https://plus.unsplash.com/premium_photo-1784462433921-ee73385b6f91?q=80&w=1067&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"]
    # quote = "Todas estas questões, devidamente ponderadas, levantam dúvidas sobre se a integração das tecnologias emergentes exige a precisão e a definição das dinâmicas sociais em transformação. Vale destacar que a valorização de fatores subjetivos nos obriga à análise das práticas reconhecidas internacionalmente. "
    # img = (random.choice(img_url))
    # print(img)
    # return {"quote" :
    #             {"quote" : quote, "author" : "Maxximus o grande"},
    #         "photo" : {"urls": {"full" : img } }}
