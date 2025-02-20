jalan kan menggunakan docker
build docker image terlebih dahulu docker build -t trading-bot .
Jalan container docker run -d --name my_trading_bot trading-bot
lihat logs yang eror docker logs -f my_trading_bot
