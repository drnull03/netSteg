from PIL import Image
import numpy as np




MAGIC='NETICO'

def Encode(src,msg):
    msg=msg+MAGIC
    if(msg=="" or msg=="" or src==""):
        return
    

    img=Image.open(src,"r")
    width, height = img.size
    array = np.array(list(img.getdata()))
    b_message = ''.join([format(ord(i), "08b") for i in msg])
    #print(b_message)
    req_pixels=len(b_message)
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    pixels=array.size//n


    #check if we have enough space to encode the message
    if(req_pixels>=pixels):
        print("error not enough space to encode message please use a larger image or a smaller image")
        return
    index=0
    for i in range(pixels):
        if(index<req_pixels):
            
            array[i][2]=int((bin(array[i][2]))[2:-1]+b_message[index])
            index += 1
        else:break
    array=array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save("_"+src)
    print("Image Encoded Successfully")


def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))


    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    pixels = array.size//n
    hidden_bits = ""
    for i in range(pixels):
            hidden_bits += (bin(array[i][2])[-1])
           #print(bin(array[i][2])[-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    hiddenmessage = ""
    for i in range(len(hidden_bits)):
        message += chr(int(hidden_bits[i], 2))
        message = f'{message}'
        hiddenmessage = message
    print("the hidden message is")
    print(hiddenmessage[0:hiddenmessage.find(MAGIC)])




def main():
    print("hello what do you want to do?")
    print("1 is for encode and 2 is for decode")
    inp = input()

    if inp == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = input()
        print("Encoding...")
        Encode(src, message)

    elif inp == '2':
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        Decode(src)

    else:
        print("ERROR: Invalid option chosen")

main()