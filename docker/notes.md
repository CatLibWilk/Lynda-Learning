# Docker

- Docker is not virtual machine, there's only one operating system involved, rather is a self-contained, sealed unit of software.
    - contains all the operating system code, configs, networking, depednencies, and processes to run the code
- takes all the services that make up a linux server, and copies that to linux kernal for each container

- Docker is a client progam (ie. the cli tool when you type `docker`) and a server program managing a linux system 

## Linux Install of Docker
- when installing docker-ce, remove old versions of docker with `apt-get remove docker docker-engine docker.io`
- update apt-get then:
    - install apt-transport-https, ca-certificates, curl, software-dependencies-common
    - get docker gpg key `curl -fsSL https://download.docker.com/index/ubuntu/gpg | sudo apt-key add`
    - add the docker repository with `apt-add-repository` (see docker.com linux install guides, get repo for x86 arch.)
    - `apt-get update`
    - `apt-get install docker-ce`
- setup to run as non-root
    - `sudo groupadd docker`
    - `sudo usermod -aG docker $USER`
    - log out/in to update changes

## Chpt.2 Using Docker
- The Docker Flow: Images to Containers
    1. Image: every file that makes up enough of the os to do what is required
        - see docker images with `docker images`
    2. Container:
        - `docker run` takes an image and transforms it into a running container with a living process
        - `docker run -ti` makes terminal interactive
        - an image and its running container will NOT have the same ID
        - changes made in a running container are NOT reflected in the image.  The image stays the same always.
- Containers to Images
    - `docker ps -l` will show last container exited 
    - can use `docker commit` to create a new image based on changes made to a container.
        - eg. `docker commit [name of changed container] [new name for image]`

- Running things in Docker
    - basic command is `docker run`
        - `docker run --rm` will run and the rm will delete the container when exited from
    - can use `-c` to pass commands to started container eg.
        - `docker run -ti ubuntu bash -c "sleep 5; echo all done"`
    - `-d` runs container as `detached`, ie. leaves it running in background
        - `docker run -d -ti ubuntu bash -c "sleep 5"` 
    - `docker attach` jumps into a running container
    - `docker exec` starts another process in a running container (ie. attach a/another terminal to the container)
- Managing Containers
    - docker logs kept for as long as container exists
        - check with `docker logs [container]` 
    - stopping and removing containers
        - `docker kill [container]` to stop a container
        - `docker rm [container]` to remove container 
    - resource constraints
        - can set container to run to fixed amount of memory
            - eg. `docker run --memory maximum-allowed-memory [image-name] [command]`
        - limit cpu
    - Best Practices
        - dont let containers fetch dependencies when they start 
        - dont leave important things in an unnamed stopped container 

- Container Networking
    - you can group containers into "private" networks 
    - you can also expose ports to allow for connections
    - exposing ports
        - use `-p` to "publish" and give the container and host ports
            - eg. `docker run -ti -p 8080:8080 ubuntu bash`
        - you can expose ports dynamically as well, ie. the port in the container is fixed but the port on the host is chosen from available ports, allowing many containers running programs with fixed ports
            - just leave off the host port definition, eg.  `docker run -ti -p 8080 ubuntu bash`
            - can find the assigned hostport with `docker port [container_name]`
            - can further specify protocol with `/[protocol]` eg. `docker run -ti -p 8080/tcp ubuntu bash`
    - Virtual Networking in Docker
        - check networking with `docker network ls`
        - create a new VN `docker network create [network_name]` 
        - run a container on a NV `docker run --rm -ti --net [netname] --name [container_name] ubuntu:14.04 bash` 
        - can put a container on multiple networks
            - `docker network connect [network] [container_to_connect]`
    - legacy linking
        - links all ports from one machine to another, only in one direction

- Managing Images
    - list downloaded images: `docker images`
    - clean up images: `docker rmi [image_id]`  

- Volumnes
    - Virtual disks that you can store data in and share between containers and containers->host
    - `persistent`: created to store data accessible between container and host, but remain after container deleted
    - `ephemeral`: only exist as long as a container is useing it 
    - start a container and share a folder in it: `docker run -ti -v full/path/to/folder:/path/in/container ubuntu bash`
        - ie. `-v` is the volume argument
    - sharing between containers
        - use `volumes-from`
            - so if one container has some data in it, then run another and get its volumes
                - `docker run -it --volumes-from [container_with_data] ubuntu bash`

- Registries
    - registries are pieces of software that manage and distribute images
    - search with `docker search [keyword]`
    - log in with `docker login` then `docker pull [imagename]` to get image 