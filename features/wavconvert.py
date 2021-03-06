import envoy
import sys


def mp3_to_wav(file_name):
    wav_file_name = "".join(file_name.split('.mp3')[:-1:]) + ".wav"
    cmd = "ffmpeg -i '{0}' '{1}'".format(file_name, wav_file_name)
    e = envoy.run(cmd)
    e.status_code
    return wav_file_name
