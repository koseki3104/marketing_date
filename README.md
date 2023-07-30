# アプリケーション名
MARKETING_DATA_ANALYTICS
 
# アプリケーション概要
飲食店でのアンケート調査のデータ解析ができるアプリケーションを作成しました。

# URL
「https://marketing-date-production.onrender.com」

# テスト用アカウント
・Basic認証パスワード：admin 
 
・Basic認証ID：2222 

・スーパーユーザー名：admin

・スーパーユーザーパスワード：password

# 利用方法
### アンケート回答
1.トップページからアンケート回答欄に回答を入力します。
2.全て入力できたら「回答」ボタンをクリックします。

### データ解析
1.「https://marketing-date-production.onrender.com/admin」にアクセスします。
2.スーパーユーザーとしてユーザー名、パスワードを入力して、ログインしてデータベースにアクセスします。
3.Reviewsをクリックし、データの内容を閲覧できます。
4.「https://marketing-date-production.onrender.com/admin」にアクセスします。
5.データ解析がされた、エクセルシートがダウンロードされます。

# アプリケーションを作成した背景
将来的には、人工知能やデータ解析を行う案件に携わりたいと考えているので、データ解析を行うアプリケーションを作成しました。
飲食店でのアンケートから得られたデータの解析を行い、集客や店舗運営の改善などのマーケティング的知見を得ることができます。また、データ解析の結果を瞬時に把握することで飲食店の人手不足という課題解決にもつながるのではないかと考えました。

# 洗い出した要件
「https://docs.google.com/spreadsheets/d/16zZ2HQu3WwCfQr7--Ev4fUUuqq0AuFfd63HK5G3_DGE/edit#gid=982722306」

# 実装予定の機能
・相関行列の表をデータの数値によってセルの色を変更する
・デモグラフィック分析の表をデータの数値によってセルの色を変更する
・クロス集計表分析、カイ二乗検定を表としてエクセルに出力（顧客と注文メニューの傾向を把握する為）

# データベース設計
「https://gyazo.com/2d5fd662b9db81a241fef989318f2004」

# 画面遷移図
「https://gyazo.com/5de75e5896059ecd877970b29861c122」

# 開発環境
Python

Django

GitHub

Render

Visual Studio Code

Excel

# ローカルでの動作方法
% git clone https://github.com/koseki3104/marketing_date

%cd marketing_date

%pip install virtualenv

%myenv\Scripts\activate

%python manage.py runserver

# 工夫したポイント
統計学に詳しくない人でも、簡単に分かりやすいデータを取得できるように工夫を行いました。
図や表を用いたり、数値によって色を変えることでデータを可視化しデータを誰でもわかるように出力しました。
特定のURLにアクセスし、ユーザー名とパスワードを入力するだけで簡単にデータ解析が行われるようにしました。