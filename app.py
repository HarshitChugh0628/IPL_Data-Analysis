import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="IPL Data Analysis", page_icon="🍕", layout="wide")

st.markdown("""<h1 style='text-align:center; color:#FF4B4B;'>🍕 IPL Data Analysis</h1>""", unsafe_allow_html=True)
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)

## sidebar
with st.sidebar:
    st.image("pictures/sh-2.png", use_container_width=True)
    with st.expander("🧑‍🤝‍🧑 About us"):
        st.write("We are students building smart NLP tools using ML.")
    with st.expander("📞 Contact us"):
        st.write("Email: harshit@example.com")
        st.write("GitHub: github.com/harshit")


images = ['pictures/ipl-1.png', 'pictures/ipl-2.png', 'pictures/ipl-3.png']
for img_path in images:
    st.image(img_path,width=1800)
