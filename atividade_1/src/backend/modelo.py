import pandas as pd
import numpy as np
from arch import arch_model
import math
import pandas as pd
from arch import arch_model
from statsmodels.tsa.arima.model import ARIMA
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Caminho completo para o arquivo bitcoin.csv
csv_path = os.path.join(current_dir, 'database/bitcoin.csv')

# Carregar o arquivo CSV
df = pd.read_csv(csv_path)


# Renomeando as colunas
df = df.rename(columns={'Último': 'Ultimo', 'Máxima': 'Maxima', 'Mínima': 'Minima', 'Vol.': 'Vol'})
df['Vol'] = df['Vol'].replace('K', '000')
df['Vol'] = df['Vol'].str.replace('K', '000')
df['Var%'] = df['Var%'].str.replace('%', '')
for i in df.columns:
    try:
        if(i != 'Data'):
            df[f'{i}'] = df[f'{i}'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
    except:
        pass

# Transformando os dados para os tipos adequados
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df['Ultimo'] = pd.to_numeric(df['Ultimo'])
df = df.sort_values(['Data'])

columns = ['Ultimo', 'Abertura', 'Maxima', 'Minima', 'Vol', 'Var%']
df_max_scaled = df.copy() 
  
# apply normalization techniques 
for column in df_max_scaled.columns:
    if column != "Data":
        df_max_scaled[column] = df_max_scaled[column]  / df_max_scaled[column].abs().max() 

df['log_return'] = (df['Ultimo'] / df['Ultimo'].shift(1)).apply(lambda x: np.log(x))
df.dropna(inplace=True)
print(df.head())



# Modelo GARCH (1, 1) - você pode ajustar as ordens de p e q conforme necessário
model = arch_model(df['log_return'], vol='Garch', p=1, q=1)
garch_fit = model.fit()
forecasts = garch_fit.forecast(horizon=30)  # Prevendo os próximos 30 dias
volatility = forecasts.variance[-1:]


# Carregar os dados
# df = pd.read_csv("dados_bitcoin.csv", parse_dates=["data"])
df.set_index("Data", inplace=True)

# Verificar e garantir que 'Ultimo' é uma série numérica unidimensional
if df['Ultimo'].ndim != 1:
    raise ValueError("A coluna 'Ultimo' não está em formato unidimensional.")

# Garantir que não há valores nulos ou não numéricos
df = df[['Ultimo']].dropna()
df['Ultimo'] = pd.to_numeric(df['Ultimo'], errors='coerce')

# Calcular o retorno logarítmico
df['log_return'] = np.log(df['Ultimo'] / df['Ultimo'].shift(1))
df.dropna(inplace=True)

# Ajustar o modelo GARCH (1, 1)
model = arch_model(df['log_return'], vol='Garch', p=1, q=1)
garch_fit = model.fit()

# Previsão da volatilidade para os próximos 30 dias
forecast_horizon = 30
forecasts = garch_fit.forecast(horizon=forecast_horizon)
volatility_forecast = forecasts.variance.values[-1]  # Assegure-se que está pegando a última linha

# Criar DataFrame para previsões
forecast_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=forecast_horizon)
forecast_df = pd.DataFrame(volatility_forecast, index=forecast_dates, columns=['forecast_volatility'])

# Adicionar a coluna de preços previstos (por simplicidade, usando um modelo ARIMA para preços)

# Ajustar o modelo ARIMA para prever o preço
arima_model = ARIMA(df['Ultimo'], order=(5,1,0))
arima_fit = arima_model.fit()

# Prever o preço para os próximos 30 dias
price_forecast = arima_fit.forecast(steps=forecast_horizon)
forecast_df['forecast_price'] = price_forecast

# Adicionar coluna com sinal de compra
# Obter o preço da semana passada para comparação
one_week_ago = df.index[-7:]
prices_last_week = df.loc[one_week_ago, 'Ultimo'].mean()  # Média dos preços da semana passada

forecast_df['previous_week_avg'] = prices_last_week

# Adicionar coluna com sinal de compra
forecast_df['buy_signal'] = forecast_df['forecast_price'] < forecast_df['previous_week_avg']

# Obter previsões para os próximos 5 dias
forecast_5_days = forecast_df.head(5)

# Diagnóstico das previsões
print("Previsões de preços e sinais de compra para os próximos 5 dias:")
print(forecast_5_days)
print("Descrição das previsões de preços e sinais de compra:")
print(forecast_5_days.describe())

# Ajustar critério de seleção
percentil = 10
threshold = np.percentile(forecast_df['forecast_volatility'], percentil)
best_forecast_days = forecast_df[forecast_df['forecast_volatility'] <= threshold]

# Exibir os melhores dias para comprar Bitcoin (baseado em baixa volatilidade e previsão de preço menor que o preço da semana passada)
print("Melhores dias para comprar Bitcoin (baseado em baixa volatilidade e previsão de preço menor que o preço da semana passada):")
print(best_forecast_days)

