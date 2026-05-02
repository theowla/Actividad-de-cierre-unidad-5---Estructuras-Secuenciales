# Actividad-de-cierre-unidad-5---Estructuras-Secuenciales
Actividad de cierre unidad 5 - Estructuras Secuenciales

**Guion para video explicativo – Sistema de Control de Inventario**

Buenos días, mi nombre es [tu nombre]. En este video voy a explicar el funcionamiento y la lógica detrás del sistema de control de inventario que desarrollé para la ferretería.

En primer lugar, el programa está estructurado a partir de un menú interactivo que se ejecuta dentro de un bucle `while`, lo que permite que el sistema permanezca activo hasta que el usuario decida salir. A partir de la opción ingresada, se utilizan estructuras condicionales `if`, `elif` y `else` para dirigir el flujo del programa hacia la funcionalidad correspondiente.

Para el almacenamiento de los datos utilicé dos listas paralelas: una llamada *herramientas* y otra llamada *existencias*. La relación entre ambas se mantiene a través del índice, de manera que cada posición en la lista de herramientas corresponde exactamente a la misma posición en la lista de existencias. Esto permite cumplir con el requisito de sincronización de datos.

En cuanto a la carga inicial, el sistema solicita al usuario la cantidad de herramientas a ingresar. Luego, mediante un bucle `for`, se piden los nombres uno por uno. Se validan para evitar valores inválidos o duplicados, asegurando así la consistencia de la información desde el inicio.

Posteriormente, en la carga de existencias, se recorre la lista de herramientas ya cargadas y se solicita al usuario la cantidad de unidades para cada una. Se valida que los valores sean números enteros no negativos, y se almacenan respetando el orden de las herramientas.

Para la visualización del inventario, el sistema recorre ambas listas en paralelo y muestra cada herramienta junto con su stock actual. Antes de realizar esta operación, se verifica que ambas listas tengan datos y que estén sincronizadas, evitando errores.

La consulta de stock permite buscar una herramienta por su nombre. Para esto, se utiliza el método `index` de la lista, que permite encontrar la posición de la herramienta y acceder a su correspondiente cantidad en la lista de existencias.

El reporte de agotados consiste en recorrer las listas y mostrar únicamente aquellas herramientas cuya cantidad es igual a cero.

En la opción de alta de nuevo producto, el sistema permite agregar una nueva herramienta junto con su stock inicial. Se validan tanto el nombre como la cantidad, y en caso de error, el sistema informa el motivo y vuelve al menú principal, tal como lo establece la consigna.

Por otro lado, la actualización de stock contempla dos casos: venta e ingreso. En el caso de venta, se verifica que haya suficiente stock antes de descontar unidades, evitando valores negativos. En el caso de ingreso, simplemente se suma la cantidad al stock existente. También se valida que la herramienta exista previamente en el sistema.

Respecto a las decisiones de diseño, elegí utilizar bucles `while` en los casos donde es necesario repetir una acción hasta que el usuario ingrese un dato válido, como en las validaciones. En cambio, utilicé bucles `for` cuando ya se conoce la cantidad de iteraciones, como en la carga inicial o el recorrido de las listas. Las estructuras condicionales permiten controlar los distintos casos posibles y asegurar un comportamiento correcto del sistema.

A continuación, voy a realizar una breve demostración. Primero, un caso de uso correcto: se cargan herramientas, se asignan existencias y se consulta el inventario. Luego, un caso de error: por ejemplo, intentar vender más unidades de las disponibles o ingresar un nombre inválido, donde el sistema responde con un mensaje de error adecuado.

En conclusión, el programa cumple con los requisitos planteados, validando entradas, manteniendo la coherencia de los datos y permitiendo gestionar el inventario de manera simple y efectiva.

Muchas gracias.
