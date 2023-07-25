#!/usr/bin/env bash
# exit on error
set -o errexit

# キャッシュの削除（WindowsとLinuxで条件分岐）
if [ "$OSTYPE" = "msys" ] || [ "$OSTYPE" = "cygwin" ]; then
    # Windowsの場合
    rmdir /s /q %userprofile%\.cache\matplotlib
else
    # Linux/Unixの場合
    rm -rf ~/.cache/matplotlib/*
fi

# 必要なパッケージのインストール
pip install -r requirements.txt

# 静的ファイルの収集
python manage.py collectstatic --no-input

# データベースのマイグレーション
python manage.py migrate

# スーパーユーザーの作成
python manage.py superuser