import streamlit as st 

import PyPDF2  # ler arquivos PDF 

import re # ler padroes


st.title('Sitema de verfica63,rçao de Fraude De Boleto')

st.header('Anexe o boleto o link Abaixo :')

boleto = st.file_uploader('Anexar Boleto : ') # pegar o arquivo 

if boleto is not None : # verficar se colocou o boleto

    try:
        pdf_reader = PyPDF2.PdfReader(boleto) # pegando o boleto
        texto = ''

        

        for pagina in pdf_reader.pages:
            texto += pagina.extract_text()

        #limpando o texto(remover espaço e pontos)
        texto_limpo = re.sub(r'[.\s]', '', texto)
    
        # verificando se o codigo tem 44 digitos 
        codigos = re.findall(r'\d{44}', texto_limpo)

        if codigos:
            st.success(f'o boleto é real {codigos[0]}')
        else:
            st.error('o boleto é falso')
    except Exception as e:
        st.error(f'erro ao processar o PDF : {e}')
else:
    st.info('Envie o arquivo PDF para verficar')