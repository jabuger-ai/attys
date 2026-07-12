#! /bin/sh
avconv -f alsa -i pulse -f x11grab -show_region 1 -r 25 -s 1280x720 -i :0.0+2000,200 -threads 0 -b 10M -b:a 256k -ac 1 -strict experimental $1
