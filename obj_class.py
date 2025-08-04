import cv2
import torch
from pathlib import Path
from utils.datasets import letterbox
from utils.general import non_max_suppression, scale_coords
from models.experimental import attempt_load

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = attempt_load("yolov7.pt", map_location=device)
model.eval()

# Load class names (COCO)
names = model.module.names if hasattr(model, "module") else model.names

# Open webcam
cap = cv2.VideoCapture(0)  # 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = letterbox(frame, new_shape=640)[0]
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3xHxW
    img = torch.from_numpy(img).float().div(255.0).unsqueeze(0).to(device)

    # Run inference
    with torch.no_grad():
        pred = model(img, augment=False)[0]
        pred = non_max_suppression(pred, 0.25, 0.45)

    # Draw boxes
    for det in pred:
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], frame.shape).round()
            for *xyxy, conf, cls in det:
                label = f"{names[int(cls)]} {conf:.2f}"
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0,255,0), 2)
                cv2.putText(frame, label, (int(xyxy[0]), int(xyxy[1]) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    cv2.imshow("YOLOv7 Real-Time", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
