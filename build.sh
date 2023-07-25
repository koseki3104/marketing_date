#!/usr/bin/env bash
# exit on error
set -o errexit

# キャッシュの削除
rmdir /s /q %userprofile%\.cache\matplotlib

# 必要なパッケージのインストール
pip install -r requirements.txt

# 静的ファイルの収集
python manage.py collectstatic --no-input

# データベースのマイグレーション
python manage.py migrate

# スーパーユーザーの作成
python manage.py superuser