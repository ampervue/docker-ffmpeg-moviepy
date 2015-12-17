FROM dkarchmervue/moviepy

# https://github.com/ampervue/ffmpeg-moviepy
# https://hub.docker.com/r/dkarchmervue/moviepy/

MAINTAINER David Karchmer <dkarchmer@gmail.com>

# ============================================================================
# As an example, create a clip with a 'Hello World' title
#
# ~~~~
# # Pull image
# docker pull dkarchmervue/moviepy
#
# # Get example files and build new image
# git clone https://github.com/ampervue/ffmpeg-moviepy
# cd example
# docker build -t example .
#
# # Mount current directory on container so that file can be written back to host
# # Assuming videos are on current directory
# docker run --rm -ti -v ${PWD}:/code example
# ls hello_world.mp4
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





