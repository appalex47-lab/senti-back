# Sentia Intelligence from Conversations — Backend 0.3.40

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

## Corrección 0.3.40 — Cohere SDK

Se eliminó la validación basada en `check_api_key(...)` que provocaba el error de la SDK en el flujo de configuración. La validación ahora utiliza el mismo cliente `cohere.ClientV2` y una llamada mínima a `Chat V2`, que es el patrón documentado actualmente por Cohere.

El catálogo autenticado de modelos también utiliza `ClientV2`.

No se almacenan API keys en el frontend, IndexedDB ni localStorage.
