import os
import sys
import xlwt
from moviepy.editor import VideoFileClip
import argparse

 
class FileUtils():
 
    def __init__(self):
    	pass
    def get_filesize(self,filename):
        """
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)
 
    def get_file_times(self,filename):
        """
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time,clip.duration
 
    def sizeConvert(self,size):# 单位换算
        K, M, G = 1024, 1024**2, 1024**3
        if size >= G:
            return str(size/G)+'G Bytes'
        elif size >= M:
            return str(size/M)+'M Bytes'
        elif size >= K:
            return str(size/K)+'K Bytes'
        else:
            return str(size)+'Bytes'
    
    def timeConvert(self,size):# 单位换算
        M, H = 60, 60**2
        if size < M:
            return str(size)+u'秒'
        if size < H:
            return u'%s分钟%s秒'%(int(size/M),int(size%M))
        else:
            hour = int(size/H)
            mine = int(size%H/M)
            second = int(size%H%M)
            tim_srt = u'%s小时%s分钟%s秒'%(hour,mine,second)
            return tim_srt

def cut(input,t,output):
    file_util = FileUtils()
    _,s = file_util.get_file_times(input)
    _filename = os.path.basename(input)
    filename, extension = os.path.splitext(_filename)
    print(filename, extension)
    isExists=os.path.exists(filename)
    if not isExists:
        os.makedirs(filename) 
    import math
    num = math.ceil( s / t)
    print(num)
    for i in range(0,num):
        start = i*t
        os.system('ffmpeg -ss {} -t {} -accurate_seek -i {} -codec copy -avoid_negative_ts 1 {}/cut-{}.{}'.format(start,t,input,filename,str(i+1),extension))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', type=str,help='the path of the video')
    parser.add_argument('--t', type=int,help='The length of each subvideo',default=30)
    parser.add_argument('--o', type=str,help='The path of the output',default='subvideo')
    args = parser.parse_args()
    if args.i:
        print("Cut ",args.i)
        cut(args.i,args.t,args.o)
    else:
        print("please give the input file")
