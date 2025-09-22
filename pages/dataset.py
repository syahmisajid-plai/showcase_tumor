import streamlit as st

# Inject custom CSS
st.markdown(
    """
    <style>
    /* Fade-in and slide-in animation */
    @keyframes slideIn {
        from {transform: translateY(20px); opacity: 0;}
        to {transform: translateY(0); opacity: 1;}
    }

    .stApp {
        background: linear-gradient(135deg, #1E1E2F, #2B2D42);
        color: #F0F0F0;
        font-family: 'Segoe UI', sans-serif;
        animation: slideIn 1s ease-out;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #20232A;
        border-right: 2px solid #FFD700;
    }

    /* Sidebar text and hover */
    .css-1cpxqw2, .css-qri22k {
        color: #FFFFFF;
        transition: color 0.3s ease;
    }

    .css-qri22k:hover {
        color: #00FFFF;
    }

    /* Custom label */
    .custom-label {
        color: #FFD700;
        font-weight: bold;
        font-size: 16px;
    }

    /* Prediction result styles */
    .predict_result_green {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #00FF7F;
        text-shadow: 1px 1px 2px #000;
    }

    .predict_result_red {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        color: #FF4500;
        text-shadow: 1px 1px 2px #000;
    }

    /* Content text styling */
    .custom-text {
        color: #EAEAEA;
        font-size: 14px;
        line-height: 1.6;
        text-align: justify;
        padding: 10px;
        border-left: 4px solid #FFD700;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 8px;
        animation: slideIn 0.8s ease-out;
    }

    /* Section headings */
    h2.custom-text {
        color: #00FFFF;
        font-size: 22px;
        margin-top: 30px;
        text-shadow: 0 0 10px #00FFFF;
        transition: all 0.3s ease;
    }

    h2.custom-text:hover {
        color: #FFD700;
        text-shadow: 0 0 5px #FFD700;
    }

    /* List hover effect */
    ul.custom-text li {
        margin-bottom: 8px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        padding: 6px;
        border-radius: 5px;
    }

    ul.custom-text li:hover {
        background-color: #FFD70033;
        transform: scale(1.02);
        cursor: pointer;
    }

    /* Image hover effect */
    img.hover-img {
        border-radius: 12px;
        box-shadow: 0 0 10px #FFD700;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    img.hover-img:hover {
        transform: scale(1.03);
        box-shadow: 0 0 20px #FFD700;
    }
    </style>
""",
    unsafe_allow_html=True,
)


def about_dataset():
    st.title("📊 Sumber Data")

    st.markdown(
        """
        <h2 class="custom-text">📊 Informasi Dataset Penelitian</h2>
        <p class="custom-text">
            Dataset yang digunakan dalam penelitian ini berasal dari <b>Kaggle.com</b> 🧠. 
            Terdiri dari <b>7.023 citra MRI otak</b> yang digunakan untuk mengidentifikasi 
            keberadaan dan jenis tumor otak. Data ini sangat penting untuk pengembangan 
            sistem deteksi dini berbasis AI.
        </p>

        <h2 class="custom-text">🧬 Kategori Kelas</h2>
        <p class="custom-text">Dataset ini terbagi menjadi 4 kelas utama:</p>
        """,
        unsafe_allow_html=True,
    )

    # st.image("data_and_model/img_dataset.png", use_container_width=True)

    with st.expander("🟢 No Tumor"):
        st.image("data_and_model/no tumor.png", use_container_width=True)

    with st.expander("🔵 Glioma"):
        st.image("data_and_model/glioma.png", use_container_width=True)

    with st.expander("🟣 Meningioma"):
        st.image("data_and_model/meningioma.png", use_container_width=True)

    with st.expander("🟠 Pituitary"):
        st.image("data_and_model/pituitary.png", use_container_width=True)

    st.markdown(
        """
        <h2 class="custom-text">📁 Pembagian Dataset</h2>
        <ul class="custom-text">
            <li>🔧 Training set: 80%</li>
            <li>🧪 Validation set: 10%</li>
            <li>🔍 Testing set: 10%</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown(
        """
        <hr style="border:1px solid #FFD700; margin-top:40px;">
        <p style="text-align:center; color:#888;">❤️ Politeknik Artificial Intelligence ❤️</p>
    """,
        unsafe_allow_html=True,
    )


about_dataset()
