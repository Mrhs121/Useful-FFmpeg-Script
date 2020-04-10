#!/bin/bash

if [ $# -eq 2 ];
then 
    vedio=$1
    audio=$2
    outputfile=${vedio%.*}
    ffmpeg -strict -2 -i $vedio  -vcodec copy  temp.mp4
    ffmpeg   -2 -i temp.mp4 -i $audio -c copy $outputfile"-merge.mp4"
    rm -f temp.mp4
    echo -n "Do you want to del the origin file?(yes/no)"
    read res
    if [ $res == 'yes' ]
    then 
        echo "del origin file:$vedio and $audio"
        rm -f $vedio
        rm -f $audio 
    fi
fi

