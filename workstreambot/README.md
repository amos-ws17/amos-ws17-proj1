## Rasa NLU and Rasa Core installation using Docker Compose

The docker-compose file launches 2 services:

- The weatherbot

- The sightseeing bot

Run the docker compose file using the following command:
```bash
docker-compose up
```

You can do the rasa nlu tutorial also from outside the container (for Windows docker might not be able to expose the port so you will have to also go inside the container). The rasa core tutorials have to be executed inside the rasa core container using the following command:

```bash
docker exec -ti $CONTAINER_ID$ bash
```
In the future we can use this to train any data set and directly connecting it with our nodejs server.

Note for Windows you can use: https://www.docker.com/products/docker-toolbox
