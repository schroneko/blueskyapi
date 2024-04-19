# Bluesky API を用いて投稿

## 環境構築

```
git clone git@github.com:schroneko/blueskyapi.git
cd blueskyapi
touch .env
```

`.env` に下記を記載。

```
BSKY_USERNAME=your_username
BSKY_PASSWORD=your_password
```

```
rye sync
rye run python post2bsky.py
```
