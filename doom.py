from time import sleep
import os
import socketio
from PIL import Image
SERVER_URL = "http://5.59.97.201:6969/"


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
def blit_image(image):
    for y in range(height):
        for x in range(width):
            try:
                pixel = image.getpixel((x, y))
                if isinstance(pixel, tuple) and len(pixel) == 4:
                    r,g,b,a = pixel
                    if a > 0: 
                        update_pixel(x, y +100, r, g, b)
                        sleep(0.05)
                else:
                    print(f"Unexpected pixel format at ({x}, {y}): {pixel}")
            except Exception as e:
                file = open("errors","+a")
                file.write(f"Error processing pixel at ({x}, {y}): {e}")
                file = None
                print(f"Error processing pixel at ({x}, {y}): {e}")
    return

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

   

