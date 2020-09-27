import requests
import keyboard
from time import sleep
from datetime import datetime
from os import path, mkdir, startfile

print("----- Initialising Timeplase Script -----")

# The Camera names/location and fixed image links
UDN = "http://ns-webcams.its.sfu.ca/public/images/udn-current.jpg?nocache=1&update=15000&timeout=1800000&offset=4"
AQPOND = "http://ns-webcams.its.sfu.ca/public/images/aqn-current.jpg?nocache=1&update=15000&timeout=1800000"
SUB = "http://ns-webcams.its.sfu.ca/public/images/aqsw-current.jpg?nocache=0.3346598630889852&update=15000&timeout=1800000"
TFF = "http://ns-webcams.its.sfu.ca/public/images/terryfox-current.jpg?nocache=1&update=15000&timeout=1800000"
GAGLARDI = "http://ns-webcams.its.sfu.ca/public/images/gaglardi-current.jpg?nocache=0.8678792633247998&update=15000&timeout=1800000&offset=4"
TRS = "http://ns-webcams.its.sfu.ca/public/images/towers-current.jpg?nocache=0.9550930672504077&update=15000&timeout=1800000"
TRN = "http://ns-webcams.its.sfu.ca/public/images/towern-current.jpg?nocache=1&update=15000&timeout=1800000"


# Camera to grab the images from
active_cam = TFF
active_name = "TFF"


# Initialising grabber
print("----- Initilising " + active_name + " Cam Grabber -----")
counter = 0


grabber_status = True
while grabber_status:

    # Checking if the folder path exists
    folder_path = "./" + active_name + "/"
    if (not(path.exists(folder_path))):
        mkdir(folder_path)

    # Grabbing the images from SFU website
    print("Grabbing " + active_name + " Image# " + str(counter))
    temp_img = requests.get(active_cam)

    while (not(temp_img.content)):
        if (grabber_status):
            print("----- Requested " + active_name + " SFU cam is down -----")

            # If cam down, delay for grabber to reconnect
            time_grab_reconnect = 5
            time_last_grab = 0
            while (time_last_grab <= time_grab_reconnect):
                if keyboard.is_pressed('esc+q'):
                    print("----- Terminating Cam Grabber Script -----")
                    grabber_status = False
                    break

                time_last_grab += 0.1
                sleep(0.1)

            temp_img = requests.get(active_cam)
        else:
            break

    if (not(grabber_status)):
        break

    # Dowloading images locally
    cur_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    img = open(folder_path + cur_time + ".jpeg", "wb")
    img.write(temp_img.content)
    img.close()
    counter += 1

    # Delay for the next grab (in seconds)
    time_grab_delay = 10.0

    # Waiting for the next grab or until keyboard interrupt
    time_last_grab = 0
    while (time_last_grab <= time_grab_delay):
        if keyboard.is_pressed('esc+q'):
            print("----- Terminating Cam Grabber Script -----")
            grabber_status = False
            break

        time_last_grab += 0.1
        sleep(0.1)


while True:
    user_inp = input("--> Start Timelapse Vid Stitcher?(Y/N):")
    if ((user_inp == 'Y') | (user_inp == 'y')):
        print("----- Initilising Vid Stitcher -----")
        startfile("vid_stitch.bat")
        print("----- Timeplase Vid Completed -----")
        break

    elif ((user_inp == 'N') | (user_inp == 'n')):
        print("----- Terminating Timeplase Script -----")
        break

    else:
        print("---> Incorrect input, Please Try Again")
