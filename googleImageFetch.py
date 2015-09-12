import urllib2
import simplejson
import cStringIO
from PIL import Image
import os

searchTerm = raw_input("Enter Search Tearm : ")

# needs to parse for spaces and such things
buildTerm = ""

for i in searchTerm.split(' '):
	buildTerm += i
	buildTerm += "+"



array = searchTerm.split(' ')
buildDir = ''
i = 0

while i < ( len(array) - 1 ):
	buildDir += array[i]
	buildDir += '\ '
	i += 1

buildDir += array.pop()
buildDir += '/'


startIndex = 1
iterations = raw_input("Enter Number of Images : ")

while startIndex <= iterations:
	fetcher = urllib2.build_opener()
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + buildTerm + "&start=" + str(startIndex)
	f = fetcher.open(searchUrl)
	deserialized_output = simplejson.load(f)
	imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
	file = cStringIO.StringIO(urllib2.urlopen(imageUrl).read())
	saveName = imageUrl.split("/")
	saveName = saveName.pop()
	if file:
		img = Image.open(file)
		try :
			img.save( saveName )
		except :
			pass
	startIndex += 1




# create a folder for pictures
# curDir = os.path.dirname(os.path.abspath(__file__))
# mypath = curDir + '/' + searchTerm
# if not os.path.isdir(mypath):
	#os.makedirs(mypath)

# savePath = curDir + '/' + buildDir 

# img.show()


