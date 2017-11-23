## Rasa NLU and Rasa Core installation using Docker Compose

The docker-compose file launches 2 services:

- the rasa nlu server reachable at port 5000 (also outside of the containers)

- the a docker container with installed rasa core which launches the rasa core server by training the simple bot. It can also launch another example, but you have to change the data folder in the Dockerfile by editing the name of the DATA_SRC environment variable

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
