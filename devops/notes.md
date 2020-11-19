- manifest
docker-compose.yaml is the manifest that used to launch a bunch of services in coordinated fashion. 

- testing
    - in docker-compose manifest, use `unit-tests` variable under `services` to:
        - mount the test dir to the container with `volumes`  
            
            volumes:  
             - "$PWD:/app"  
        - build an rspec image (see docker-compose manifest)          

- Terraform
    - provision and track infrastructure

*From Devops Foundations course
- githooks: do things like run unit tests before a git push is run