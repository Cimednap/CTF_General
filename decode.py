#!/usr/bin/python 

import base64

with open ('results2.txt') as f:
		decoded = base64.b64decode()

		print decoded