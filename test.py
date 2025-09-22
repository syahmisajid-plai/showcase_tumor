import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import InputLayer
import tensorflow as tf
import tensorflow_hub as hub

st.title("🔍 Cek Load Model H5")

try:
    # Memuat model dari file .keras
    model = load_model(
        "googlenet_savedmodel",
        custom_objects={"KerasLayer": hub.KerasLayer, "InputLayer": InputLayer},
        compile=False,
    )
    st.success("✅ Model berhasil dimuat!")
except Exception as e:
    st.error(f"⚠️ Gagal memuat model: {e}")
