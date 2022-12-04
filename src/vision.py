# import cv2 as cv
# import numpy as np


# class Vision:

#     def __init__(self, img_path, method=cv.TM_CCOEFF_NORMED):
#         self.img = cv.imread(img_path, cv.IMREAD_UNCHANGED)

#         self.img_w = self.img.shape[1]
#         self.img_h = self.img.shape[0]

#         self.method = method

#     def find(self, img, threshold=0.8, debug=None):
#         result = cv.matchTemplate(img, self.img, cv.TM_CCOEFF_NORMED)
#         print(result)

#         locations = np.where(result >= threshold)
#         locations = list(zip(*locations[::-1]))
#         print(locations)


#         rectangles = []
#         for loc in locations:
#             rect = [int(loc[0]), int(loc[1]), self._w, self._h]
#             rectangles.append(rect)
#             print(rectangles)


#     def get_input_positions(self, rectangles):
#         points = []

#         for (x, y, w, h) in rectangles:
#             center_x = x + int(w/2)
#             center_y = y + int(h/2)
#             points.append((center_x, center_y))

#         return points

#     def draw_rectangles(self, img, rectangles):
#         line_color = (0, 255, 0)
#         line_type = cv.LINE_4

#         for (x, y, w, h) in rectangles:
#             top_left = (x, y)
#             bottom_right = (x + w, y + h)
#             cv.rectangle(img, top_left, bottom_right, line_color, lineType=line_type)

#         return img

#     def draw_crosshairs(self, img, points):
#         marker_color = (255, 0, 255)
#         marker_type = cv.MARKER_CROSS

#         for (center_x, center_y) in points:
#             cv.drawMarker(img, (center_x, center_y), marker_color, marker_type)

#         return img

#     def centeroid(self, point_list):
#         point_list = np.asarray(point_list, dtype=np.int32)
#         length = point_list.shape[0]
#         sum_x = np.sum(point_list[:, 0])
#         sum_y = np.sum(point_list[:, 1])
#         return [np.floor_divide(sum_x, length), np.floor_divide(sum_y, length)]