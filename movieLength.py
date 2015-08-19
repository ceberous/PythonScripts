#!/usr/bin/env python
import math
import os
import sys
from Tkinter import *
import tkFileDialog, Tkconstants
from hachoir_metadata import extractMetadata
from hachoir_parser import createParser

dirpathAsk = tkFileDialog.askdirectory()
if (dirpathAsk):
	print(dirpathAsk)
	currentDir = dirpathAsk
else:
	currentDir = os.path.dirname(os.path.realpath(__file__))

def getinfo(rootdir, extensions=(".avi", ".mp4" , ".mov")):
    if not isinstance(rootdir, unicode):
       rootdir = rootdir.decode(sys.getfilesystemencoding())
    for dirpath, dirs, files in os.walk(rootdir):
        dirs.sort() # traverse directories in sorted order
        files.sort()
        for filename in files:
            if filename.endswith(extensions):
               path = os.path.join(dirpath, filename)
               yield path, extractMetadata(createParser(path))



totalHours = 0
totalMinutes = 0
totalSeconds = 0.0

for path, metadata in getinfo(currentDir):
    if metadata.has('duration'):
    	
    	current = metadata.get('duration')
    	current = str(current)
    	working = current.split(':')

    	totalHours = totalHours + float(working.pop(0))
    	totalMinutes = totalMinutes + float(working.pop(0))
    	totalSeconds = totalSeconds + float(working.pop(0))

        # print("%s" % metadata.get('duration'))


if (totalSeconds > 59):
	x = math.floor( (totalSeconds / 60) )
	totalMinutes = totalMinutes + x
	totalSeconds = totalSeconds % 60

if (totalMinutes > 59):
	x = math.floor( (totalMinutes / 60) )
	totalHours = totalHours + x
	totalMinutes = totalMinutes % 60

print("Total Hours = %s" % totalHours )
print("Total Minutes = %s" % totalMinutes )
print("Total Seconds = %s" % totalSeconds )

displayText = "Total Hours : " + str(totalHours) + "\n" + "Total Minutes : " + str(totalMinutes) + "\n" + "Total Seconds  : " + str(totalSeconds) 

root = Tk()
w = Label(root , text=displayText)
w.pack()
root.mainloop()