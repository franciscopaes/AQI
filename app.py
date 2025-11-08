import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# ===========================
# CONFIGURAÇÃO DA PÁGINA
# ===========================
st.set_page_config(page_title="Monitoramento da Qualidade do Ar", page_icon="💨", layout="centered")

# ===========================
# ESTILO PERSONALIZADO
# ===========================
st.markdown("""
    <style>
        /* Fundo geral */
        .stApp {
            background: linear-gradient(135deg, #e6f7ff, #cceeff);
            font-family: 'Poppins', sans-serif;
            color: #004d66;
        }

        /* Títulos */
        h1, h2, h3 {
            text-align: center;
            color: #004d99;
        }

        /* Texto introdutório */
        .intro {
            text-align: center;
            font-size: 16px;
            color: #004d66;
            margin-bottom: 30px;
        }

        /* Texto dos resultados */
        .resultado {
            text-align: center;
            font-size: 22px;
            margin-top: 20px;
            font-weight: bold;
            color: #003366;
        }

        /* Mensagens complementares */
        .mensagem {
            text-align: center;
            font-size: 18px;
            margin-top: 10px;
            color: #004d66;
        }

        /* Rodapé */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #004d66;
            margin-top: 40px;
        }

        /* Botão personalizado */
        div[data-testid="stButton"] > button {
            background-color: #007acc;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.6em 1.2em;
            font-size: 16px;
            transition: 0.3s;
        }

        div[data-testid="stButton"] > button:hover {
            background-color: #005fa3;
            transform: scale(1.05);
        }

        /* Barra de informação (alertas do Streamlit) */
        .stAlert {
            color: #004d66 !important;
            background-color: #e6f2ff !important;
            border-left: 6px solid #007acc !important;
        }
    </style>
""", unsafe_allow_html=True)

# ===========================
# CABEÇALHO
# ===========================
st.title("Monitoramento da Qualidade do Ar")
st.markdown("<p class='intro'>Este projeto tem como objetivo conscientizar a população sobre a importância da qualidade do ar e seu impacto na saúde e no meio ambiente.</p>", unsafe_allow_html=True)

# ===========================
# BOTÃO CENTRALIZADO
# ===========================
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    verificar = st.button("🔍 Verificar Qualidade do Ar")

if verificar:
    st.info("⏳ Verificando a qualidade do ar, por favor aguarde...")

    # ===========================
    # CONFIGURAÇÃO DO SELENIUM
    # ===========================
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    # ===========================
    # ACESSANDO O SITE
    # ===========================
    URL_SITE = "https://weather.com/pt-BR/forecast/air-quality/l/e1af5159ff6ece8ea4699268b22e8c4b390cb745b0549fde9f796b5ffbbfadda?par=samsung_widget_ZTO&cm_ven=L1_condition_aqi&theme=samsungLight"
    driver.get(URL_SITE)
    time.sleep(5)

    # ===========================
    # CAPTURANDO O VALOR
    # ===========================
    try:
        elemento_qualidade = driver.find_element(By.CLASS_NAME, "AirQuality--displayValue--2Usp0")
        valor_qualidade = int(elemento_qualidade.text)
        driver.quit()

        st.markdown(f"<h2>Índice de Qualidade do Ar: <b>{valor_qualidade}</b></h2>", unsafe_allow_html=True)

        # ===========================
        # INTERPRETAÇÃO E ORIENTAÇÕES
        # ===========================
        if 0 <= valor_qualidade <= 50:
            st.success("Qualidade do ar: **Boa** 🌿")
            st.markdown("<p class='mensagem'>O ar está limpo e saudável! Continue adotando práticas sustentáveis e apoie ações que reduzam a poluição.</p>", unsafe_allow_html=True)

        elif 51 <= valor_qualidade <= 100:
            st.info("Qualidade do ar: **Moderada** 🌤️")
            st.markdown("<p class='mensagem'>O ar está razoavelmente limpo, mas pessoas sensíveis devem evitar longas exposições. Pequenas mudanças no dia a dia ajudam a melhorar a qualidade do ar.</p>", unsafe_allow_html=True)

        elif 101 <= valor_qualidade <= 150:
            st.warning("Qualidade do ar: **Ruim para grupos sensíveis** 😷")
            st.markdown("<p class='mensagem'>Pessoas com problemas respiratórios devem evitar atividades ao ar livre. Incentive o uso do transporte coletivo e evite queima de resíduos.</p>", unsafe_allow_html=True)

        elif 151 <= valor_qualidade <= 200:
            st.error("Qualidade do ar: **Ruim** 🌫️")
            st.markdown("<p class='mensagem'>A qualidade do ar está ruim. Evite exercícios ao ar livre e contribua reduzindo o uso de veículos e poluentes.</p>", unsafe_allow_html=True)

        elif 201 <= valor_qualidade <= 300:
            st.error("Qualidade do ar: **Muito Ruim** 🌋")
            st.markdown("<p class='mensagem'>O ar está muito poluído. Fique em locais fechados, com janelas fechadas. Reforce a conscientização ambiental em sua comunidade.</p>", unsafe_allow_html=True)

        elif 301 <= valor_qualidade <= 500:
            st.error("Qualidade do ar: **Perigosa** ☠️")
            st.markdown("<p class='mensagem'>Evite sair de casa e procure locais com purificação de ar. Situações como essa mostram a urgência de medidas ambientais globais.</p>", unsafe_allow_html=True)

        else:
            st.warning("Valor de qualidade do ar inválido.")

    except Exception as e:
        st.error("❌ Erro ao capturar a qualidade do ar. Tente novamente mais tarde.")
        st.markdown(f"<p class='mensagem'>Detalhes técnicos: {e}</p>", unsafe_allow_html=True)

# ===========================
# RODAPÉ
# ===========================
st.markdown("""
---
<div class='footer'>
Atividade acadêmica sem fins lucrativos<br>
Projeto desenvolvido por <b>Davi Alves</b>, <b>Gabriel Prestello</b> e <b>Thiago Francisco</b><br>
Inspirado na <b>ODS 11 – Cidades e Comunidades Sustentáveis</b>
</div>
""", unsafe_allow_html=True)
