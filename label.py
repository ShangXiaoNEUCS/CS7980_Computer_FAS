
#Create label folder containing labels for each images

import os
#parent_dir = os.path.dirname(os.path.realpath(__file__))
dir = "/Users/zongruiliu/Downloads/fasdataset/train/labelTxt"
import os


image_list = os.listdir(dir)
org_dic = {"device":0,"photo":3,"live":1,"mask":2}
filename_list = list()
for i in image_list:
    filename_list.append(i)
#print(filename_list)


width = 640
height = 640

for r in filename_list:
    x_center = []
    y_center = []
    x = []
    y = []
    obj = []

    with open("/Users/zongruiliu/Downloads/fasdataset/train/labelTxt/{f}".format(f=r)) as file:
        for line in file:
            tmp = line.rstrip().split(" ")    
            x_center.append(((int(tmp[0])+int(tmp[2]))/2)/(width))
            y_center.append(((int(tmp[1])+int(tmp[5]))/2)/(height))
            x.append((int(tmp[2])-int(tmp[0]))/width)
            y.append((int(tmp[5])-int(tmp[1]))/height)
            obj.append(org_dic[tmp[-2]])

    with open("/Users/zongruiliu/Downloads/fasdataset/label/{z}".format(z=r),"w") as f:
        for i in range(len(obj)):
            f.write(str(obj[i])+" ")
                
            f.write(str(x_center[i])+" ")
            f.write(str(y_center[i])+" ")
            f.write(str(x[i])+" ")
            f.write(str(y[i]))
            f.write("\n")
            if i==len(obj)-1:
                break

