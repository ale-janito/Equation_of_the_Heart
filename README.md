# Equation_of_the_Heart
Generar y animar la ecuación paramétrica de la forma de un corazón
Este proyecto tiene como objetivo generar y animar la ecuación paramétrica de la forma de un corazón utilizando Python y la biblioteca Matplotlib. A través de la animación, se visualiza cómo se forma el corazón conforme se varía el parámetro 
𝑡
t, proporcionando una representación visual atractiva de la ecuación.

Requisitos del Proyecto
Python 3.x: Asegúrate de tener instalada una versión reciente de Python (recomendado 3.6+).

Bibliotecas:

NumPy: Para realizar cálculos numéricos, en particular el manejo de las ecuaciones matemáticas.

Matplotlib: Para generar y visualizar las gráficas y la animación.

Puedes instalar estas bibliotecas usando pip:
    pip install numpy matplotlib

Ecuación del Corazón
La forma del corazón se genera a partir de las siguientes ecuaciones paramétricas:
![image](https://github.com/user-attachments/assets/c028bee4-bd36-4d46-be32-94d780a184b1)

x(t) = 
16
⋅
sin
⁡
3
(
𝑡
)
16⋅sin 
3
 (t)

y(t) = 
13
⋅
cos
⁡
(
𝑡
)
−
5
⋅
cos
⁡
(
2
𝑡
)
−
2
⋅
cos
⁡
(
3
𝑡
)
−
cos
⁡
(
4
𝑡
)
13⋅cos(t)−5⋅cos(2t)−2⋅cos(3t)−cos(4t)

Estas ecuaciones generan una figura de un corazón al graficar los puntos para varios valores de t.
![image](https://github.com/user-attachments/assets/91a67ec0-f810-4156-a5e4-e37876aa6f0c)


Estructura del Proyecto
El proyecto está compuesto por un archivo principal de Python que crea la animación.
![image](https://github.com/user-attachments/assets/d8439f43-950b-4d4b-989b-cd0cb00f2b1e)
![image](https://github.com/user-attachments/assets/e0983672-1b9e-440f-bd5a-33e0f2abeacf)

Archivos del Proyecto:
#Equation_of_the_Heart.py: Contiene el código principal para generar la animación.

#README.md: Este archivo, que proporciona detalles sobre cómo ejecutar el proyecto.

#vista del grafico

![corazon-python](https://github.com/user-attachments/assets/7503546a-6829-4742-a6c2-f8b612bb9e93)

                              Explicación del Código:
      Librerías Importadas:

numpy: Se usa para generar un rango de valores para el parámetro 
𝑡
t y para realizar cálculos de las funciones trigonométricas.

matplotlib.pyplot: Se utiliza para generar las gráficas y la animación.

matplotlib.animation.FuncAnimation: Permite la creación de animaciones paso a paso.

    Generación de Datos:

t: Un rango de valores entre 0 y 
2
𝜋
2π, que representan el parámetro temporal para las ecuaciones.

x y y: Se calculan utilizando las ecuaciones paramétricas definidas al principio del código.

    Creación del Gráfico:

Se crea una figura y un conjunto de ejes con plt.subplots().

Se establecen límites para los ejes x y y y se configura la apariencia del gráfico.

    Animación:

La función animate() es responsable de actualizar los datos de la animación y mostrar el punto a medida que el parámetro 
𝑡
t cambia.

La animación se genera usando FuncAnimation, que crea un objeto de animación que actualiza la gráfica en cada fotograma.

    Mostrar el Gráfico:

Se utiliza plt.show() para visualizar la animación en una ventana.
