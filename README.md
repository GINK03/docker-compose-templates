# dockerをdocker hubから引き出す

## minimal-machine-learning-oppai
```console
$ docker-compose build
...
$ docker-compose up
```

## メンテナンスをするには、コマンドで立ち上げて行う
```console
docker run -p 1022:22 -it nardtree/oppai server.py
docker run -it nardtree/oppai server.py
```

## docker hubにpushする
```console
docker push nardtree/oppai:latest
```


## 　注：Ubuntu 18.04とDockerではloginできない問題がある
 - [ここ](https://github.com/docker/cli/issues/1136#issuecomment-399537945)のバイナリを潰すと動く
 
## デーモン化
dockerが仮に自動起動するデーモンだととってもメリットがあるが、Ubuntu 18.04でこのような方法で動かすことができた。

まず、init.rcを作成して実行権限とシーバンを与える。  

```console
$ printf '%s\n' '#!/bin/bash' 'exit 0' | sudo tee -a /etc/rc.local
$ sudo chmod +x /etc/rc.local
$ sudo reboot
```

init.rcに作成したdocker-compose.ymlをしていしてupするスクリプトを書く  
```
docker-compose -f /home/anasys/opf-ai-ymbg-secession-prediction/system/docker-compose.yml up
```

なお、docker-compose.ymlの内容は
```
version: '3'
services:
  secession-prediction:
    build: .
# 必要に応じて  restart: alwaysをつける
```
これでちゃんと動く（すごーい）

