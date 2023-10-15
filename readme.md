# Torch, Timm, FastAPI, Pillow Application

This is a Dockerized application that combines the power of Torch, Timm, FastAPI, and Pillow to provide a customizable image processing API. You can use this README as a starting point for your project's documentation.

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Build and run the docker image

```bash
docker build -t image_recognition .
docker run -d -p 80:80 image_recognition
docker run -it -p 8000:8000 image_recognition /bin/bash

```
