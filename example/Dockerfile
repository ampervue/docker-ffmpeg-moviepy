FROM dkarchmervue/ffmpeg-moviepy

# https://github.com/ampervue/ffmpeg-moviepy

MAINTAINER David Karchmer <dkarchmer@gmail.com>

# ============================================================================
# As an example, the python script uses moviepy to build a 2x2 mosaic
# based on four videos
#
# ~~~~
# # Pull image
# docker pull dkarchmervue/ffmpeg-moviepy
#
# # Get example files and build new image
# git clone https://github.com/ampervue/ffmpeg-moviepy
# cd example
# docker build -t mosaic .
#
# # Mount current directory on container so that file can be written back to host
# # Assuming videos are on current directory
# docker run --rm -ti -v ${PWD}:/code mosaic video1.mp4 video2.mp4 video3.mp4 video4.mp4
# ls mosaic.mp4
# ~~~~
# ============================================================================

# Step 1: Install any Python packages
# ----------------------------------------

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

# Step 2: Copy Python script
# ----------------------------------------

ADD app /code/app

# Step 3: Configure entrypoint
# ----------------------------------------

CMD           ["-h"]
ENTRYPOINT    ["/usr/bin/python", "app/script.py"]





