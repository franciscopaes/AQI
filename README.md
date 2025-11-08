# Monitoramento da Qualidade do Ar

Aplicação desenvolvida em **Python** com **Streamlit**, que realiza a consulta do **Índice de Qualidade do Ar (IQA)** em tempo real utilizando a **API Open-Meteo**.  
O sistema exibe mensagens interativas sobre o nível de poluição e fornece orientações sobre cuidados com a saúde e o meio ambiente.

---

## 🚀 Funcionalidades

- Consulta automática da **qualidade do ar** com base na cidade digitada pelo usuário.  
- Integração com a **API Open-Meteo** para obter dados ambientais atualizados.  
- Classificação do ar em níveis (boa, moderada, ruim, perigosa, etc).  
- Exibição de mensagens personalizadas com recomendações de saúde e sustentabilidade.  
- Interface moderna e amigável desenvolvida com **Streamlit**.  
- Projeto inspirado na **ODS 11 – Cidades e Comunidades Sustentáveis**.

---

## 🧩 Exemplo de uso

O usuário digita o nome de sua cidade (ex: *Hortolândia*) e clica em **“🔍 Verificar Qualidade do Ar”**.  
A aplicação exibe:
- O valor do **Índice de Qualidade do Ar (AQI)**;  
- A classificação (boa, moderada, ruim...);  
- Uma mensagem educativa com recomendações específicas.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**  
- **Streamlit** — Interface web interativa  
- **Requests** — Comunicação com APIs REST  
- **Open-Meteo API** — Dados meteorológicos e de qualidade do ar  

---

## ⚙️ Instalação e execução

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/monitoramento-qualidade-ar.git
```
### 2. Acesse a pasta do projeto
```bash
cd monitoramento-qualidade-ar
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```
### 4. Execute o projeto
```bash
streamlit run app.py
```

