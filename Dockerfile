# ベースイメージの指定
FROM python:3.10-slim

# 作業ディレクトリの指定
WORKDIR /app

# ソースコードのコピー
COPY . .

# 必要な依存関係のインストール（例：pipのアップグレード）
RUN pip install --upgrade pip
RUN pip install pytest
