import pandas as pd
import numpy as np

# Definindo uma semente para que os dados sejam sempre os mesmos ao rodar
np.random.seed(42)

# Configuração do número de registros
n_registros = 300

# Gerando dados aleatórios com lógica médica aproximada
data = {
    'ID': range(1, n_registros + 1),
    'Idade': np.random.randint(18, 91, size=n_registros),
    'Sexo': np.random.choice(['Masculino', 'Feminino'], size=n_registros),
    'Pressao_Arterial_Sistolica': np.random.randint(95, 185, size=n_registros),
    'Colesterol': np.random.randint(150, 310, size=n_registros),
    'Historico_Cardiaco': np.random.choice(['Sim', 'Nao'], size=n_registros, p=[0.25, 0.75]),
    'Sintomas': np.random.choice(['Assintomatico', 'Dor no Peito', 'Falta de Ar', 'Fadiga'], size=n_registros),
    'Frequencia_Cardiaca_Repouso': np.random.randint(58, 102, size=n_registros),
    'Diabetes': np.random.choice(['Sim', 'Nao'], size=n_registros, p=[0.15, 0.85])
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando o arquivo CSV
nome_arquivo = 'dados_pacientes.csv'
df.to_csv(nome_arquivo, index=False, encoding='utf-8')

print(f"Arquivo '{nome_arquivo}' gerado com sucesso com {n_registros} linhas!")

# Exibindo as primeiras 5 linhas para conferência
print("\nExemplo das primeiras linhas:")
print(df.head())