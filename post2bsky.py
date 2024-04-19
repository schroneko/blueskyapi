import os
from atproto import Client

from dotenv import load_dotenv

load_dotenv()


def get_client(base_url, username, password):
    client = Client(base_url=base_url)
    try:
        client.login(login=username, password=password)
    except Exception as e:
        print(f"ログインに失敗しました: {e}")
        return None
    return client


def send_post(client, text):
    if client is not None:
        try:
            client.send_post(text=text)
            print("投稿が成功しました。")
        except Exception as e:
            print(f"投稿に失敗しました: {e}")
    else:
        print("クライアントが初期化されていません。")


if __name__ == "__main__":
    USERNAME = os.getenv("BSKY_USERNAME")
    PASSWORD = os.getenv("BSKY_PASSWORD")
    BASE_URL = "https://bsky.social"

    if USERNAME is None or PASSWORD is None:
        print("ユーザー名またはパスワードが設定されていません。")
    else:
        client = get_client(BASE_URL, USERNAME, PASSWORD)
        send_post(client, "Hello from API")
