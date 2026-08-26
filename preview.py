import os
import cv2
import xml.etree.ElementTree as ET

# ==================== CONFIGURATION ====================
IMG_DIR = "/home/ui/Downloads/Helmet_detection_data_set/images"
XML_DIR = "/home/ui/Downloads/Helmet_detection_data_set/annotations"
PREVIEW_DIR = "/home/ui/Downloads/Helmet_detection_data_set/previews"
# =======================================================

os.makedirs(PREVIEW_DIR, exist_ok=True)
xml_files = [f for f in os.listdir(XML_DIR) if f.endswith(".xml")]

print(f"Generating color-coded previews for {len(xml_files)} files...")

for xml_file in xml_files:
    base_name = os.path.splitext(xml_file)[0]
    xml_path = os.path.join(XML_DIR, xml_file)

    # Find matching image
    img_path = None
    for ext in [".png", ".jpg", ".jpeg", ".PNG", ".JPG"]:
        possible_img = os.path.join(IMG_DIR, f"{base_name}{ext}")
        if os.path.exists(possible_img):
            img_path = possible_img
            break

    if not img_path:
        continue

    img = cv2.imread(img_path)
    if img is None:
        continue

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for obj in root.findall("object"):
        raw_name = obj.find("name").text
        clean_name = raw_name.strip().lower()
        
        bndbox = obj.find("bndbox")
        xmin = int(float(bndbox.find("xmin").text))
        ymin = int(float(bndbox.find("ymin").text))
        xmax = int(float(bndbox.find("xmax").text))
        ymax = int(float(bndbox.find("ymax").text))

        # Choose color based on class name (BGR format)
        if "without" in clean_name or "no" in clean_name:
            box_color = (0, 0, 255)    # Red
        else:
            box_color = (0, 255, 0)    # Green (default for With Helmet, etc.)

        # Draw the rectangle and text
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), box_color, 2)
        cv2.putText(
            img, 
            raw_name, 
            (xmin, max(ymin - 10, 10)), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.6, 
            box_color, 
            2
        )

    preview_path = os.path.join(PREVIEW_DIR, f"{base_name}_preview.jpg")
    cv2.imwrite(preview_path, img)

print(f"Done! Check your preview folder: {PREVIEW_DIR}")