
from bot import start_polling
from config import bot_token, api_client_url


def start():
    start_polling(bot_token, api_client_url)


if __name__ == "__main__":
    start()
