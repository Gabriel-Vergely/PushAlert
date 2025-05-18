# PushAlert Webhook Server

Este proyecto inicia un servidor FastAPI que actúa como receptor de Webhooks para eventos `push` de GitHub.

---

## 🚀 Requisitos

- Python 3.8 o superior
- `uvicorn`
- `fastapi`
- Conexión SSH para tunelizar con [Serveo](https://serveo.net)

---

## 🛠 Instalación

1. Instala dependencias:

```bash
pip install fastapi uvicorn
```

---

## Iniciar servidor

```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
ssh -R 80:localhost:5000 serveo.net
```

---

## 🛠 Configurar Webhook en GitHub

### 1. Abre la configuración del repositorio:

- Ve a tu repositorio en GitHub
- Haz clic en **Settings** (esquina superior derecha)
- En el menú lateral izquierdo, haz clic en **Webhooks**
- Pulsa **"Add webhook"**

---

### 2. Completa el formulario con esta configuración:

| Campo                        | Valor                                                                                      |
|-----------------------------|---------------------------------------------------------------------------------------------|
| **Payload URL**             | `https://xxxxxx.serveo.net/webhook` *(tu URL pública generada por Serveo)*                 |
| **Content type**            | `application/json`                                                                         |
| **Secret**                  | *(opcional, puedes dejarlo vacío durante el desarrollo)*                                   |
| **SSL verification**        | `Disable (not recommended)` ⚠️ *(debes desactivar si usas Serveo, que no tiene certificado)* |
| **Which events trigger it** | `Just the push event` *(activa solo los eventos push)*                                     |
| **Active**                  | ✅ **Marcado** *(para que el webhook esté habilitado)*                                     |

---

GitHub mostrará este mensaje:

> *"We'll send a POST request to the URL below with details of any subscribed events. You can also specify which data format you'd like to receive (JSON, x-www-form-urlencoded, etc). More information can be found in our developer documentation."*

Esto significa que GitHub enviará una solicitud POST a la URL que pongas, con la información del evento que ocurra (como un `push`), en el formato que tú elijas (`application/json` es el recomendado).

---

### ✅ Finaliza

- Pulsa el botón **Add webhook**
- Luego haz un `git push` o haz clic en **"Redeliver"** en la sección del webhook para probarlo

Mira los logs en tu servidor FastAPI para verificar que llegó el evento.

