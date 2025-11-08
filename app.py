import streamlit as st
import requests

# ===========================
# CONFIGURAÇÃO DA PÁGINA
# ===========================
st.set_page_config(page_title="Monitoramento da Qualidade do Ar", page_icon="💨", layout="centered")

# ===========================
# ESTILO PERSONALIZADO
# ===========================
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #e6f7ff, #cceeff);
            font-family: 'Poppins', sans-serif;
            color: #004d66;
        }
        h1, h2, h3 {
            text-align: center;
            color: #004d99;
        }
        .intro {
            text-align: center;
            font-size: 16px;
            color: #004d66;
            margin-bottom: 30px;
        }
        .mensagem {
            text-align: center;
            font-size: 18px;
            margin-top: 10px;
            color: #004d66;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: #004d66;
            margin-top: 40px;
        }
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
st.markdown(
    "<p class='intro'>Este projeto tem como objetivo conscientizar a população sobre a importância da qualidade do ar e seu impacto na saúde e no meio ambiente.</p>",
    unsafe_allow_html=True
)

# ===========================
# CAMPO DE ENTRADA
# ===========================
cidade = st.text_input("Digite o nome da sua cidade:", "Hortolândia")

# ===========================
# BOTÃO CENTRALIZADO
# ===========================
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    verificar = st.button("🔍 Verificar Qualidade do Ar")

# ===========================
# FUNÇÃO PRINCIPAL
# ===========================
if verificar:
    st.info("⏳ Verificando a qualidade do ar, por favor aguarde...")

    try:
        # Obter latitude e longitude da cidade
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt&format=json"
        geo_res = requests.get(geo_url, verify=True).json()

        if "results" not in geo_res or not geo_res["results"]:
            st.error("❌ Cidade não encontrada. Verifique o nome e tente novamente.")
        else:
            lat = geo_res["results"][0]["latitude"]
            lon = geo_res["results"][0]["longitude"]

            # Obter índice de qualidade do ar
            air_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&hourly=us_aqi"
            air_res = requests.get(air_url, verify=True).json()

            valor_qualidade = air_res["hourly"]["us_aqi"][-1]

            # Caso o valor venha None
            if valor_qualidade is None:
                st.warning("⚠️ O valor de qualidade do ar ainda não está disponível para esta hora.")
                st.stop()

            # Exibe o valor numérico
            st.markdown(f"<h2>Índice de Qualidade do Ar: <b>{valor_qualidade}</b></h2>", unsafe_allow_html=True)

            # Interpretação do valor
            if 0 <= valor_qualidade <= 50:
                st.success(f"🌿 Qualidade do ar: **Boa** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>O ar está limpo e saudável! Continue adotando práticas sustentáveis e evite o uso excessivo de veículos.</p>", unsafe_allow_html=True)
            elif 51 <= valor_qualidade <= 100:
                st.info(f"🌤️ Qualidade do ar: **Moderada** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>O ar está aceitável, mas pessoas sensíveis devem limitar longas exposições. Pequenas ações ajudam a manter o ar limpo!</p>", unsafe_allow_html=True)
            elif 101 <= valor_qualidade <= 150:
                st.warning(f"😷 Qualidade do ar: **Ruim para grupos sensíveis** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>Pessoas com problemas respiratórios devem evitar atividades ao ar livre. Incentive o transporte coletivo e evite queimadas.</p>", unsafe_allow_html=True)
            elif 151 <= valor_qualidade <= 200:
                st.error(f"🌫️ Qualidade do ar: **Ruim** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>Evite exercícios ao ar livre. Reduza o uso de veículos e mantenha janelas fechadas.</p>", unsafe_allow_html=True)
            elif 201 <= valor_qualidade <= 300:
                st.error(f"🌋 Qualidade do ar: **Muito Ruim** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>O ar está muito poluído. Fique em locais fechados e promova a conscientização ambiental.</p>", unsafe_allow_html=True)
            elif 301 <= valor_qualidade <= 500:
                st.error(f"☠️ Qualidade do ar: **Perigosa** ({valor_qualidade})")
                st.markdown("<p class='mensagem'>Evite sair de casa e busque locais com purificação de ar. Reforce medidas ambientais urgentes.</p>", unsafe_allow_html=True)
            else:
                st.warning(f"Valor inválido retornado pela API: {valor_qualidade}")

    except requests.exceptions.SSLError:
        st.error("⚠️ Erro de verificação SSL. Tente novamente em outro momento ou verifique sua conexão segura.")
    except Exception as e:
        st.error(f"❌ Ocorreu um erro ao buscar os dados: {e}")

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
