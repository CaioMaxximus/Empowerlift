from src.repositories.quotes_repository import QuotesReposoitory
import pytest


def test_repository_raises_an_exception_if_the_data_frame_is_not_initialized():

   with pytest.raises(ValueError):
      QuotesReposoitory.get_ramdom_quote()
