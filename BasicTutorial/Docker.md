## Add Group and setup user

sudo groupadd docker
sudo usermod -aG docker ${USER}

====

## Basic Commands

docker pull redis

docker run redis
docker run redis:4.10     						# Specific versions can de downloaded with :
docker run --name some_name redis:4.10 			# Specify name of the container (Optional)

docker run -d redis

docker ps
docker ps -a  									# List Running and Stopped containers

docker stop <container id>
docker start <container id>    					# Restart the container

docker rm <container id>

docker images									# Shows all the images
docker rmi <image name and tag>					# Detele an image

===

## Container Port Binding

docker run  -p 6000:6397 -d redis 		# first port is the host machine port, second one is container port
œ
===

## Logs from the container

docker logs <container id or name>

===

## Get a terminal inside a container

docker exec -it <container id> /bin/bash 	## -it stands for intercative terminal

===

## (Important) Difference between docker run and docker start

	- run command works with images and creates containers out of it
	- start only works with containers

The great thing about start is say I first run the following:

docker run -p6000:6397 --name redis_test -d redis

The I stop the container

docker stop redis_test

**When I restart it back with docker start, the port binding and detached mode autometically is activated**

docker start redis_test

===

## Docker Network

docker network ls
docker network create my_redis_network

docker run -d -p6000:6397 --name redis_test --network my_redis_network 

If multiple containers are running in the same docker network then they can connect with each other using the container name and the port. Probably this is the container port (not the port mapped to the host machine : This I have not tested, just a guess)

===

## Add env variables in the container

Typically DockerHub pages contain the way. Typically It needs to be done using a -e flag. Example:

docker run -d \
	-p 6000:6397 \
	-e ADMIN=admin \
	-e PASSWORD=pass \
	--network my_redis_network \
	--name redis_test \
	redis

===

## Attaching volume for data persistence

3 types

	- Map an existing folder from the host OS to a folder in the container
	- Crete a new location in the host OS (annynymous volume created inside /ver/lib/docker/volumes)
	- Same as above but provide name / location (named volume)

docker run -v <host location>:<container location>
docker run -v <container location>
docker run -v some_name:<container location>

In Docker-compose use "volumes" attribute

===

### Questions

	- Difference between CMD and ENTRYPOINT in dockerfile
	- While using docker-compose yaml file, how does the my app refer to a db ? Since in the same network no need to provide hostname but should I give the container name as the hostname ? will it work ? 


### Links:

	- https://www.youtube.com/watch?v=3c-iBn73dDE&ab_channel=TechWorldwithNana
	- https://spacelift.io/blog/docker-entrypoint-vs-cmd








