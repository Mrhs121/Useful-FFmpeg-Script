import os
import sys
import xlwt
from moviepy.editor import VideoFileClip
import argparse
import math
 
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

def create_output_path(input,output):
    _filename = os.path.basename(input)
    filename, extension = os.path.splitext(_filename)
    output_dir = os.path.join(output,'sub-videos',"sub-"+filename)
    print("output path: ",output_dir)
    isExists=os.path.exists(output_dir)
    if not isExists:
        os.makedirs(output_dir)
    base_output_file = 'sub{}-'+filename+extension
    return os.path.join(output_dir,base_output_file),filename

def cut_by_duration_time(input,t,output='./'):
    file_util = FileUtils()
    _,s = file_util.get_file_times(input)
    base_output_file,filename = create_output_path(input,output)
    num = math.ceil( s / 30 )
    print("filename:{} length: {}".format(filename,s))
    print("cut video into {} subv, every subv {}s".format(num,t))
    cut(num,t,base_output_file,input)
    # for i in range(0,num):
    #     print("生成 sub-{}".format(i+1))
    #     start = i*t
    #     output_file = base_output_file.format(i)
    #     os.system('ffmpeg -y -loglevel 0 -ss {} -t {} -accurate_seek -i {} -codec copy -avoid_negative_ts 1 {} > /dev/null'.format(start,t,input,output_file))

def cut_by_num_of_subvideo(input,n,output='./'):
    file_util = FileUtils()
    _,second = file_util.get_file_times(input)
    base_output_file,filename = create_output_path(input,output)
    sub_second = math.ceil( second / n )
    print("filename:{} length: {}".format(filename,second))
    print("cut video into {} subv, every subv {}s".format(n,sub_second))
    cut(n,sub_second,base_output_file,input)
    # for i in range(0,n):
    #     print("生成 sub-{}".format(i+1))
    #     start = i*sub_second
    #     output_file = base_output_file.format(i)
    #     os.system('ffmpeg -y -loglevel 0 -ss {} -t {} -accurate_seek -i {} -codec copy -avoid_negative_ts 1 {} '.format(start,sub_second,input,output_file))

def cut(n,sub_second,base_output_file,input):
    for i in range(0,n):
        print("生成 sub-{}".format(i+1))
        start = i*sub_second
        output_file = base_output_file.format(i)
        os.system('ffmpeg -y -loglevel 0 -ss {} -t {} -accurate_seek -i {} -codec copy -avoid_negative_ts 1 {} '.format(start,sub_second,input,output_file))

def to_mp4(input,output='./'):
    file_util = FileUtils()
    _,second = file_util.get_file_times(input)
    _filename = os.path.basename(input)
    filename, extension = os.path.splitext(_filename)
    output_dir = os.path.join(output,'conversed')
    isExists=os.path.exists(output_dir)
    if not isExists:
        os.makedirs(output_dir)  

    output_file = os.path.join(output_dir,filename+'-conv.mp4')
    print("====> save to ",output_file)
    os.system('ffmpeg -i {} {}'.format(input,output_file))


def merge(video_path,audio_path,output):
    _filename = os.path.basename(video_path)
    filename, extension = os.path.splitext(_filename)
    output_dir = os.path.join(output,'merged')
    isExists=os.path.exists(output_dir)
    if not isExists:
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir,filename+'-merge.mp4')
    print("====> save to ",output_file)
    os.system('ffmpeg -i {}  -vcodec copy  temp.mp4'.format(video_path))
    os.system('ffmpeg -loglevel 0 -y -i temp.mp4 -i {} -c copy {}'.format(audio_path,output_file))
    os.remove('temp.mp4')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ffmpeg视频处理脚本，包含视频裁切，视频转码，视频合并")
    parser.add_argument('--i', type=str,help='the path of the video')
    parser.add_argument('--m', type=str,help='use which tool. [cut] for cut or [ts] for transcoding or [mg] for merge')
    parser.add_argument('--t', type=int,help='The length of each subvideo',default=30)
    parser.add_argument('--o', type=str,help='The path of the output',default='./')
    parser.add_argument('--c', type=str,help='the approch of cut. [num]:cut_by_num_of_subvideo or [time]:cut_by_duration_time',default='num')
    parser.add_argument('--n', type=int,help='num_of_subvideo',default=5)
    parser.add_argument('--a', type=str,help='the audio path')
    args = parser.parse_args()
    if args.m:
        if args.m=='cut' and args.i:
            if args.c == 'time':
                print("cut_by_duration_time: ")
                cut_by_duration_time(args.i,args.t,args.o)           
            elif args.c == 'num':
                print("cut_by_num_of_subvideo")
                cut_by_num_of_subvideo(args.i,args.n,args.o)
            else:
                print("Please specify the approch of cut: [time] or [num]")
        elif args.m=='ts'and args.i:
            to_mp4(args.i,args.o)
        elif args.m=='mg' and args.i and args.a:
            merge(args.i,args.a,args.o)
        else:
            print("Please specify which tool to be use:  [c] for cut or [t] for transcoding")
            parser.print_help()
    else:
        print("Please specify which tool to be use:  [c] for cut or [t] for transcoding")
        parser.print_help()
