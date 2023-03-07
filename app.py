from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu




st.set_page_config(page_title="Accesoria", page_icon=":tada:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
# use local css


#---LOAD ASSETS ---
lottie_shopping = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_5ngs2ksb.json")
img_malisa = Image.open("C:\\Users\\PC\\Python Projects\\Accesoria\\images\\malisa.png")
img_onlinesm2 = Image.open("C:\\Users\\PC\\Python Projects\\Accesoria\\images\\slika2.png")


#--HEADER SECTION---
with st.container():
    st.subheader("Cao, kupac")
    st.title("Accesoria")
    st.write("Prvi i jedini online shoppingmall u Srbiji, sve radnje na jednom mestu!")
    st.write("[Learn More >](https://www.instagram.com/unicatjewelry/)")
  

#---WHAT I DO---  
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Na nasoj stranici mozete naci prodavnice koje vama odgovaraju
            i prodavnice koje pruzaju usluge koje vama odgovaraju....
            bla,bla,bla,bla,bla
            """
        )
        st.write("[Instagram stranica >](https://www.instagram.com/stefanprentovic/)")
    with right_column:
        st_lottie(lottie_shopping, height=300, key="shopping")
        
#--PROJECTS---
with st.container():
    st.write("---")
    st.header("Kompletan izbor")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_malisa)
    with text_column:
        st.subheader("Malisa - prodaj kod Malise, placa najvise")
        st.write(
            """
            Sta je bilo, sto si skenjan?
            Ma imam neko zlato, ne znam kome da prodam...
            Hah, prodaj kod malise, placa najvise!!!
            """
        )
        st.markdown("[Idi na sajt!](https://zlatarmalisa.com/?lang=en)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_onlinesm2)
    with text_column:
        st.subheader("Druga prodavnica")
        st.write(
        """
        Text vezan za prodavnicu, bla,bla,bla,bla,bla
        """
        )
        st.markdown("[Idi na sajt!](https://zlataraormai.com/)")
        
#--CONTACT---
with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/your@email.com" method="POST">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


# !!!!!! NAPRAVI SIDEBAR I NA NJEMU PRODAVNICE
# !!!!!! NAPRAVI VISE FAJLOVA ZA PRODAVNICU, DA SVE STOJE NA JENDOM MESTU