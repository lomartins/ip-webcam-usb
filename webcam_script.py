#!/usr/bin/python3
from argparse import ArgumentParser
import subprocess
import os

CMD_SUCCESS = 0


class WebcamArgumentParser(ArgumentParser):
    def __init__(self):
        super().__init__()
        self.add_argument('-s', '--serial', type=str, help='use device with given serial (overrides $ANDROID_SERIAL)')
        self.add_argument('-hp', '--hostport', type=int, help='host port', default="4545" ,)
        self.add_argument('-dp', '--deviceport', type=int, help='android device port', default="8080")
        self.add_argument('-n', '--videonumber', type=int, help='video number', default="42")


class WebcamCommands:
    @staticmethod
    def start_connection(host_port, device_port, serial=None):
        if serial == None:
            forward_cmd = f'adb forward tcp:{host_port} tcp:{device_port}'
        else:
            forward_cmd = f'adb -s {serial} forward tcp:{host_port} tcp:{device_port}'

        return subprocess.getstatusoutput(forward_cmd)

    @staticmethod
    def start_virtual_device(video_number):
        virtual_device_cmd = f'sudo modprobe v4l2loopback devices=2 video_nr=0,{video_number} exclusive_caps=0,1'
        return subprocess.getstatusoutput(virtual_device_cmd)

    @staticmethod
    def open_webcam_connection(host_port, video_number):
        webcam_connection_cmd = f'gst-launch-1.0 souphttpsrc location=http://localhost:{host_port}/video ! jpegdec ! videoconvert ! v4l2sink device=/dev/video{video_number}'
        os.system('pkill gst-launch-1.0')
        os.system(webcam_connection_cmd)


def main():
    args = WebcamArgumentParser().parse_args()

    conection_status = WebcamCommands.start_connection(args.hostport, args.deviceport, args.serial)
    if conection_status[0] is not CMD_SUCCESS:
        print('Error when starting adb forward: ' + conection_status[1])
        return

    virtual_device_status = WebcamCommands.start_virtual_device(args.videonumber)
    if virtual_device_status[0] is not CMD_SUCCESS:
        print('Error when starting v4l2loopback virtual device: ' + conection_status[1])
        return

    WebcamCommands.open_webcam_connection(args.hostport, args.videonumber)

if __name__ == '__main__':
    main()
