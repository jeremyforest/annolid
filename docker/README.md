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
xhost +local:docker
docker run -it -e XDG_RUNTIME_DIR=/tmp -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY -v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY -e QT_QPA_PLATFORM=wayland annolid:latest
```

