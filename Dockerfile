FROM node:7.10 as build-react
WORKDIR /react-app
COPY react-app/ /react-app/
RUN ls -l
RUN npm install --silent
RUN npm run build

FROM python:3.7.4-alpine as build-python
RUN apk --no-cache add build-base
WORKDIR /python-api
COPY python-api/ /python-api/
RUN pip install -r requirements.txt --target ./

#FROM nginx:1.17-alpine
#RUN apk --no-cache add python3
FROM python:3.7.4-alpine
RUN apk --no-cache add nginx
COPY --from=build-react /react-app/ /usr/share/nginx/html
COPY --from=build-python /python-api/* /python-api/
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

CMD ["/bin/sh", "-lc", "python /python-api/main.py"]
