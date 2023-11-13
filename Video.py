import os
import cv2

path = "C:/Users/Aman/Documents/coding projects/Projects/Project 105/Images"
Images = []


for file in os.listdir(path):
    root,ext = os.path.splitext(file)
    
    if ext in (".png",".jpg",".gif",".jpeg",".jfif"):
        file_name = path+"/"+file

        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
height,width,channels = frame.shape
size = (width,height)
out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8 ,size)

for i in range(count,0):
    frame = cv2.imread(Images[i])
    out.write(frame)
    cv2.imshow("output",frame)
    if cv2.waitKey(100) == 32 :
            break
    
print("Done")


