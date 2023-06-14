# Python Web Server With Basic Authentication

This Python web server implements basic authentication and can be used locally or in a Kubernetes cluster. The server has a home page that requires credentials to log in. The default credentials are `username` and `password`. If the correct credentials are provided, it will redirect you to `/token` with an HTTP 200 code and a message of "Successful authentication." If the credentials are incorrect, it will display a message of "Login failed" without redirecting.


## Deploy Locally

There are two ways to deploy the server locally:

### Option 1: Running on Your Machine

To run the server directly on your machine, follow these steps:

1. Make sure you have Python installed.
2. Run the following command:

```
python3 http-server.py
```
3. The server will be deployed, and you can access it at http://localhost:8000.

### Option 2: Using Docker
To deploy the server using Docker, follow these steps:

1. Make sure you have Docker installed on your machine.
2. Build the Docker image using the following command, replace `<name-of-the-image>` and `<img-tag>` in the command below with the actual values for your Docker image:
```
docker build -t <name-of-the-image>:<img-tag> .
```
3. Run the Docker container, mapping a host port to the container port, with the following command:
```
docker run -dp 8000:8000 <name-of-the-image>:<img-tag>
```
Alternatively, if you don't want to build the image, you can pull the pre-built image from Docker Hub:
```
docker run -dp 8000:8000 caroarbiza/python-webserver:1.0
```
4. The server will be deployed, and you can access it at http://localhost:8000.

## Deploy with Kubernetes
To deploy the server in a Kubernetes cluster, follow these steps:
1. Make sure you have a working Kubernetes cluster and are connected to it.
2. Deploy the server using the provided `deployment.yaml` manifest:
```
kubectl create -f deployment.yaml
```
3. Deploy the service to expose the server using the provided `service.yaml` manifest:
```
kubectl create -f service.yaml
```
Note: If you want to deploy in a specific namespace, use the -n flag to specify the namespace.

4. Once deployed, you can access the server using the external IP or DNS provided by the LoadBalancer service.
