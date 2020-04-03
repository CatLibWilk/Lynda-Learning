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