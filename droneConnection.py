#
# Tello Python3 Control Demo (Edited)
#
# http://www.ryzerobotics.com/
#
# 1/1/2018


import threading 
import socket
import sys
import time


# You do not need to make any edits to this program to 
# connect to the drone. This will work for all of them.
#
# I left a brief guidebatter to getting a drone connected at the bottom of the 
# program to help if you are having any issues.
#
# Feel free to implement this in your software.



# Inputting the local address. You do not need to change this.
host = ''
port = 9000
locaddr = (host,port) 


# Creating the socket that will connect to the drone.
droneSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Saving of the drones IP/UDP Port Numbers. Commands are will be sent to this port.
tello_address = ('192.168.10.1', 8889)


# Connecting our socket to the drone:
droneSocket.bind(locaddr)

# From this point on, your program can communicate and send commands to your drone.
# A few different commands will be printed when the program is run.


print ('\r\n\r\nTello Python3 Demo.\r\n')
print ('Tello commands:\ncommand takeoff land flip forward back left right\nup down cw ccw speed speed?\r\n')
print ('To put the drone into sdk mode, send the following input: command \r\n')
print ('To sever the connection, send the following input: end \r\n')

def recv():
    count = 0
    
    while True: 

        try:
            data, server = droneSocket.recvfrom(1518)
            print(data.decode(encoding="utf-8"))

        except Exception:
            print ('\nExit . . .\n')
            break


recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 
    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            droneSocket.close()  
            break

        msg = msg.encode(encoding="utf-8") 
        sent = droneSocket.sendto(msg, tello_address)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        droneSocket.close()  
        break




# To connect the program to a tello drone:

# 1.
# The Tello drone has two unique identifiers, located underneath the battery.
# The WIFI SSID is the only one you need to look for.
#
# It will look something like:
# WIFI: TELLO-58A55
#
# Make note of your drones WIFI SSID. You will connect your computer to this later. 


# 2. 
# On the side of the drone there is a small button. 
# Press it once and the drone will turn on, starting a series of blinking lights on the
# front of the drone.
#
# The lights indicate the current state of the drone, you can reference page 6 of
# the user manual to determine their meaning.
# 
# If the drone is charged then it should settle on a yellow blinking light. 
# In this state, you can connect to the drone.


# 3. 
# You will need to connect the computer running the program to the drone, 
# the same way you would connect your computer to a wifi network.
#
# Open up your WIFI settings and if your drone is on and outputting a signal, 
# the WIFI SSID (e.g. TELLO-58A55) will appear, as though it were any other WIFI network.
# 
# Connect to this signal.


# 4. 
# At this point, you can run this program to connect to the drone.
#
# Once running, this 
# To put the drone into SDK mode, send it: "command".
#
# This allows the drone to accept other commands.
#
# You can find the full list of commands the drones can accept
# on the Tello SDK user guide
# 
# To sever your connection, send "end".