#!/bin/bash

filename=$1
outputfile=${filename%%.*}
echo $outputfile
#ffmpeg -i $1 -s 1080x1920 $outputfile".mp4"
ffmpeg -i $1 $outputfile"-copy.mp4"
