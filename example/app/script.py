__author__ = 'David Karchmer'

import os
import sys
import json
import logging
import argparse
from logging import StreamHandler, Formatter

import moviepy.editor as moviepy

if __name__ == "__main__":

    # Logger Format
    FORMAT = '[%(asctime)-15s] %(levelname)-6s %(message)s'
    DATE_FORMAT = '%d/%b/%Y %H:%M:%S'
    formatter = Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)
    handler = StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-o', dest='output', type=str, help="Output File", default='stack.mp4')
    __author__ = 'dkarchmer'

import os
import sys
import json
import logging
import argparse
from logging import StreamHandler, Formatter

#from moviepy.editor import *
import moviepy.editor as moviepy


if __name__ == "__main__":

    # Logger Format
    FORMAT = '[%(asctime)-15s] %(levelname)-6s %(message)s'
    DATE_FORMAT = '%d/%b/%Y %H:%M:%S'
    formatter = Formatter(fmt=FORMAT, datefmt=DATE_FORMAT)
    handler = StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-o', dest='output', type=str, help="Output File", default='stack.mp4')
    parser.add_argument('videos', metavar='videos', type=str, nargs='+', help='Videos to process')

    args = parser.parse_args(sys.argv[1:])

    logger.debug('ARGS: ' + str(args))

    if not args.jsonfile:
        logger.error('Missing required configuration json file')
        exit(1)

    logger.info('Processing data from Json file: {0}'.format(args.jsonfile))
    json_file = video_file = os.path.join(args.indir, args.jsonfile)
    if not os.path.isfile(json_file):
        logger.error('Json file not found: {0}'.format(json_file))
        exit(1)

    json_data=open(json_file).read()
    data = json.loads(json_data)
    logger.info(data)

    print('Generate Matrix')


    clips = []
    for v in data['videos']:
        # If we need to resize: clip.fx( resize, width=240)
        clips.append(moviepy.VideoFileClip(os.path.join(data['input_dir'], v['file']))
                     .subclip(v['ss'],v['ss']+60*data['duration']).without_audio().margin(10))
        #             .set_start(v['ss']).set_duration(30).without_audio().margin(10))

    final_clip = moviepy.clips_array([[clips[0], clips[1]], [clips[2], clips[3]]])

    final_clip.write_videofile(args.output)

    args = parser.parse_args(sys.argv[1:])

    logger.debug('ARGS: ' + str(args))

    if not args.jsonfile:
        logger.error('Missing required configuration json file')
        exit(1)

    logger.info('Processing data from Json file: {0}'.format(args.jsonfile))
    json_file = video_file = os.path.join(args.indir, args.jsonfile)
    if not os.path.isfile(json_file):
        logger.error('Json file not found: {0}'.format(json_file))
        exit(1)

    json_data=open(json_file).read()
    data = json.loads(json_data)
    logger.info(data)

    print('Generate Matrix')


    clips = []
    for v in data['videos']:
        # If we need to resize: clip.fx( resize, width=240)
        clips.append(moviepy.VideoFileClip(os.path.join(data['input_dir'], v['file']))
                     .subclip(v['ss'],v['ss']+60*data['duration']).without_audio().margin(10))
        #             .set_start(v['ss']).set_duration(30).without_audio().margin(10))

    final_clip = moviepy.clips_array([[clips[0], clips[1]], [clips[2], clips[3]]])

    final_clip.write_videofile(args.output)
