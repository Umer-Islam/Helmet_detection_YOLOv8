import os
import xml.etree.ElementTree as ET

# ==================== CONFIGURATION ====================
XML_DIR = "/home/ui/Downloads/Helmet_detection_data_set/annotations"  # Update with your actual path
OUTPUT_DIR = "/home/ui/Downloads/Helmet_detection_data_set/txt_outputs"

CLASSES = ["With Helmet"]
# =======================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

xml_files = [f for f in os.listdir(XML_DIR) if f.endswith(".xml")]
print(f"Total XML files found in directory: {len(xml_files)}")

for xml_file in xml_files:
    xml_path = os.path.join(XML_DIR, xml_file)
    base_name = os.path.splitext(xml_file)[0]
    txt_path = os.path.join(OUTPUT_DIR, f"{base_name}.txt")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Debug size
    size = root.find("size")
    if size is None:
        print(f"[{xml_file}] ERROR: Missing <size> tag")
        continue

    width = int(size.find("width").text)
    height = int(size.find("height").text)

    yolo_lines = []
    objects = root.findall("object")
    print(f"[{xml_file}] Found {len(objects)} object(s) in XML.")

    for obj in objects:
        name_elem = obj.find("name")
        if name_elem is None:
            print(f"  -> Object missing <name> tag")
            continue
        
        raw_name = name_elem.text
        cleaned_name = raw_name.strip().lower()
        print(f"  -> Read class name: '{raw_name}' (cleaned: '{cleaned_name}')")

        lower_classes = [c.lower() for c in CLASSES]
        if cleaned_name not in lower_classes:
            print(f"  -> MISMATCH! '{cleaned_name}' is not in allowed classes: {lower_classes}")
            continue

        class_id = lower_classes.index(cleaned_name)
        
        bndbox = obj.find("bndbox")
        xmin = float(bndbox.find("xmin").text)
        ymin = float(bndbox.find("ymin").text)
        xmax = float(bndbox.find("xmax").text)
        ymax = float(bndbox.find("ymax").text)

        # Normalize
        x_center = ((xmin + xmax) / 2.0) / width
        y_center = ((ymin + ymax) / 2.0) / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

    if yolo_lines:
        with open(txt_path, "w") as f:
            f.write("\n".join(yolo_lines))
        print(f"  -> Successfully wrote {len(yolo_lines)} line(s) to {txt_path}\n")
    else:
        print(f"  -> WARNING: No valid objects matched, leaving/making file empty.\n")