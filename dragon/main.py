# Importa todas las funciones del módulo turtle
from turtle import *

# Importa funciones para trabajar con colores en formato HSV
from colorsys import *

# Acelera la animación (400 es bastante rápido)
tracer(400)

# Cambia el color de fondo a negro
bgcolor('black')

# Oculta la flechita (cursor) del turtle
hideturtle()

# Define el grosor del lápiz
pensize(2)

# Bucle principal: se repite 460 veces
for i in range(460):
    
    # Cambia el color dinámicamente usando HSV
    # i/600 cambia gradualmente el tono (Hue)
    # 1 es saturación máxima
    # 1 es brillo máximo
    color(hsv_to_rgb(i / 600, 1, 1))
    
    # Segundo bucle que se repite 10 veces
    for b in range(10):
        
        # Dibuja parte de un círculo
        # El radio aumenta progresivamente (40 + i * 0.8)
        # 90 significa que solo dibuja 90 grados del círculo
        circle(40 + i * 0.8, 90)
        
        # Gira 80 grados a la derecha
        right(80)
        
        # Gira 10 grados adicionales (total 90 grados)
        right(10)
        
        # Avanza una distancia proporcional a i
        forward(i * 0.8)
        
        # Dibuja otro arco pequeño (radio 20, ángulo 200 grados)
        circle(20, 200)
        
        # Retrocede la misma distancia para volver al punto anterior
        backward(i * 0.8)

# Mantiene la ventana abierta hasta que la cierres
done()