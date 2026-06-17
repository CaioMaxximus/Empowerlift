
import pandas as pd
## Depois gerar um contrato para essa classe nao ser inicializada com mais de uma instancia

class QuotesReposoitory():

    quotes = None

    @classmethod
    def verify_quotes_state(func):
        def wrapper(*args, **kwargs):
            if not args[0].quotes:
                raise ValueError("You need to inialize the quotes dataframe first!")
            return func(*args,**kwargs)
        return wrapper()


    @verify_quotes_state
    @classmethod
    def get_ramdom_quote(cls):

        return cls.quotes.sample(n = 1).to_dict()

    @classmethod
    def init_quotes(cls, path):
        if cls.quotes:
            raise ValueError("Quotes already loaded in memory")
        cls.quotes = pd.open_csv(path)

