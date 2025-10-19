# 🧭 Task Tracker CLI

Una herramienta de línea de comandos para gestionar tus tareas de forma simple, rápida y sin dependencias externas.

---

## 🚀 Características

- ✅ Agregar tareas
- 📝 Actualizar descripción de tareas
- 🗑️ Eliminar tareas
- 📌 Marcar tareas como "en progreso" o "completadas"
- 📋 Listar todas las tareas o filtrarlas por estado
- 💾 Persistencia en archivo `tasks.json` sin necesidad de base de datos

---

## 🛠️ Requisitos

- Python 3.x
- No se utilizan librerías externas
- Compatible con Windows, macOS y Linux

---

## 📦 Instalación

```bash
git clone https://github.com/Yovanis/task-tracker.git
cd task-tracker
python -m venv venv
# Activar entorno virtual
# En PowerShell:
.\venv\Scripts\Activate.ps1
# En Bash:
source venv/bin/activate
```

## 📋 Uso

```bash
python task_cli.py add "Comprar leche"
python task_cli.py update 1 "Comprar leche y pan"
python task_cli.py delete 1
python task_cli.py mark-in-progress 2
python task_cli.py mark-done 2
python task_cli.py list
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

## 📁 Estructura del JSON
El archivo `tasks.json` tiene la siguiente estructura:

```json
{
  "id": 1,
  "description": "Comprar leche",
  "status": "todo",
  "createdAt": "2025-10-18T22:30:00",
  "updatedAt": "2025-10-18T22:30:00"
}
```
## 🧠 Buenas prácticas
- Usa IDs enteros para referenciar tareas
- No edites tasks.json manualmente
- El archivo se crea automáticamente si no existe

## 🧪 Testing
Puedes probar cada comando desde la terminal. El archivo  se actualizará automáticamente.

## 📄 Licencia
Este proyecto es de uso libre para fines educativos y personales.

## 🔗 Proyecto en GitHub

Puedes ver el código fuente y contribuir en:  
[https://github.com/yovidev/task-tracker](https://github.com/yovidev/task-tracker)
