# Docker+Flask+MySQLでRESTfulAPI

## 主な操作
dockerはインストールしておく
### コンテナビルド
```sh
$ docker-compose build
```

### コンテナ起動
`-d`オプションを付与するとバックグラウンドでコンテナが起動する
```sh
$ docker-compose up -d
```

### apiコンテナに入る
```sh
$ docker-compose exec python sh
```

### dbコンテナに入る
```sh
$ docker-compose exec db sh
```

### mysqlに接続
パスワードは`mysql`
```mysql
mysql> mysql -u root -p
```

### Flaskのマイグレーション
```flask
# flask db init
# flask db migrate
# flask db upgrade
```