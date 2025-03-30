import os

import dotenv
import pytest

from helius import HeliusAPI


@pytest.fixture
def HeliusInterface():
    dotenv.load_dotenv()

    API_KEY = os.getenv("API_KEY")

    return HeliusAPI(api_key=API_KEY)
