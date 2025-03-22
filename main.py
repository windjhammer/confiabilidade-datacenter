import matplotlib
matplotlib.use('Agg')  
import numpy as np
import matplotlib.pyplot as plt

MTBF = 8766  # quantidade de horas

tempo = np.linspace(0, 15000, 100)

confiabilidade = np.exp(-tempo / MTBF)

plt.figure(figsize=(8, 5))
plt.plot(tempo, confiabilidade, label=f'MTBF = {MTBF} horas', color='b')
plt.xlabel('Tempo (horas)')
plt.ylabel('Confiabilidade R(t)')
plt.title('Confiabilidade de Infraestrutura de Datacenter')
plt.legend()
plt.grid(True)

plt.savefig("mtbf.png")

print("Gráfico salvo como arquivo no diretório.")

