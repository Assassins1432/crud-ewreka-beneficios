# CRUD Ewreka Beneficios

Este proyecto es una API CRUD para gestionar beneficios, construida con FastAPI y desplegada en Vercel.

## Estructura del Proyecto

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu-usuario/crud-ewreka-beneficios.git
    cd crud-ewreka-beneficios
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Abre tu navegador y ve a [`http://127.0.0.1:8000/docs`]("Go to definition") para ver la documentación interactiva de la API.

## Despliegue

Este proyecto está configurado para ser desplegado en Vercel. El archivo [`vercel.json`] ya está configurado para usar el entorno de Python.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.