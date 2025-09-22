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


# Main content
def about_case():
    st.title("🧠 Tentang Kasus")

    st.markdown(
        """
        <h2 class="custom-text">🧠 Latar Belakang Masalah</h2>
        <p class="custom-text">
            Penelitian ini berfokus pada tantangan identifikasi jenis tumor otak, yang menjadi isu penting di bidang medis. Tumor otak dapat:
        </p>
        <ul class="custom-text">
            <li>Bersifat <b>jinak</b> atau <b>ganas</b></li>
            <li>Tumor ganas berpotensi <b>berkembang cepat</b> dan <b>mengancam jiwa</b></li>
            <li>Deteksi dini sangat penting untuk <b>meningkatkan peluang kesembuhan</b></li>
            <li>Penanganan medis yang tepat bergantung pada <b>diagnosis awal yang akurat</b></li>
        </ul>

        <h2 class="custom-text">🧪 Tantangan Analisis MRI</h2>
        <p class="custom-text">
            MRI merupakan alat utama dalam mendeteksi tumor otak, namun analisis manual menghadapi beberapa kendala:
        </p>
        <ul class="custom-text">
            <li>Memerlukan <b>waktu lama</b> untuk interpretasi</li>
            <li>Sangat bergantung pada <b>keahlian radiolog</b></li>
            <li>Rentan terhadap <b>subjektivitas</b> dan <b>inkonsistensi diagnosis</b></li>
        </ul>

        <h2 class="custom-text">🔬 Pendekatan Penelitian</h2>
        <p class="custom-text">
            Penelitian ini mengusulkan pendekatan berbasis deep learning dengan strategi berikut:
        </p>
        <ul class="custom-text">
            <li>Menggunakan <b>Convolutional Neural Networks (CNN)</b></li>
            <li>Memanfaatkan <b>transfer learning</b> dan <b>ensemble learning</b></li>
            <li>Model yang digunakan:
                <ul>
                    <li>MobileNetV2</li>
                    <li>EfficientNet-B0</li>
                    <li>GoogleNet</li>
                </ul>
            </li>
            <li>Penggabungan model dengan <b>bagging ensemble</b> untuk meningkatkan akurasi</li>
        </ul>

        <h2 class="custom-text">🎯 Harapan dan Manfaat</h2>
        <p class="custom-text">
            Sistem yang dikembangkan diharapkan mampu:
        </p>
        <ul class="custom-text">
            <li>Memberikan <b>klasifikasi tumor yang lebih akurat</b></li>
            <li>Mempercepat proses diagnosis secara <b>efisien</b></li>
            <li>Meningkatkan <b>stabilitas hasil</b> dibandingkan analisis manual</li>
            <li>Menjadi <b>dukungan teknologi</b> dalam diagnosis medis yang lebih andal</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

    # # Optional image (place inside 'static' folder)
    # st.markdown(
    #     """
    #     <img src="static/Screenshot.png" class="hover-img" width="100%">
    # """,
    #     unsafe_allow_html=True,
    # )

    # Footer
    st.markdown(
        """
        <hr style="border:1px solid #FFD700; margin-top:40px;">
        <p style="text-align:center; color:#888;">❤️ Politeknik Artificial Intelligence ❤️</p>
    """,
        unsafe_allow_html=True,
    )


about_case()
