
import streamlit as st 

st.title('Simulador de Gorjeta')

atendimento = st.text_input('Digite o nivel de atendimento : (otimo, medio, ruim)').lower()

st.divider()

valorConta = st.number_input('Digite o  valor da compra : ')

valorGorjeta = 0

if atendimento == 'otimo':
    valorGorjeta = valorConta * 0.15
    valorTotal = valorConta + valorGorjeta
    st.success(f'o valor da conta com a gorgeta ficou {valorTotal}')
elif atendimento == 'medio':
    valorGorjeta = valorConta * 0.10
    valorTotal = valorConta + valorGorjeta
    st.success(f'o valor da conta com a gorgeta ficou {valorTotal}')
elif atendimento == 'ruim':
    valorGorjeta = valorConta * 0.05 
    valorTotal = valorConta + valorGorjeta 
    st.success(f'o valor da conta com gorjeta ficou {valorTotal}')

else:
    st.error('valor invalido')