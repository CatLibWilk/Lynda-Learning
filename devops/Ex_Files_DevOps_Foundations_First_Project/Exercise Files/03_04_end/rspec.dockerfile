FROM ruby:alpine
MAINTAINER Carlos Nunez <dev@carlosnunez.me>

RUN apk add --no-cache build-base ruby-nokogiri
RUN gem install  capybara selenium-webdriver
ENTRYPOINT [ "" ]
