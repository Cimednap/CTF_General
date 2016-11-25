#!/usr/bin/python 

from scapy.all import *


#open file for writing
f = open('results4.txt', 'a')

def customAction(packet):
	packetCount = 0
	if packet[0][1].dst == '192.168.1.198':
		data = str(packet)
		stripped = data[-2:]
		print "Writing these chars to file: %s" % (stripped)
		f.write(str(stripped))

sniff(offline='somepang.pcap', prn=customAction)

f.close()

