// app_position 475 180
// mq_position = 947 , 237
// skip_position = 1120, 53

Progression:
    -- Include Case and Switch to handle actions.
            - make module for Action
            - make module for image path

    -- Include concurrent.future -> in main & action module




    --Get official tap position vs pointer location

            prev_sqpx = aW x aH (type int) <-- the dimension of the window size at time the image was taken
            curr_sqpx = bW x bH (type int) <-- new dimension

            scale_w = adjusted_W / previous_W
            scale_h = adjusted_H / previous_H
            scale_avg = ( scale_w + scale_h) / 2

            final_sqPx = scale_avg * previous_SqPx

            final_w = final_sqPx / h
            final_h = final_sqPx / w

            new_img_dimension = final_w , final_h

            resolution scale =  sqpx_after / sqpx_before

            

            W: 1280  , H: 720 <-- Initial Res @ the time Image was taken

            VISION_X: 443  VISION_Y: 168  <-- recognized image location x y

            VISION_W: 64 VISION_H: 59 <---- size of the image






            scale resolution = // capw



            a/b = c


            pointer location = cW -










    1) refactor img path to be in its own component
        1B) import it to main to call on Assign_Device as device [COMPLETED]

    2) give Assign Device an argument for img_path [COMPLETED]






//  autopy2lon
//  create image recognition to automate incidents on multiple android devices simultaneously 

still to do:
    -refactor and organize, move logic from main to new component, -vision class[]

//============  MVP:  ============//
//  -as a user ~I want to be able to fully automate actions within an android device
    * use opencv to for image recognition
    * find position of the image in opencv capture, and print position 
    * convert position of opencv resolution to adb resolution
    * use position to make actions through adb shell

//  -as a user ~I want to see the progress and actions that is being made as the program is making them
    * use terminal to print actions verbosely
       * print what image is found
       * print image recognition threshold & confidence
       * print actions if that image is found
       * print (errors)

//  -as a user ~I want to be able to automate these tasks without having to sacrifice my mouse and keyboard so I that I can do something else while it is running
    * use adb shell to make these actions virtually
       * get position of the image
       * shell to call action taps to android adb device(s) 

//  -as a user ~I want to I want to automate these tasks without any strain toward my cpu and its memory
(most strains come from the emulator and the applications that the emulator is running on)
    * separate actions and functions to be made only on specialized occasions instead of looping endlessly
    * attempt to test run and make actions through headless -no-window call through adb
      


//============  SVP:  ============//
// -Make Simultaneous actions calls to multiple adb
    * for loop to connect adb


// -Run ADB in headless to reduce cpu usage, but still functioning through openCV
