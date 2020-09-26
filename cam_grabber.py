import requests
import time

# The Camera names/location and fixed image links are below
UDN = "http://ns-webcams.its.sfu.ca/public/images/udn-current.jpg?nocache=1&update=15000&timeout=1800000&offset=4"
AQPOND = "http://ns-webcams.its.sfu.ca/public/images/aqn-current.jpg?nocache=1&update=15000&timeout=1800000"
SUB = "http://ns-webcams.its.sfu.ca/public/images/aqsw-current.jpg?nocache=0.3346598630889852&update=15000&timeout=1800000"
TFF = "http://ns-webcams.its.sfu.ca/public/images/terryfox-current.jpg?nocache=1&update=15000&timeout=1800000"
GAGLARDI = "http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg?nocache=0.8678792633247998&update=15000&timeout=1800000&offset=4"
TRS = "http://ns-webcams.its.sfu.ca/public/images/towers-current.jpg?nocache=0.9550930672504077&update=15000&timeout=1800000"
TRN = "http://ns-webcams.its.sfu.ca/public/images/towern-current.jpg?nocache=1&update=15000&timeout=1800000"


# Camera you want to grab the images from
active_name = "AQPOND"
active_cam = AQPOND

# Initialising grabber
print("-- Initilising " + active_name + " Cam Grabber --")
counter = 0

while True:
    print("Grabbing " + active_name + " Image# " + str(counter))
    img = requests.get(active_cam)
    down_img = open("./" + active_name + "/" + str(counter) + ".jpeg", "wb")
    down_img.write(img.content)
    down_img.close()
    counter += 1
    time.sleep(10)
