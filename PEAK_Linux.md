# How to use PEAK adapters in Linux?

PEAK Website: https://www.peak-system.com/fileadmin/media/linux/index.htm
1. Check if CAN drivers are part of your Linux environment:
    > grep PEAK_ /boot/config-`uname -r`
2. Check if the CAN device is initialized:
    > lsmod | grep ^peak


https://blog.mbedded.ninja/programming/operating-systems/linux/how-to-use-socketcan-with-the-command-line-in-linux/

1. Run below 3 lines to start the PEAK adapter as a network adapter, then use socketcan to treat it as a regular UDP socket:
    > sudo modprobe peak_usb
    > sudo ip link set can0 up type can bitrate 500000
    > sudo ip link set can0 up
    Can store above lines to a .sh file, an then in the terminal window:
        > chmod +x ./[filename].sh
        > ./[filename].sh

2. Check if can0 is in the list
    > sudo apt install net-tools
    > ifconfig OR ifconfig can0

3. Use can-utils to interact with it: https://github.com/linux-can/can-utils
    > sudo apt install can-utils
    - Send:
        > cansend can0 123#1122334455667788
    - display messages:
        > candump can0

4. Run below script:
   > #!/bin/bashcan dump
   > if ! ip link show can0 | grep -q "UP"; then
   >     sudo modprobe peak_usb
   >     sudo ip link set $1 type can bitrate $2
   >     sudo ip link set up $1
   > fi
 
i put it in my home directory and use it with ./scriptname.sh <any name you want> <baud rate>

5. Unload PEAK:
    > sudo rmmod peak_usb

PCAN-USB FD: https://gist.github.com/pranav083/6be974e881ffa494e8096e5c7eb90c23
