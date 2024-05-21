# Map My World API

Este proyecto implementa una API RESTful utilizando FastAPI para gestionar ubicaciones, categorías y revisiones de ubicación-categoría.

La API permite gestionar ubicaciones, categorías y revisiones de ubicación-categoría. Los usuarios pueden crear nuevos recursos, obtener recomendaciones de exploración, marcar combinaciones como revisadas y mostrar registros guardados. La documentación facilita el uso y la comprensión de la API.
La API está diseñada para ser fácilmente utilizada e integrada en aplicaciones que requieren funcionalidades relacionadas con la exploración y revisión de ubicaciones en diferentes categorías. Además, la documentación proporcionada en el archivo README.md facilita a los usuarios entender cómo utilizar la API y realizar las solicitudes adecuadas.

```css
Este resumen proporciona una descripción concisa de la API y sus características principales, lo que ayuda a los usuarios a entender rápidamente su funcionalidad y cómo utilizarla.
```

El repositorio se encuentra en Línea. En la documentación se incluye ejemplos de uso resaltados para cada una de las funcionalidades principales del API.
```css
La documentación incluye ejemplos de uso resaltados para cada una de las funcionalidades principales del API, lo que facilita a los usuarios entender cómo utilizarlo.
```

## Instrucciones de Uso

1. **Instalación**:
   - Asegúrate de tener Python y FastAPI instalados en tu sistema.
   - Clona este repositorio en tu máquina local.
   - Crea y activa un entorno virtual:
     ```bash
     python -m venv venv
     source venv/bin/activate  # En sistemas Unix/Mac
     .\venv\Scripts\activate   # En sistemas Windows
     ```
   - Instala las dependencias del proyecto:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecución**:
   - Ejecuta el servidor de desarrollo utilizando Uvicorn:
     ```bash
     uvicorn main:app --reload
     ```

     * Si se presentan inconvenientes con el anterior comando, usar el sugerido en la documentación oficial de FastAPI:
     ```bash
     fastapi dev main.py
     ```

## Documentación del API

- Puedes acceder a la documentación interactiva del API visitando `/docs` en tu navegador después de iniciar el servidor. Por ejemplo, si estás ejecutando el servidor en `localhost`, puedes visitar `http://localhost:8000/docs`.

- La documentación describe todas las rutas disponibles, los modelos de datos esperados y los parámetros de consulta.

## Ejemplos de Uso

### Obtener Recomendaciones de Exploración:

Para obtener recomendaciones de exploración, realiza una solicitud GET a la ruta `/exploration_recommendations/`.

Ejemplo:
```http
GET /exploration_recommendations/
 ```

Marcar una Combinación de Ubicación-Categoría como Revisada:

Para marcar una combinación de ubicación-categoría como revisada, realiza una solicitud PUT a la ruta /location_category_review/{location_name}/{category_name}/.

Ejemplo:
```http
PUT /location_category_review/Location1/Category1/
```

## Ejemplos de JSON para Crear Locaciones y Categorías

JSON para Crear una Ubicación:
```json
{
  "name": "Restaurante La Trattoria",
  "category": "Restaurante Italiano",
  "longitude": -74.005941,
  "latitude": 40.712784
}
```
JSON para Crear una Categoría:
```json
{
  "name": "Museo de Historia Natural"
}
```
Comprobación de la Funcionalidad

    Se han realizado pruebas exhaustivas para garantizar el funcionamiento correcto de todas las funcionalidades.
    Se pueden encontrar ejemplos de pruebas unitarias en el directorio tests/.
