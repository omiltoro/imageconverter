__author__ = 'REACH9'
import base64

with open("C:/Users/REACH9/Desktop/ritaprj1.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print str

    fh = open("C:/Users/REACH9/Desktop/imageToSave.png", "wb")
    fh.write(str.decode('base64'))
    fh.close()
    print "done"