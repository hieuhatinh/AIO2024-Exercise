# -*- coding: utf-8 -*-
"""open_vocab_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z0OgJiyv43dZ91aDZFm4hXKXVFcVDy3s

### Import các thư viện cần thiết
"""

from ultralytics import YOLOWorld
from ultralytics.engine.results import Boxes

from src.utils import save_detection_results

"""### Khởi tạo mô hình YOLO-World"""

# Initialize a YOLO-World model
model = YOLOWorld("yolov8s-world.pt")

"""### Định nghĩa các lớp tùy chỉnh"""

# Define custom classes
model.set_classes(["bus"]) # <--------- Change this to the class you want to detect

"""### Thực hiện dự đoán trên một hình ảnh"""

# Execute prediction on an image
results: Boxes = model.predict("bus.jpg")

"""### Lưu kết quả phát hiện đối tượng"""

# Save detection results as images
save_detection_results(results)