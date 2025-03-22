# Confiabilidade de um datacenter.

O gráfico representa a confiabilidade de uma infraestrutura de datacenter ao longo do tempo, baseada no MTBF onde o eixo **X** representa o tempo em em horas e o eixo **Y** representa a confiabilidade (que varia de 0% a 100%).

A confiabilidade é calculada utilizando a seguinte fórmula:

$$
R(t) = e^{-t/\mathrm{MTBF}}
$$

Onde:
- $R(t)$ = Probabilidade de operação sem falhas no tempo $t$
- $\mathrm{MTBF}$ = tempo médio entre falhas
- $t$ = Período de operação considerado em horas (Período de um ano considerado no exemplo)
