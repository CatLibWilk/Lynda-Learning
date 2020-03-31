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