FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY ./src ./src
COPY ./resources ./resources

EXPOSE 8080

CMD [ "node", "src/server.js" ]
