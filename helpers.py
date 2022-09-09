
from random import randint
from PIL import Image;
from os.path import exists
import os
import json


# connstants
WIDTH = 2000
HEIGHT = 2400
SUB_WIDTH = 800




def generateAssets(directory):
    mainFolder = os.getcwd()
    print("Looking directory " + directory)
    os.chdir(directory)
    counter = 0
    for count, path in enumerate(os.listdir()):
        
        print(path)
        if exists(str(count)+".png") :
            print("File already existing, do nothing...")
        else:
            os.rename(path, str(count)+".png")
        counter = count
    
    print("MAX INDEX: " + str(counter))
    os.chdir(mainFolder)
    return counter



def generate(img_code):

    codes = img_code.split("_")

    background = codes[0].split("-")[1]
    top = codes[1].split("-")[1]
    middle = codes[2].split("-")[1]
    bottom = codes[3].split("-")[1]

    print("BG-filename: " + background )
    print("TOP-filename: " + top)
    print("MIDDLE-filename: " + middle)
    print("BOTTOM-filename: " + bottom)
    bgFile  = Image.open("BG/"+ background + ".png")
    tFile  = Image.open("TOP/"+ top + ".png")
    mFile  = Image.open("MIDDLE/"+ middle + ".png")
    bFile  = Image.open("BOTTOM/"+ bottom + ".png")


    #generate

    im = Image.new("RGBA", (WIDTH, HEIGHT))
    im.paste(bgFile)
    im.paste(tFile, (0,0), mask= tFile)
    im.paste(mFile, (0,SUB_WIDTH * 1), mask= mFile)
    im.paste(bFile, (0,SUB_WIDTH * 2), mask=bFile)

    im.save("static/art.png")
    return im


def build():
    bgIndex =  generateAssets("BG")
    topIndex =  generateAssets("TOP/")
    mIndex =  generateAssets("MIDDLE/") 
    bIndex =  generateAssets("BOTTOM/") 

    data = {
        "assets": {
            "bgIndex": bgIndex,
            "topIndex": topIndex,
            "mIndex": mIndex,
            "bIndex": bIndex
        },
        "settings": {
            "width" : WIDTH,
            "height" : HEIGHT
        }
    }

    with open("data.json", "w") as write_file:
        json.dump(data, write_file)
    return "ok"

def read():
    with open("data.json", "r") as read_file:
        return json.load(read_file)
        

    
def random():
    data = read() 
    bgMax = data["assets"]["bgIndex"]
    tMax = data["assets"]["topIndex"]
    mMax = data["assets"]["mIndex"]
    bMax = data["assets"]["bIndex"]

    bgIndex = randint(0,bgMax)
    tIndex = randint(0,tMax)
    mIndex = randint(0,mMax)
    bIndex = randint(0,bMax)
    
    imgCode = "bg-{}_t-{}_m-{}_b-{}".format(bgIndex,tIndex,mIndex,bgIndex)
    return imgCode
    
#build()


def listAll():
    data = read() 
    bgMax = data["assets"]["bgIndex"]
    tMax = data["assets"]["topIndex"]
    mMax = data["assets"]["mIndex"]
    bMax = data["assets"]["bIndex"]

    #epmpty set
    codes = []

    i = 0
    while i <= bgMax:
        j = 0
        while j <= tMax:
            k = 0
            while k <= mMax:
                l = 0
                while l <= bMax:
                    codes.append("bg-{}_t-{}_m-{}_b-{}".format(i,j,k,l))
                    print("loop")
                    l+=1
                k +=1
            j+=1
        i+=1
    print(codes)
    return codes                    

    



# print(im.format, im.size, im.mode)
print("hej")
listAll()
# img_code = "a-001_t-001_m-001_b-001"
# im = generate(img_code)

# im.show()