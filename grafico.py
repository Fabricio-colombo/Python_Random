import matplotlib.pyplot as plt

# Definir os dados
labels = ['Maio', 'Junho', 'Julho', 'Agosto', 'Setembro']
serie1 = [50, 70, 30, 80, 60]
serie2 = [20, 90, 40, 70, 30]

# Criar o gráfico
fig, ax = plt.subplots()
ax.bar(labels, serie1, label='Série 1')
ax.bar(labels, serie2, bottom=serie1, label='Série 2')

# Adicionar títulos e legendas
ax.set_ylabel('Valores')
ax.set_xlabel('Meses')
ax.set_title('Gráfico de barras com duas séries de dados')
ax.legend()

# Exibir o gráfico
plt.show()
