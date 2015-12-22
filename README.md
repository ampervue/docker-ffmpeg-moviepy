
A Docker image running Ubuntu:trusty with latest Python 3.5 and latest FFMPEG (built from source)
Also installs moviepy and necessary packages (numpy, scipy, ImageMagick, etc.)
Image based on https://github.com/ampervue/docker-ffmpeg

For more on Moviepy, see http://zulko.github.io/moviepy/ 
Many thanks to all the contributors of that great project.

### To Build

~~~~
docker build -t <imageName> .
~~~~

### To pull and run from hub.docker.com

Docker Hub: https://registry.hub.docker.com/u/dkarchmervue/moviepy/

Source and example: https://github.com/ampervue/docker-ffmpeg-moviepy

~~~~
docker pull dkarchmervue/moviepy
docker run --rm -ti dkarchmervue/moviepy ffmpeg -version
docker run --rm -ti -v ${PWD}:/work dkarchmervue/moviepy python your-moviepy-script.py
docker run --rm -ti dkarchmervue/moviepy bash
~~~~

## Example

As an example, the python script demonstrates a
Hello Work, creating a title slide for 10sec

~~~~
# Pull image
docker pull dkarchmervue/moviepy

# Get example files and build new image
git clone https://github.com/ampervue/docker-ffmpeg-moviepy
cd example
docker build -t hello-world .

# Mount current directory on container so that file can be written back to host
# Assuming videos are on current directory
docker run --rm -ti -v ${PWD}:/code hello-world
ls hello_world.mp4
~~~~