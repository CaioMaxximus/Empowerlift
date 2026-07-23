from src.repositories.quotes_repository import QuotesReposoitory
import random
import os
import httpx
from fastapi import HTTPException
from src.core.config import settings

UNSPLASH_ACCESS_KEY = settings.api_key

quotes_repo = QuotesReposoitory

# print(UNSPLASH_ACCESS_KEY)

def init_quotes_repository():
    quotes_repo.init_quotes()

async def get_random_quote():
    
    quote = quotes_repo.get_ramdom_quote()
    choose_photo = await get_a_photo_by_tags(quote["tags_photos"].split(","))
    return {"quote" : quote , "photo" : choose_photo[0]}

async def get_a_photo_by_tags(tags):
    choose_tags = random.sample(tags , min(5, len(tags)))
    # print(choose_tags)
    photos = await search_photos(" ".join(choose_tags))
    # print(photos)
    choose_photo = random.sample(photos,1)
    return choose_photo





async def search_photos(tags: str = "nature"):
    url = "https://api.unsplash.com/search/photos"
    
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": tags
        # ,"per_page": 10
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            
            response.raise_for_status()
            
            dados = response.json()
            return dados["results"]
            
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"Erro na API externa: {exc.response.text}"
            )
        except httpx.RequestError as exc:
            raise HTTPException(
                status_code=503,
                detail=f"Falha na conexão com o Unsplash: {str(exc)}"
            )