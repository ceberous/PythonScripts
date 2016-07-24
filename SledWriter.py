import sys
import os

hex_letters = [ "a" , "b" , "c" , "d" , "e" , "f" ]

# 1 letter and 1 number for each spot in length
def pattern_fill( length ):

	global hex_letters
	output = ''

	l = int(length)
	bounds = 16
	
	i = 0
	j = 1
	hLPOS = 0
	
	while i < l: 

		while j < 10:

			output = output + hex_letters[hLPOS] + str(j)
			j = j + 1
			i = i + 1

		j = 1
		hLPOS = hLPOS + 1
		if hLPOS > len(hex_letters) - 1:
			hLPOS = 0

	print(output)

	fileDEST = os.getcwd()
	fileDEST = os.path.join( fileDEST , "patternFILL.txt" )
	if os.path.exists( fileDEST ):
		with open( fileDEST , "a" ) as myfile:
			myfile.write( output )
	else:
		with open( fileDEST , "w" ) as myfile:
			myfile.write( output )



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
	# just a simple patter-fill dump
	pattern_fill(sys.argv[1])
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


