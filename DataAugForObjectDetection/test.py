import os
imgs_path='./VOC2007/JPEGImages'
scale=3
for parent, _, files in os.walk(imgs_path):
    pass

print(parent)
print(_)
print(files)

# aug_num = scale * len(files)
#
# path=parent
#
# a=aug_num
# print(a)
# print(path)

