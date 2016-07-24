import sys
import os

def convert_to_bytes( str1 ):
	print("tsting")
	return "".join( "{:02x}".format( ord(c) ) for c in str1 )


def print_string( str1 , fileDEST , mult = 0 ):

	output = str(str1)
	global sysArgLen

	if sysArgLen == 5:
		if sys.argv[4] == "b":
			output = convert_to_bytes( output )
			str1 = output
			print(output)

	y = int(mult)
	while y > 1:
		print(output)
		output = output + str(str1)
		y = y - 1

	if os.path.exists( fileDEST ):
		with open( fileDEST , "a" ) as myfile:
			myfile.write( output )
	else:
		with open( fileDEST , "w" ) as myfile:
			myfile.write( output )

	print( output )	

sysArgLen = len( sys.argv )

if sysArgLen == 1:
	print("Pleae input a string to write\na File PATH\n\tor/and a multiplyer\n")
elif sysArgLen == 2:
	print( "still not enough options passed")
	print( sys.argv[1] )
elif sysArgLen == 3:
	print ( sys.argv[1] + " @ " + sys.argv[2] )
	print_string( sys.argv[1] , sys.argv[2] )
else:
	x = 0
	try:
		x = float( sys.argv[3] )
		print ( sys.argv[1] + " * " + sys.argv[3] + " @ " + sys.argv[2] )
	except:
		pass

	if x > 0:
		print_string( sys.argv[1] , sys.argv[2] , sys.argv[3] )
	else:
		print( "Third argument was not a number" )


