# Server to ping (ex. google or default gateway)
#SERVER=8.8.8.8
SERVER=192.168.0.1

# Send two pings and output to /dev/null
ping -c2 ${SERVER} > /dev/null

# If internet is down, reconnect
if [ $? != 0 ]
then
    # ifdown and ifup aren't currently working for me
    #ifdown --force wlan0
    #ifup wlan0
    sudo ifconfig wlan0 down
    sudo ifconfig wlan0 up
fi
