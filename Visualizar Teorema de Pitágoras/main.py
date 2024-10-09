import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Configurações da figura
fig, ax = plt.subplots(figsize=(3.33, 3.33), dpi=300)

# Comprimentos dos catetos
a = 3
b = 4

# Hipotenusa
c = np.sqrt(a**2 + b**2)

# Coordenadas do triângulo retângulo
triangle_coords = np.array([[0, 0], [a, 0], [0, b]])

#Cores usadas
rosa = [0.984, 0.682, 0.823]
roxo = [0.435, 0.176, 0.659]
roxo_intenso = [0.341, 0.137, 0.522]
ametista = [0.6, 0.4, 0.8, 0.5]

# Adiciona o triângulo
triangle = plt.Polygon(triangle_coords, closed=True, edgecolor=roxo, facecolor=ametista)
ax.add_patch(triangle)

# Adiciona os quadrados
# Quadrado sobre o cateto 'a'
square_a = patches.Polygon([[0, -a], [a, -a], [a, 0], [0, 0]], closed=True, edgecolor=roxo, facecolor=rosa)
ax.add_patch(square_a)

# Quadrado sobre o cateto 'b'
square_b = patches.Polygon([[0, 0], [0, b], [-b, b], [-b, 0]], closed=True, edgecolor=roxo, facecolor=rosa)
ax.add_patch(square_b)

# Quadrado sobre a hipotenusa 'c'
square_c = patches.Polygon([[0,4], [4,7], [7,3], [3,0]], closed=True, edgecolor=roxo, facecolor=rosa)
ax.add_patch(square_c)

# Adiciona etiquetas
ax.text(a / 2, -a / 2, '$a^2$', horizontalalignment='center', verticalalignment='center', fontsize=12, color=roxo_intenso)
ax.text(-b / 2, b / 2, '$b^2$', horizontalalignment='center', verticalalignment='center', fontsize=12, color=roxo_intenso)
ax.text(3.5,3.5, '$c^2$', horizontalalignment='center', verticalalignment='center', fontsize=12, color=roxo_intenso)

# Adiciona etiquetas do triângulo
ax.text(a / 2, 0, '$a$', horizontalalignment='center', verticalalignment='top', fontsize=12, color=roxo_intenso)
ax.text(-0.1, b / 2, '$b$', horizontalalignment='right', verticalalignment='center', fontsize=12, color=roxo_intenso)
ax.text(1.5,2, '$c$', horizontalalignment='left', verticalalignment='bottom', fontsize=12, color=roxo_intenso)

# Configurações do gráfico
ax.set_aspect('equal', 'box')
ax.set_xlim(-b-1, a+b+1)
ax.set_ylim(-3.1, b+a+1)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
#plt.title('Visualização do Teorema de Pitágoras')

plt.subplots_adjust(left=0, right=1, top=1.09, bottom=0)

# Exibe o gráfico
plt.show()
