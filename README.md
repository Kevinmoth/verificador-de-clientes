# verificador-de-clientes
# Bot y Backend para Discord: Asignación de Roles Automatica

---

Este repositorio contiene un **Backend** , construido con **Express.js**, y un **bot de Discord** que trabajan en conjunto. Su propósito principal es **escuchar solicitudes POST** para **asignar roles a usuarios** de forma automatizada. ¡Es una herramienta ideal para optimizar la gestión de tu comunidad!

---

## 🚀 Integración y Uso

Este sistema es perfecto para **integrarlo con sistemas externos** para clientes o usuarios verificados. Imagina, por ejemplo, conectar tu tienda online o tu plataforma de suscripciones para que tus usuarios reciban roles específicos en Discord tras una acción.

---

## 📦 Formato de Solicitud POST Requerido

Para que el backend procese correctamente las solicitudes y asigne los roles, debe recibir un objeto **JSON** con la siguiente estructura exacta:

```json
{
  "discord_id": "id de dc",
  "compra_verificada": true
}
