Marcar una Combinación de Ubicación-Categoría como Revisada:

Para marcar una combinación de ubicación-categoría como revisada, realiza una solicitud PUT a la ruta /location_category_review/{location_name}/{category_name}/.

Ejemplo:

http

PUT /location_category_review/Location1/Category1/

Mostrar Registros Guardados:

Para mostrar registros guardados, realiza una solicitud GET a la ruta /show_records/ con parámetros opcionales offset y limit para paginar los resultados.

Ejemplo:

http

GET /show_records/?offset=0&limit=10

Comprobación de la Funcionalidad

    Se han realizado pruebas exhaustivas para garantizar el funcionamiento correcto de todas las funcionalidades.
    Se pueden encontrar ejemplos de pruebas unitarias en el directorio tests/.

Repositorio en Línea

El código fuente de este proyecto se encuentra disponible en GitHub.

css


Ahora la documentación incluye ejemplos de uso resaltados para cada una de las funcionalidades principales del API, lo que facilita a los usuarios entender cómo utilizarlo.
