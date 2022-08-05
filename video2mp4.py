import os
from pathlib import Path

def convert_to_mp4(video_file, out_dir):
    if not Path(out_dir).exists():
        Path(out_dir).mkdir(parents=True, exist_ok=True)

    output = Path(out_dir) / Path(video_file).stem
    cmd = f'ffmpeg -i "{video_file}" -y -vcodec copy -acodec copy "{str(output)}.mp4"'
    print(cmd)
    os.system(cmd)
