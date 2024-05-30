import streamlit as st
st.markdown('<div class="contact-me">', unsafe_allow_html=True)
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #6A0083;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = 'Nicolás Vega Muñoz'
with col1:
    gradient('#FFD4DD','#000395','e0fbfc','📨 Contacta conmigo!', '')
    st.write("")
    # st.write(info['About'])


contact_form = """
<style>
form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
input, textarea, button {
    width: 100%;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
}
input:focus, textarea:focus {
    border-color: #6a1b9a;
    outline: none;
}
button {
    background-color: #6a1b9a;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}
button:hover {
    background-color: #4a148c;
}
</style>
<form action="https://formsubmit.co/nicovegamunoz1@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
    <button type="submit">Enviar</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
