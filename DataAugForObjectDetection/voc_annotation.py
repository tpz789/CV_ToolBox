import xml.etree.ElementTree as ET
import os


def convert_annotation(xml_id, list_file):
    in_file = open('./VOC2007/Annotations/{}.xml'.format(xml_id), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text),
             int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


if __name__ == '__main__':

    classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", \
               "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", \
               "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    wd = os.getcwd()

    xmlfilepath = './VOC2007/Annotations'
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)

    for i in range(num):
        total_xml[i] = total_xml[i][:-4]

    with open('train.txt', 'w', encoding='utf-8') as list_file:
        for xml_id in total_xml:
            list_file.write('{}/VOC2007/JPEGImages/{}.jpg'.format(wd, xml_id))
            convert_annotation(xml_id, list_file)
            list_file.write('\n')
