from alpine
MAINTAINER Todd Dah <t@d.com?

##install terraform
RUN wget -O /temp/terraform.zip https://releases.hashicorp.com/terraform/0.12.28/terraform_0.12.28_linux_amd64.zip
RUN unzip /temp/terraform.zip -d /

## prevent malicious use of container root on host machine 
USER nobody