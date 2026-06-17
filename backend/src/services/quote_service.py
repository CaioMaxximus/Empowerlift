from repositories.quotes_repository import QuotesReposoitory



quotes_repo = QuotesReposoitory


def init_quotes_repository():
    quotes_repo.init_quotes()

def get_random_quote():
    return quotes_repo.get_ramdom_quote()