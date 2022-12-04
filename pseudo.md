// app_position 475 180
// mq_position = 947 , 237
// skip_position = 1120, 53

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
