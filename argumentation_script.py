from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Training with explicit augmentation hyperparameters
results = model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    
# Example of data argumentation settings

    degrees=15.0,      # Rotation (± 15 degrees)
    scale=0.5,         # Scaling (zoom in/out)
    fliplr=0.5,        # Horizontal flip probability (50% chance)
    flipud=0.0,        # Vertical flip probability (0% for helmets since upside down doesn't make sense)
    hsv_s=0.7,         # Saturation (changes brightness/color intensity)
    hsv_v=0.4          # Value / Brightness adjustments
)
