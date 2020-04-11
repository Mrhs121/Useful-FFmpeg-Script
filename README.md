# Useful-FFmpeg-Script
## ffmpeg 简单处理视频的实用脚本   

## cut.py

### 作用：ffmpeg视频处理脚本，包含视频裁切，视频转码，视频合并
* 参数说明：--i：视频路径，--m：选择视频处理工具【裁切｜合并｜转码】，--t：每个子视频的时长，--o：输出路径
* 参数说明：--c：选择裁切的方法【按数量裁切｜按时间裁切】，--n：裁切成多少个子视频，--a：音频路径
### 裁切用法：
* 使用方法：python cut.py --m cut --i [your_videio] --n 10，将视频裁切成10份
* 使用方法：python cut.py --m cut --c time -t 30 --i [your_videio]，每30s裁切一个子视频

### 转码用法：
* 使用方法：python cut.py --m ts --i [input_path]

### 合并用法：
* 使用方法：python cut.py --m mg --i [input_path]

webm2mp4.sh


##下面这些脚本都融合在cut.py中了
## webm2mp4.sh
* 作用：将webm转换成mp4格式

* 使用方法：./webm2mp4.sh [webm_file]

## merge.sh
* 作用：把音频合并到视频中

* 使用方法：./merge.sh [vidio_file] [audio_file]
