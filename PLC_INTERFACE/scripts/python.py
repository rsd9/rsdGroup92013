#!/usr/bin/env python
import roslib; roslib.load_manifest('PLC_INTERFACE')
import rospy
from std_msgs.msg import String
import time
import serial


def callback(data):
	signal = data.data
	rospy.loginfo(signal)
	if(signal=="1"):
		ser.write("sta")
	if(signal=="0"):
		ser.write("sto")
	ser.flush()
		

def main():
	rospy.init_node('plcControl', anonymous=True)
	rospy.Subscriber("robotReady", String, callback)
	global ser
	ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
	
	ser.open()
	ser.isOpen()
# 	run = 1
#  	while run:
# 		output = raw_input(">> ")
# 		if output == "q":
# 			print "Closing connection!"
# 			exit()
# 		else:
# 			print "Sending data : " + output
# 			ser.write(output)
# 		    
# 	
# 		time.sleep(1)
# 		while ser.inWaiting() > 0:
# 			bits = ser.read(ser.inWaiting())
# 			print "Received data: " + bits
	
	rospy.spin()
	
	


if __name__ == '__main__':
    main()
