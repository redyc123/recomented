# recomented

build
```
docker build . -t recomented
```

run
```
docker run --env-file .env-local -p 8080:80 -t recomented
```