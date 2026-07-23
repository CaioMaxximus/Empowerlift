
import pandas as pd
## Depois gerar um contrato para essa classe nao ser inicializada com mais de uma instancia

class QuotesReposoitory():

    quotes = None

    def verify_quotes_state(func):
        def wrapper(*args, **kwargs):
            if not args[0].quotes:
                raise ValueError("You need to inialize the quotes dataframe first!")
            return func(*args,**kwargs)
        return wrapper

    @classmethod
    # @verify_quotes_state
    def get_ramdom_quote(cls):

        return cls.quotes.sample(n = 1).to_dict(orient='records')[0]

    @classmethod
    def init_quotes(cls, path):
        if cls.quotes:
            raise ValueError("Quotes already loaded in memory")
        cls.quotes = pd.read_csv(path)


# if __name__ == "__main__":
#     QuotesReposoitory.init_quotes("/home/caiomaxx/Documentos/projetos/empowerlift/backend/quotes.csv")
#     print(QuotesReposoitory.quotes.head(10))    
