import matplotlib
matplotlib.use('Agg')  
import numpy as np
import matplotlib.pyplot as plt

MTBF = 8766  # quantidade de horas

tempo = np.linspace(0, 15000, 100)

confiabilidade = np.exp(-tempo / MTBF)

uptime_percentual = confiabilidade * 100

plt.figure(figsize=(8, 5))
plt.plot(tempo, uptime_percentual, label=f'MTBF = {MTBF} horas', color='b')
plt.xlabel('Tempo (horas)')
plt.ylabel('Confiabilidade (%)')
plt.title('Confiabilidade de Infraestrutura de Datacenter (Uptime %)')
plt.legend()
plt.grid(True)

plt.savefig("mtbf_uptime.png")

print("Gráfico salvo como arquivo no diretório.")

