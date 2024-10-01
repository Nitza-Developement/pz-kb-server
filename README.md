# pz-kb-server 🦓🩷

Flask's Server Backend between (KillBill, Bigcommerce, Braintree) for the v2 of the Pink Zebra project

## Prerequisites

1. You need to have [Docker](https://docs.docker.com/) installed on your machine.
2. Then get the `.env`, install [Warp VPN](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/download-warp/) and configure it (ask the developer team for this step)

# 📦 Docker's Commands

### Build the image

```bash
docker build -t pz-kb-server .
```

### Create **container**

```bash
docker run --name pz-kb-server-container -d -p 5000:5000 pz-kb-server
```

<!-- Build & Create dev container  -->
<!-- docker build -t pz-kb-server-container . && docker run --name pz-kb-server -d -p 5000:5000 pz-kb-server-container -->

### Run container

```bash
docker run pz-kb-server-container
```

### Shell inside container

```bash
docker exec -it pz-kb-server-container /bin/sh
```

### Stop container

```bash
docker stop pz-kb-server
```

### Remove container

```bash
docker rmi pz-kb-server-container
```

# ↪️ Commands inside container

### run server

```bash
flask run
```

### run tests

```bash

```

<!-- TODO -->

## Note for developers 📝

- 📍 When **add**, **move** or **remove** any route file/folder please restart the server to watch the changes ..

- 📖 Swagger UI is located at [.../apidocs/](http://localhost:5000/apidocs/) and 🧾 Swagger spec can be fount at [.../apispec.json](http://localhost:5000/apispec.json)

- Please follow are rules ⚖️ to contribute in [CONTRIBUTING.md](./CONTRIBUTING.md)

## ⚙️ Built with :

- [Flask](https://flask.palletsprojects.com/en/3.0.x/) : Is a lightweight WSGI web application framework in Python
- [flasgger](https://github.com/flasgger/flasgger) : Is a simple Flask blueprint for adding Swagger UI to your Flask application; based on [swagger.io](https://swagger.io/)
- [KillBill](https://docs.killbill.io/) : Is an open-source billing and payment platform that automates complex billing processes.
- [BigCommerce](https://developer.bigcommerce.com/docs/api) : Is a NASDAQ-listed ecommerce platform that provides software as a service (SaaS) solutions to retailers.
- [Braintree](https://developer.paypal.com/braintree/docs/start/overview/) : Is a full-stack payment platform from PayPal that makes it easy to accept payments in your app or website.
