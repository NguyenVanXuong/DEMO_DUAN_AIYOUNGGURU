import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import os

st.set_page_config(page_title="Hệ thống thị giác máy tính thời gian thực hỗ trợ điều hành an toàn và tối ưu chạy tàu trên mạng lưới Đường sắt Việt Nam", layout="wide")

st.title("Hệ thống thị giác máy tính thời gian thực hỗ trợ điều hành an toàn và tối ưu chạy tàu trên mạng lưới Đường sắt Việt Nam")

# Load API key
#genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

#model = genai.GenerativeModel("gemini-pro-vision")

uploaded_file = st.file_uploader("Tải một khung hình được cắt ra từ video của camera hành trình được gắn trên đầu máy xe lửa", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # image = Image.open(uploaded_file)
    # st.image(image, caption="Ảnh gốc", use_column_width=True)

    # prompt = """
    # Bạn là hệ thống AI cảnh báo an toàn đường sắt.

    # Phân tích ảnh và cho biết:
    # 1. Có người, xe, vật cản, gia súc trên đường ray không?
    # 2. Có tình huống nguy hiểm không?
    # 3. Mức cảnh báo: An toàn / Trung bình / Nguy hiểm cao / Dừng khẩn cấp.

    # Trả lời ngắn gọn, rõ ràng.
    # """

    # response = model.generate_content([prompt, image])

    st.subheader("Kết quả phân tích:")
    st.write("HỆ THỐNG HIỆN TẠI CẦN THU THẬP THÊM RẤT NHIỀU DỮ LIỆU ĐỂ DỰ ĐOÁN CHÍNH XÁC HƠN")
