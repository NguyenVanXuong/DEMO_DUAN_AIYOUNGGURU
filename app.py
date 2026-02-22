import streamlit as st
from openai import OpenAI
import base64
import json

# --- Cấu hình trang ---
st.set_page_config(page_title="AI Cảnh Báo Đường Sắt", layout="centered")

st.title("🚆 HỆ THỐNG CẢNH BÁO NGUY HIỂM ĐƯỜNG SẮT (DEMO)")
st.write("Tải ảnh hiện trường đường ray để hệ thống AI phân tích mức độ nguy hiểm.")

# --- Nhập API key ---
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# --- Upload ảnh ---
uploaded_file = st.file_uploader("Tải ảnh lên", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image_bytes = uploaded_file.read()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    st.image(uploaded_file, caption="Ảnh đã tải lên", use_column_width=True)

    with st.spinner("AI đang phân tích..."):

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """Bạn là hệ thống cảnh báo an toàn đường sắt.
Phân tích hình ảnh và trả về JSON theo cấu trúc:
{
  "muc_canh_bao": "Thap/Trung binh/Cao/Khan cap",
  "loai_nguy_hiem": "...",
  "ly_do": "...",
  "de_xuat": "..."
}"""
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Phân tích mức độ nguy hiểm."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=500,
        )

        result = response.choices[0].message.content

    st.subheader("📊 Kết quả phân tích:")
    st.write(result)
