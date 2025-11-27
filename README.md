# MS-Concesionarios - Microservicio de Concesionarios

Microservicio para manejo de datos de concesionarios del sistema CaFES Check.

## Características

- Consulta de concesionarios por código QR
- Creación y actualización de concesionarios
- Validación de datos desde archivo de texto
- API REST compatible con FastAPI

## Endpoints Disponibles

### Consultas
- `GET /concesionarias/qr/{numAutorizado}` - Obtener concesionario por número autorizado
- `GET /concesionarias/todas` - Obtener todos los concesionarios

### Gestión
- `POST /concesionarias/crear` - Crear nuevo concesionario
- `PUT /concesionarias/{numAutorizado}` - Actualizar concesionario existente

## Instalación

1. Ejecutar `instalar_dependencias.bat` o:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar el servidor:
   ```bash
   python run.py
   ```

3. El servidor estará disponible en `http://localhost:8001`

## Estructura de Datos

Los concesionarios se almacenan en formato texto en el archivo `concesionario_001.txt`:

```
Id_concesionaria: 1
numAutorizado: 1062
dependencia: Facultad de Estudios Superiores Acatlán
autorizado: Grupo Mondainz 8, S.A. de C.V.
horario_atencion: Lunes a viernes de 8:00 a 20:30 horas y sábados de 8:00 a 16:00 horas.
```

## Integración con Frontend

Este microservicio se integra con el frontend caFES-Check a través de los endpoints definidos en `api-config.js`:

- `ConcesionariaAPI.obtenerPorQR(numAutorizado)` → `GET /concesionarias/qr/{numAutorizado}`
- `ConcesionariaAPI.crear(concesionaria)` → `POST /concesionarias/crear`
- `ConcesionariaAPI.obtenerTodas()` → `GET /concesionarias/todas`
