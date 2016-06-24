from PIL import Image
from collections import Counter
import sys

rPixels = []
gPixels = []
bPixels = []

def computeCommonValues(img):

    rPixels.sort()
    gPixels.sort()
    bPixels.sort()

    rCount = Counter(rPixels).most_common(3)
    gCount = Counter(gPixels).most_common(3)
    bCount = Counter(bPixels).most_common(3)

    print ("          1.)          2.)        3.)")
    print ( "R =          " + str(rCount[0][0]) + "            " + str(rCount[1][0]) + "            " + str(rCount[2][0]) )
    print ( "G =          " + str(gCount[0][0]) + "            " + str(gCount[1][0]) + "            " + str(gCount[2][0]) )
    print ( "B =          " + str(bCount[0][0]) + "            " + str(bCount[1][0]) + "            " + str(bCount[2][0]) )



def compute_average_image_color(img):
    width, height = img.size

    r_ave = 0
    g_ave = 0
    b_ave = 0

    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_ave = (r + r_ave) / 2
            g_ave = (g + g_ave) / 2
            b_ave = (b + b_ave) / 2

            rPixels.append(r)
            gPixels.append(g)
            bPixels.append(b)

    return (r_ave, g_ave, b_ave)

img = Image.open(sys.argv[1])
#img = img.resize((50,50))  # Small optimization
average_color = compute_average_image_color(img)
print("\nPrimary Average = ")
print(average_color)

print("\nMost Common 3 Values = \n")
computeCommonValues(img)
