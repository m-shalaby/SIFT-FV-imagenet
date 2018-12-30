import urllib.request as urllib
import tarfile
import os
count = 0
with open("Sysnets.txt") as f:
    for line in f:
        aSysName = line.strip()
        aSysName = aSysName.split()
        aSysName = aSysName[1]
        foreignName = "http://www.image-net.org/download/synset?wnid=" + aSysName + "&username=ismael&accesskey=ce8e942e93fd9b184750ca4dcf981282fbefe68a&release=latest&src=stanford"
        localName = "ImageData/" + aSysName + ".tar.gz"
        print("Sys Num: " + str(count) + " " + aSysName)
        urllib.urlretrieve(foreignName,localName)
        tar = tarfile.open(localName)
        tar.extractall(path="ImageData/"+ aSysName+"/")
        tar.close()
        if os.path.exists(localName):
            os.remove(localName)
        count = count + 1
 
