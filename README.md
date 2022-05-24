# Useful-FFmpeg-Script
## FFmpeg 简单处理视频的实用脚本   

## cut.py

### 作用：ffmpeg视频处理脚本，包含视频裁切，视频转码，视频合并
* 参数说明：--i：视频路径，--m：选择视频处理工具{cut 裁切｜mg 合并｜ts 转码}，--t：每个子视频的时长(默认30s)，--o：输出路径
* 参数说明：--c：选择裁切的方法 {num 按数量裁切｜time 按时间裁切}，--n：裁切成多少个子视频(默认5个)，--a：音频路径
* 
### 裁切用法：
* 使用方法：python cut.py --m cut --c num --i <your_video> --n 10，将视频裁切成10份
* 使用方法：python cut.py --m cut --c time -t 30 --i <your_video>，每30s裁切一个子视频

### 转码h.264用法：
* 使用方法：python cut.py --m ts --i <input_path>

### 视频音频合并用法：
* 使用方法：python cut.py --m mg --i <video_path> --a <audio_path>

### 旋转视频
* 使用方法：python cut.py --i [video_path] --m ro --r [Angle]
* 



