## Rasa NLU and Rasa Core installation using Docker Compose

The docker-compose file launches 2 services:

- The weatherbot

- The sightseeing bot

Run the docker compose file using the following command:
```bash
docker-compose up
```
The weather bot exposes a REST API at port **5012**, example:

```bash
curl -X POST http://localhost:5012/bot/default/execute?query=hey
```

The sightseeing bot exposes a REST API at port **5022**, example:

```bash
curl -X POST http://localhost:5022/bot/default/execute?query=hey
```

Note for Windows you can use: https://www.docker.com/products/docker-toolbox
