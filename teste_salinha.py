
import streamlit as st
st.write('Oi')

st.write('estou aprendendo')
st.write('acho que entendi!')

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.slider('Selecione uma respota', 0,100)
st.select_slider('Selecione uma resposta', options=['A', 'B', 'C'])
st.select_slider('Selecione uma resposta', ['Bom', 'Ruim'])
st.selectbox('Selecione uma resposta', ['Bom', 'Ruim'])

x = st.checkbox('Sim')
st.write(x)

