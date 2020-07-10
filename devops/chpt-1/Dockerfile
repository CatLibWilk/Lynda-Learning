FROM nginx:alpine
MAINTAINER Andy W >andrewdwilk@gmail.com>
#this is note for person maintaining

COPY website /website
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
# this is output, doesn't do anything else, ie. you would need to manually map 80 to 80 when running the resulting image