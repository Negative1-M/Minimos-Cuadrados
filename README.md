# Minimos-Cuadrados
## Técnica de mínimos cuadrados para la identificación de sistemas paramétricos deterministas.
Para utilizar este código cambiando los valores necesarios, puedes seguir estos pasos:
1. **Modificar los datos de entrada-salida:** Puedes cambiar los valores en los arrays ***n*** y ***y*** para representar tus propios datos de entrada y salida.
2. **Modificar los vectores de entrada x y x1:** Si tu sistema tiene variables de entrada adicionales, puedes modificar los vectores ***x*** y ***x1*** según sea necesario.
3. **Modificar la construcción de la matriz phi:** Si el modelo que estás utilizando requiere una matriz ***phi*** diferente, puedes modificar la construcción de phi para adaptarla a tus necesidades.
4. **Interpretar y ajustar los resultados:** Después de ejecutar el código con tus propios datos, asegúrate de interpretar los resultados correctamente y realizar los ajustes necesarios en tu modelo según sea necesario.

Este código proporciona una base para implementar la técnica de mínimos cuadrados para la identificación paramétrica de sistemas, pero es importante entender la teoría detrás de este método y cómo se relaciona con tu problema específico para utilizarlo de manera efectiva.

### Grafica del modelo con los parametros de entrada y salida iniciales
![forma de ecuación de diferencias característica](/assets/1.png)

### Graficacion de la ecuacion de recurrencia obtenida anteriormente
Para utilizar este código cambiando los valores necesarios, puedes seguir estos pasos:
1. **Modificar la ecuación de recurrencia:** Puedes modificar la función ***modelo_discreto*** para representar un modelo diferente, ajustando los coeficientes y términos según sea necesario.
2. **Modificar los datos de entrada-salida:** Puedes cambiar la función de generación de datos de entrada ***u*** para representar tus propios datos de entrada. También puedes inicializar el ***array y*** con valores diferentes si es necesario.
3. **Interpretar y ajustar los resultados:** Después de ejecutar el código con tus propios datos o modificaciones, asegúrate de interpretar los resultados correctamente y realizar los ajustes necesarios en tu modelo según sea necesario.

![Modelo discreto lineal de la ecuacion de recurrencia](/assets/2.png)
