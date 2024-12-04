#import cv2
from time import sleep
import os
import socketio
from PIL import Image
SERVER_URL = "http://5.59.97.201:6969/"

# cam = cv2.VideoCapture("doom.mp4")
# image = Image.open("cd.png")
# width, height = image.size

# image = image.convert("RGBA")

sio = socketio.Client()
sio.connect(SERVER_URL)

dir = os.fsencode("h")

def update_pixel(x, y, r, g, b):
    response = sio.emit('updatePixel',
                             {
                                 "x": x,
                                 "y": y,
                                 "r": r,
                                 "g": g,
                                 "b": b
                             })
    # if response.status_code != 200:
    #     print(f"Failed to update pixel at ({x}, {y}): {response.text}")
def blit_image(image):
    for y in range(height):
        for x in range(width):
            try:
                pixel = image.getpixel((x, y))
                if isinstance(pixel, tuple) and len(pixel) == 4:
                    r,g,b,a = pixel
                    #print(pixel)
                    if a > 0: 
                        update_pixel(x, y +100, r, g, b)
                        sleep(0.0001)
                else:
                    print(f"Unexpected pixel format at ({x}, {y}): {pixel}")
            except Exception as e:
                print(f"Error processing pixel at ({x}, {y}): {e}")
    return

print("Finished updating the canvas!")
currentframe=1

while True:
    for file in os.listdir(dir):
        image = Image.open(os.path.join("h","out"+str(currentframe)+".png"))
        width, height = image.size
        image = image.convert("RGBA")
        print(currentframe)
        blit_image(image)
        sleep(1)
        currentframe+=1

   

