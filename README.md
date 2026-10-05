# Sentia Intelligence from Conversations — Backend 0.3.39

Backend Python HTTPS para las integraciones de Sentia.

## Despliegue en Render

1. Crea un repositorio independiente con el contenido de este ZIP.
2. En Render crea un Web Service desde ese repositorio.
3. `render.yaml` define el build y el health check.
4. Configura `SENTIA_ALLOWED_ORIGINS` con el origen exacto de GitHub Pages, por ejemplo `https://usuario.github.io`.
5. Configura los secretos como variables de entorno de Render; nunca los subas al repositorio.
6. Copia la URL HTTPS resultante en Sentia → Configuración → Backend seguro.

## Cohere

La API key puede configurarse desde Sentia → Integraciones → Cohere. El backend recibe la clave y no la devuelve al navegador ni la persiste en IndexedDB/localStorage.

También puede provisionarse `COHERE_API_KEY` como secreto del servicio.
