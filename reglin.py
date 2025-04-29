# Importando bibliotecas importantes
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Criando título para aplicação
st.title('Previsão Inicial de Custo para Franquia')

# Carregando dados
dados = pd.read_csv('slr12.csv', sep=';')

# Separando as variáveis em feature e target
X = dados[['FrqAnual']]
y = dados['CusInic']

modelo = LinearRegression().fit(X,y)

# Criando colunas para exibir conteúdo um ao lado do outro no streamlit
col1, col2 = st.columns(2)

# Configurando a primeira coluna com a tabela de dados
with col1:
    st.header('Dados')
    st.table(dados.head(10))

# Configurando a segunda coluna com o gráfico de dispersão
with col2:
    st.header('Gráfico de dispersão')
    # Criando o gráfico
    fig, ax = plt.subplots()
    # Criando os pontos
    ax.scatter(X, y, color='darkblue')
    # Criando a linha de regressão
    ax.plot(X, modelo.predict(X), color='red')
    # Exibindo o gráfico na página
    st.pyplot(fig)

# Criando o botão de input e botão de processar para calcular o custo inicial
st.header('Valor Anual da Franquia:')
novo_valor = st.number_input('Insira Novo Valor', min_value=1.0, max_value=999999.0, value= 1500.0, step=0.01)
processar = st.button('Processar')

# Fazendo a condição da previsão do modelo com base nos dados inseridos pelo usuário
if processar:
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
    prev = modelo.predict(dados_novo_valor)
    st.header(f'Previsão de Custo Inicial R$:{prev[0]:.2f}')