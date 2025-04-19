import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<h1 class="titulo">EU AMO VOCÊ</h1>', unsafe_allow_html=True)

st.title("Exemplo de Botão")

if st.button('Clique aqui'):
    st.write("Você clicou no botão!")
else:
    st.write("Aguarde o clique no botão.")
    
    
nome = st.text_input("Digite seu nome:")
st.write("Eu amo voce,", nome)