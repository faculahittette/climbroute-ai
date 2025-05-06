"""Fine‑tunes YOLOv8 on custom dataset of climbing holds."""
from ultralytics import YOLO

if __name__ == "__main__":
    data_yaml = "data/holds.yaml"  # create with train/val splits
    model = YOLO("yolov8n.pt")     # tiny backbone
    model.train(data=data_yaml, epochs=30, imgsz=640, patience=10)
    model.export(format="onnx")
