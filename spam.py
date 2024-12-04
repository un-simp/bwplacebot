from PIL import Image
import requests
import time
import socketio
SERVER_URL = "http://5.59.97.201:6969/"

image = Image.open("cd.png")
width, height = image.size

image = image.convert("RGBA")

sio = socketio.Client()
sio.connect(SERVER_URL)
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

while True:
    for y in range(height):
        for x in range(width):
            try:
                pixel = image.getpixel((x, y))
                if isinstance(pixel, tuple) and len(pixel) == 4:
                    r,g,b,a = pixel
                    print(pixel)
                    if a > 0: 
                        update_pixel(x, y +100, r, g, b)
                        #time.sleep(0.001)
                else:
                    print(f"Unexpected pixel format at ({x}, {y}): {pixel}")
            except Exception as e:
                print(f"Error processing pixel at ({x}, {y}): {e}")

print("Finished updating the canvas!")
