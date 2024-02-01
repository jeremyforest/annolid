# Annolid Docker 

   _____                           .__   .__     .___ 
  /  _  \    ____    ____    ____  |  |  |__|  __| _/ 
 /  /_\  \  /    \  /    \  /  _ \ |  |  |  | / __ |  
/    |    \|   |  \|   |  \(  <_> )|  |__|  |/ /_/ |  
\____|__  /|___|  /|___|  / \____/ |____/|__|\____ |  
        \/      \/      \/                        \/  

                                                      
To help streamline installation we support a dockerized implementation of annolid. 
The image will also be available on DockerHub soon.


# To build the docker container: 

Please make sure that [Docker](https://www.docker.com/) is installed on your system.

```
cd annolid/docker
docker build -t annolid .
```

Then we need to get the `<Image ID>` of newly build container using: 
```
docker images
``` 

Copy the `<Image ID>` of the annolid repository and run 

```
xhost +local:docker
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix/ -e DISPLAY=$DISPLAY  <Image ID>
```
