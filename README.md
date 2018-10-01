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


##　注：Ubuntu 18.04とDockerではloginできない問題がある
 - [ここ](https://github.com/docker/cli/issues/1136#issuecomment-399537945)のバイナリを潰すと動く
