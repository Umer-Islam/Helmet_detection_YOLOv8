# structure of the project + checklist

---
## structure of the project

dataset of 764 images was initially annotated in pascal VOC (.xml) format, it was converted to .txt format for yolov8 using xml_to_txt.py script.

run the preview.py script to view the annotated images, it will create a director with labelled images(please setup a venv and add the dependencies from requirements.txt file before running this script)


---
## Checklist
Automated Helmet detection system using deep learning
– Prototype Assignment
Tasks
You have to perform the following tasks.
    1. Data Collection & Preprocessing:
- [x] Use a helmet detection dataset. (done)
- [x]  Include images of people wearing helmets and not wearing helmets. (done)
- [x]  Convert dataset into YOLO format (images + label files). (done, convereted .xml annotations to .txt)
- []  Resize and normalize images.(Yolov8 handling normalization automatically )[https://docs.ultralytics.com/guides/preprocessing-annotated-data]
- []  Apply data augmentation (flip, rotation, brightness, scaling).(how do i do this)
