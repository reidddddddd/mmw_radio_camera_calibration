# from exif import Image
#
# # with open('testData/1.png', 'rb') as image_file:
#
# my_image = Image('testData/1.png')
#
# print(my_image.list_all())】
import cv2
import pyexifinfo as p
import json

videoCapture = cv2.VideoCapture()

def save_image(image,addr,num):
  address = addr + str(num)+ '.jpg'
  cv2.imwrite(address,image)
#读帧
success, frame = videoCapture.read()
i = 0
while success :
  i = i + 1
  save_image(frame,'./output/image',i)



p.ver()
data = p.get_json("testData/image1.jpg")
print( json.dumps(data, sort_keys=True,
                  indent=4, separators=(',', ': ')) )
