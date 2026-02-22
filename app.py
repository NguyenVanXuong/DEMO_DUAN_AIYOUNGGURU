import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="AI Cảnh Báo Đường Sắt", layout="wide")

st.title("🚆 HỆ THỐNG CẢNH BÁO AN TOÀN ĐƯỜNG SẮT (YOLOv8)")

# Load model
@st.cache_resource
def load_model():
    model = YOLO("yolov8n.pt")  # model nhẹ, chạy được trên Streamlit Cloud
    return model

model = load_model()

uploaded_file = st.file_uploader("📤 Tải ảnh lên", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_np = np.array(image)

    st.image(image, caption="Ảnh gốc", use_column_width=True)

    # Detect
    results = model(img_np)

    annotated_frame = results[0].plot()

    st.subheader("📌 Kết quả nhận diện")
    st.image(annotated_frame, caption="Ảnh sau khi nhận diện", use_column_width=True)

    # Phân tích mức độ nguy hiểm
    detected_objects = []

    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        detected_objects.append(label)

    st.write("### 🧾 Danh sách vật thể phát hiện:")
    st.write(detected_objects)

    # Logic cảnh báo
    warning_level = "An toàn"
    color = "green"

    if "person" in detected_objects:
        warning_level = "⚠️ CẢNH BÁO TRUNG BÌNH"
        color = "orange"

    if "car" in detected_objects or "truck" in detected_objects or "bus" in detected_objects:
        warning_level = "🚨 NGUY HIỂM CAO"
        color = "red"

    if "train" in detected_objects:
        warning_level = "🛑 DỪNG KHẨN CẤP"
        color = "darkred"

    st.markdown(f"## <span style='color:{color}'>{warning_level}</span>", unsafe_allow_html=True)
