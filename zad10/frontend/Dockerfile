FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

EXPOSE 3000

COPY ./src ./src
COPY ./public ./public
COPY ./tsconfig.json ./tsconfig.json

CMD [ "npm", "start" ]
