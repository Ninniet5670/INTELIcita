import streamlit as st
import requests
import json

st.set_page_config(
    page_title = 'INTELIcita',
    page_icon = 'frontend/app/assets/licitacao.png'
)

BACKEND_URL = "http://127.0.0.1:8000"


def main():
    st.title("Envio de Texto ou JSON para Processamento")

    option = st.selectbox("Escolha a forma de entrada:", ("Texto", "Arquivo JSON"))

    if option == "Texto":
        text_input = st.text_area("Digite seu texto aqui:")
        if st.button("Enviar Texto"):
            if text_input:
                pass  # process_text(text_input)
            else:
                st.error("Por favor, insira um texto.")
    
    elif option == "Arquivo JSON":
        file_upload = st.file_uploader("Carregue um arquivo JSON", type=["json"])
        if st.button("Enviar JSON"):
            if file_upload:
                pass  # process_json(file_upload)
            else:
                st.error("Por favor, carregue um arquivo JSON.")

def process_text(text):
    response = requests.post(f"{BACKEND_URL}/process-text/", json={"text": text})
    if response.status_code == 200:
        st.success("Texto processado com sucesso!")
        st.json(response.json())
    else:
        st.error(f"Erro no processamento do texto: {response.text}")

def process_json(file):
    try:
        json_data = json.load(file)
        response = requests.post(f"{BACKEND_URL}/process-json/", json=json_data)
        if response.status_code == 200:
            st.success("JSON processado com sucesso!")
            st.json(response.json())
        else:
            st.error(f"Erro no processamento do JSON: {response.text}")
    except json.JSONDecodeError:
        st.error("O arquivo carregado não é um JSON válido.")

if __name__ == "__main__":
    main()
