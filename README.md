# docker-ffmpeg-moviepy

A Docker image running Ubuntu:trusty with latest Python 3.5 and latest FFMPEG (built from source)
Also installs moviepy and necessary packages (numpy, scipy, ImageMagick, etc.)

### To Build

~~~~
docker build -t <imageName> .
~~~~

### To pull and run from hub.docker.com

Docker Hub: https://registry.hub.docker.com/u/dkarchmervue/ffmpeg-moviepy/

Source and example: https://github.com/ampervue/ffmpeg-moviepy

~~~~
docker pull dkarchmervue/ffmpeg-moviepy
docker run -ti dkarchmervue/ffmpeg-moviepy
~~~~

## Example

As an example, the python script uses FFMPEG to build a mosaic of
four videos

~~~~
# Pull image
docker pull dkarchmervue/ffmpeg-moviepy

# Get example files and build new image
git clone https://github.com/ampervue/ffmpeg-moviepy
cd example
docker build -t mosaic .

# Mount current directory on container so that file can be written back to host
# Assuming videos are on current directory
docker run --rm -ti -v ${PWD}:/code mosaic video1.mp4 video2.mp4 video3.mp4 video4.mp4
ls mosaic.mp4

# To run with bash
docker run --entrypoint bash -ti thumbnail
~~~~