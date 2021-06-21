import cv2
import difflib

####################
#All system
####################
def CalcImageHash(FileName):
    image = cv2.imread(FileName) #Read the picture
    resized = cv2.resize(image, (7,7), interpolation = cv2.INTER_AREA) #Reduce the picture 
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) #black and white format
    avg=gray_image.mean()
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)
    
    #Рассчитаем хэш
    _hash=""
    for x in range(7):
        for y in range(7):
            val=threshold_image[x,y]
            if val==255:
                _hash=_hash+"1"
            else:
                _hash=_hash+"0"
            
    return _hash
 
def CompareHash2(hash1,hash2):
    l=len(hash1)
    i=0
    count=0
    while i<l:
        if hash1[i]!=hash2[i]:
            count=count+1
        i=i+1
    return count

def srva(comphash):
    if comphash == 0:
        print("The pictures are identical")
    elif comphash >= 0 and comphash <= 5:
        print("There are small differences")
    else:
        print("The pictures differ almost completely")

###############
#End all system
###############

# Calculate
hash1 = CalcImageHash("screenshots/screen1.jpg")
hash2 = CalcImageHash("screenshots/screen2.jpg")
# End calculate

# First example
comparehashall = CompareHash2(hash1, hash2)
print(comparehashall)

srva(comparehashall) # 4 There are small differences
###############

# Second example
comparehashall = CompareHash2(hash1, hash1)
print(comparehashall)

srva(comparehashall) # 0 The pictures are identical
#################
