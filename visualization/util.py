import cv2

def draw_points_on_picture(picture_dir:str, points, out_dir):
    point_size = 1
    point_color = (0, 0, 255)  # BGR
    thickness = 4  # 0 、4、8
    image = cv2.imread("picture_dir")
    for coor in points:
        cv2.circle(image, (int(coor[0]), int(coor[1])), point_size, point_color, thickness)

    cv2.imwrite('out_dir', image, [int(cv2.IMWRITE_JPEG_QUALITY), 95])