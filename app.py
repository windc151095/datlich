import streamlit as st
import google.generativeai as genai

# 1. Cấu hình chìa khóa (Thay bằng Key bạn lấy ở mục "Get API key")
genai.configure(api_key="KEY_CỦA_BẠN")

# 2. Định nghĩa "Tính cách/Chỉ dẫn" cho AI
# Bạn hãy copy nội dung trong ô "System Instructions" của bạn dán vào đây
SYSTEM_INSTRUCTION = """
Bạn là một chuyên gia về tâm thức... (Dán nội dung của bạn vào đây)
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_INSTRUCTION
)

# 3. Tạo giao diện Web
st.title("Ứng dụng của Chất")
input_text = st.text_input("Gửi câu hỏi hoặc chia sẻ của bạn:")

if st.button("Trò chuyện"):
    response = model.generate_content(input_text)
    st.write(response.text)