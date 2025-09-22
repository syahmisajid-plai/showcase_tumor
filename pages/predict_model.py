import streamlit as st
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from tensorflow.keras.models import load_model

# =====================
# Custom CSS
# =====================
st.markdown(
    """
<style>
.stApp {
    background-color: #121826;
    color: white;
    font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
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
h1 {
    font-size: 2.5em !important;
    text-align: center;
    margin-bottom: 1rem;
    color: #00BFA6;
}
h4 {
    color: #E0E0E0;
    margin-top: 1.5rem;
}
.upload-box {
    background-color: #1E1E2F;
    padding: 1rem;
    border-radius: 10px;
    border: 1px dashed #00BFA6;
}
</style>
""",
    unsafe_allow_html=True,
)


# =====================
# App Title
# =====================
def about_predict():
    st.title("🧬 Klasifikasi Tumor Gambar")
    # Custom CSS
    st.markdown(
        """
        <style>
        .upload-section {
            background-color: #1E1E2F;
            padding: 1.5rem;
            border-radius: 12px;
            border: 2px dashed #00BFA6;
            margin-bottom: 0.5rem;
        }
        .upload-section h4 {
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: #00BFA6;
            font-size: 20px;
        }
        section[data-testid="stFileUploader"] {
            margin-top: -1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Upload section markup
    st.markdown(
        '<div class="upload-section"><h4>📤 Unggah Gambar MRI Otak Anda di bawah ini: 👇👇👇 </h4></div>',
        unsafe_allow_html=True,
    )

    with st.expander("📤 Klik untuk unggah gambar MRI"):
        uploaded_file = st.file_uploader(
            "Pilih file gambar",
            type=["jpg", "png", "jpeg"],
            label_visibility="collapsed",
        )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # st.image(image, caption="🖼️ Gambar yang Anda unggah", use_container_width=True)
        # Tampilkan gambar
        col1, col2, col3 = st.columns([1, 2, 1])  # Kolom tengah lebih lebar

        with col2:
            st.image(image, width=400)

        with st.expander("📋 Detail Gambar"):
            st.write("Dimensi:", image.size)
            st.write("Format:", image.format)

        with st.spinner("🔎 Sedang memproses dan memprediksi..."):
            # Load model
            model = load_model(
                "googlenet_savedmodel", custom_objects={"KerasLayer": hub.KerasLayer}
            )
            infer = model.signatures["serving_default"]

            class_names = np.array(["No Tumor", "Glioma", "Meningioma", "Pituitary"])

            def preprocess_image(image, img_shape=299):
                image = image.convert("RGB")
                image = image.resize((img_shape, img_shape))
                img_array = np.array(image) / 255.0
                return img_array

            def predict_class(image, infer, class_names):
                image_array = preprocess_image(image)
                image_array = np.expand_dims(image_array, axis=0).astype(np.float32)
                input_name = list(infer.structured_input_signature[1].keys())[0]
                prediction = infer(**{input_name: tf.constant(image_array)})
                prediction = list(prediction.values())[0].numpy()
                predicted_class = class_names[np.argmax(prediction)]
                confidence = np.max(prediction)
                return predicted_class, confidence

            pred_class, confidence = predict_class(image, infer, class_names)

        # =====================
        # Display Result
        # =====================
        st.markdown("## 🧠 Hasil Prediksi")

        if pred_class == "No Tumor":
            st.success(
                f"🟢 {pred_class} — Tidak ditemukan indikasi tumor.\n\nConfidence: {confidence:.2%}"
            )
        elif pred_class == "Glioma":
            st.warning(
                f"🔵 {pred_class} — Kemungkinan tumor jenis glioma.\n\nConfidence: {confidence:.2%}"
            )
        elif pred_class == "Meningioma":
            st.warning(
                f"🟣 {pred_class} — Kemungkinan tumor jenis meningioma.\n\nConfidence: {confidence:.2%}"
            )
        elif pred_class == "Pituitary":
            st.error(
                f"🟠 {pred_class} — Kemungkinan tumor pituitary.\n\nConfidence: {confidence:.2%}"
            )
        else:
            st.info(
                f"❓ {pred_class} — Kelas tidak dikenali.\n\nConfidence: {confidence:.2%}"
            )

        # Footer
        st.markdown(
            """
            <hr style="border:1px solid #FFD700; margin-top:40px;">
            <p style="text-align:center; color:#888;">❤️ Politeknik Artificial Intelligence ❤️</p>
        """,
            unsafe_allow_html=True,
        )


# Menjalankan aplikasi prediksi
about_predict()
