import cv2 as cv
import numpy as np
from action import dispatch

class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None



    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):

        self.needle_img = needle_img_path

        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        self.method = method


    def find(self,device, scale_avg, haystack_img, threshold=0.5, debug_mode=None):


        result = cv.matchTemplate(haystack_img, self.needle_img, self.method)

        locations = np.where(result >= threshold)
        locations = list(zip(*locations[::-1]))
        #print(locations)

        rectangles = []
        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), self.needle_w, self.needle_h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=2, eps=0.5)

        points = []
        action_coordinates = []
        if len(rectangles):
            line_color = (0, 255, 0)
            line_type = cv.LINE_4
            marker_color = (255, 0, 255)
            marker_type = cv.MARKER_CROSS

            for (x, y, w, h) in rectangles:
                # print(f'VISION_X: {int(x /scale_avg)}  VISION_Y: {int(y/scale_avg)}')
                # print(f'VISION_W: {w} VISION_H: {h}')

                scale_x = int(x / scale_avg)
                scale_y = int(y / scale_avg)
                center_w = int(h/2)
                center_h = int(w/2)

                action_x = int(scale_x + center_w + 20)
                action_y = int(scale_y + center_h + 5)


                action_coordinates = f'{action_x} {action_y}'
                dispatch('tap', device, f'{action_coordinates}')
                         # action_coordinates.append((action_x,action_y))
                # print(f'FROM VIISSSSION====:   {action_coordinates}')

                print(f'FROM VISSSION____{action_coordinates}')


                center_x = x + int(w/2)
                center_y = y + int(h/2)

                # points.append((center_x, center_y))
                # print(self.action_coordinates)

                if debug_mode == 'rectangles':
                    # Determine the box position
                    top_left = (x, y)
                    bottom_right = (x + w, y + h)
                    # Draw the box
                    cv.rectangle(haystack_img, top_left, bottom_right, color=line_color,
                                lineType=line_type, thickness=20)
                elif debug_mode == 'points':
                    # Draw the center point
                    cv.drawMarker(haystack_img, (center_x, center_y),
                                color=marker_color, markerType=marker_type,
                                markerSize=20, thickness=2)
        # if debug_mode:

        cv.imshow(f'test', haystack_img)



            # [points] = points
            #cv.imwrite('result_click_point.jpg', haystack_img)
        # print(self.action_coordinates)

