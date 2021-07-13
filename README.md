# ip-webcam-usb
Simple script for Linux to use Android device with "IP Webcam" app as USB Webcam

## Dependencies:
**adb:**
```
sudo apt install adb
```

**v4l2loopback:**
```
sudo apt install v4l2loopback-utils v4l2loopback-dkms
```

## Note:
You'll need Ip Webcam server started on your Android device and connected on USB. Then start the script.

If you're with multiple devices connected, you'll need to specify the device serial number.


## Usage:
```webcam_script.py [-h] [-s SERIAL] [-hp HOSTPORT] [-dp DEVICEPORT] [-n VIDEONUMBER]```
```
optional arguments:
  -h, --help            show this help message and exit
  -s, --serial          use device with given serial (overrides $ANDROID_SERIAL)
  -hp, --hostport       host port
  -dp, --deviceport     android device port
  -n, --videonumber     number of virtual webcam
```
