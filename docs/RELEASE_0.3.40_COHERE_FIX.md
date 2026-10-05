# Sentia Backend 0.3.40 — Cohere SDK Fix

## Problema corregido

La configuración de Cohere fallaba con:

`Since python sdk cohere==5.0.0, the function check_api_key(...) has been deprecated.`

La causa era que `CohereService.check_connection()` creaba un cliente V1 (`cohere.Client`) y llamaba `check_api_key()`.

## Corrección

- Validación de credenciales mediante `cohere.ClientV2`.
- La validación usa una llamada mínima a `Chat V2`.
- El catálogo autenticado de modelos utiliza `ClientV2`.
- La API key continúa siendo exclusiva del backend.
- No se guarda ninguna API key en IndexedDB/localStorage.
- No se cambia el contrato del frontend ni la URL pública del backend.

## Validación

- `pytest -q`: 3 passed.
- `py_compile`: OK.
- Versión backend: `0.3.40`.

## Despliegue en Render

Reemplazar el contenido del repositorio backend por este release y hacer un nuevo deploy.

No es necesario cambiar:

- `SENTIA_ALLOWED_ORIGINS`
- `SENTIA_TOKEN_ENCRYPTION_KEY`
- `COHERE_API_KEY`
- `COHERE_MODEL`
- Start Command: `python -m python.connection_server`
- Health Check: `/api/health`

Después del deploy:

1. Abrir `/api/health` y confirmar `version: 0.3.40`.
2. En Sentia → Integraciones → Cohere, volver a configurar la API key.
3. Confirmar que la configuración responde correctamente.
4. Probar `/api/cohere/test` desde la aplicación.

La API key nunca debe compartirse en el chat ni subirse a GitHub.
