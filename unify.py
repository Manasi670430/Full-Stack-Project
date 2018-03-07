import urllib.request
contents = urllib.request.urlopen("https://www.random.org/integers/?num=1&min=120000000&max=160000000&col=1&base=10&format=plain&rnd=new").read()
bitmap=[]     #Declared a list to store 128*128 Bitmap Image
bitmapLine=[] #Declared a list to store One line of Bitmap Image
apiNumber=int(contents) 
for j in range(0,128):
    for i in range(0,128):
        if(int(apiNumber)<=0):
            contents = urllib.request.urlopen(
                "https://www.random.org/integers/?num=1&min=120000000&max=16000000&col=1&base=10&format=plain&rnd=new").read()  #GET API call
            apiNumber = float(contents)
#Getting RGB values from the random numbers
        r=str(int(apiNumber%255))  
        apiNumber=apiNumber/255
        g = str(int(apiNumber%255))
        apiNumber = apiNumber/ 255
        b = str(int(apiNumber%255))
        apiNumber = apiNumber/ 255
        rgb=r+","+g+","+b
        bitmapLine.append(rgb)   //storing the RGB values in the (R,G,B) format
    bitmap.append(bitmapLine)
    bitmapLine=[]
print(bitmap)
