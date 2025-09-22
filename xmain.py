# env\Scripts\activate

import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt

# =====================
# Setup Streamlit
# =====================
st.set_page_config(page_title="🧬 Klasifikasi Tumor Gambar", layout="wide")

# =====================
# Custom CSS
# =====================
st.markdown(
    """
<style>
.block-container {
    max-width: 1000px;
    padding-top: 1rem;
    padding-bottom: 2rem;
    margin-top: 5rem;
    margin-left: auto;
    margin-right: auto;
}
.stApp {
    background-color: #121826;
    color: white;
}
.stButton>button {
    color: white;
    background-color: #00BFA6;
    border-radius: 8px;
    padding: 0.5em 1em;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #008C7E;
}
.title {
    font-size: 3em;
    text-align: center;
    margin-bottom: 1rem;
}
label, input, textarea {
    color: white !important;
    background-color: #1E1E2F !important;
}
::placeholder {
    color: #ccc !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# =====================
# Judul Aplikasi
# =====================
st.markdown(
    '<div class="title">🧬 Klasifikasi Tumor dari Gambar</div>', unsafe_allow_html=True
)
st.markdown(
    "Prediksi jenis tumor berdasarkan citra medis menggunakan model klasifikasi berbasis CNN."
)

# =====================
# Load Model
# =====================
try:
    model = load_model("googlenet_model.h5")
    st.success("✅ Model klasifikasi berhasil dimuat!")
except Exception as e:
    st.error(f"⚠️ Model belum tersedia atau gagal dimuat: {e}")
    st.stop()


# =====================
# Fungsi Preprocessing
# =====================
def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# =====================
# Upload Gambar
# =====================
st.header("📂 Upload Gambar Tumor")
uploaded_file = st.file_uploader(
    "Unggah gambar tumor (jpg/png)", type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Gambar yang diunggah", use_column_width=True)

    # Preprocessing dan Prediksi
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0]

    # Jika model output berupa probabilitas
    class_names = ["Tumor Jinak", "Tumor Ganas"]
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    st.success(f"🎯 Jenis Tumor: **{predicted_class}**")
    st.info(f"📊 Keyakinan Model: **{confidence:.2f}%**")

    # Visualisasi Probabilitas
    fig, ax = plt.subplots()
    ax.bar(class_names, prediction, color=["#00BFA6", "#FF6B6B"])
    ax.set_ylabel("Probabilitas")
    ax.set_title("Distribusi Prediksi")
    st.pyplot(fig)
