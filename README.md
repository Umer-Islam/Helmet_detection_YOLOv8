# notes + checklist + Project structure


## How to run the project
1. setup .venv
2. install dependencies from requirements.txt file
3. run the python scripts


---
## notes

- dataset of 764 images was initially annotated in pascal VOC (.xml) format, it was converted to .txt format for yolov8 using xml_to_txt.py script.

- run the preview.py script to view the annotated images, it will create a director with labelled images(please setup a venv and add the dependencies from requirements.txt file before running this script).

-  the argumentation can be done while training the model, please see argumentation_script.py for example.

---
## Checklist
Automated Helmet detection system using deep learning
– Prototype Assignment
Tasks
You have to perform the following tasks.
###    1. Data Collection & Preprocessing:
- [x] Use a helmet detection dataset. (done)
- [x]  Include images of people wearing helmets and not wearing helmets. (done)
- [x]  Convert dataset into YOLO format (images + label files). (done, convereted .xml annotations to .txt)
- [x]  Resize and normalize images.(Yolov8 handling normalization automatically )[https://docs.ultralytics.com/guides/preprocessing-annotated-data]
- [x]  Apply data augmentation (flip, rotation, brightness, scaling).(done while training)

---
## Project Structure

The repository is organized as follows:

```text
Helmet_detection_data_set/
│
├── annotations/            # Raw Pascal VOC annotation files (.xml)
├── images/                 # Raw dataset image files both with and without helmets (.jpg / .png)
├── txt_outputs/            # Converted YOLO format annotation files (.txt)
│
├── xml_to_txt.py           # Script to parse XML files and convert bounding boxes to YOLO .txt format
├── preview.py              # Visualization script to draw color-coded bounding boxes on images(this will create a new directory)
├── argumentation_script.py # Data augmentation script to be includded while training (flips, rotations, brightness, scaling)
│
├── requirements.txt        # Required Python packages (opencv-python, ultralytics, etc.)
├── README.md               # Project documentation and setup instructions
├── .gitignore              # Git ignore configuration file
└── .venv/                  # Python local virtual environment (untracked)