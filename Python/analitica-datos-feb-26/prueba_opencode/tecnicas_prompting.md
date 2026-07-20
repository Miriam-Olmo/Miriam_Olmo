Los 5 componentes de un prompt 

**Qué decir:**

> "Un prompt es básicamente un briefing. Y como todo buen briefing, tiene partes. No hace falta usarlas todas siempre, pero conocerlas te ayuda a saber qué le falta a un prompt cuando el resultado no es el que esperabas."

Presentar los 5 componentes uno a uno:

**1. Rol:** Qué experto o personaje debe encarnar la IA.
> "Si le dices a ChatGPT 'eres el responsable de marketing de un periódico digital', calibra su lenguaje, su tono y su nivel de profundidad hacia ese perfil. Sin rol, la IA responde desde una posición genérica que suele ser menos útil."

**2. Tarea:** La acción concreta con un verbo claro.
> "La tarea tiene que tener un verbo de acción y un objeto específico. 'Redacta 3 asuntos de email' es una buena tarea. 'Ayúdame con los emails' no lo es."

**3. Contexto:** El fondo, las restricciones, los datos relevantes.
> "Este es el componente que más impacto tiene en la calidad del resultado. El 80% de las mejoras en los resultados vienen de añadir más y mejor contexto."

**4. Formato / Output:** Cómo quieres recibir la respuesta.
> "Especifica si quieres una tabla, una lista, un email completo, cuántas opciones, cuántas palabras máximo. Si no lo dices, la IA elige por ti y no siempre acierta."

**5. Público objetivo:** A quién va dirigida la respuesta que genera la IA.
> "No es lo mismo escribir para suscriptores activos que para lectores que se están dando de baja. Decirle a la IA quién es el destinatario final cambia mucho el resultado."

---

## Bloque 3 — Framework ROLE + TASK + CONTEXT + OUTPUT

**Qué decir:**

> "El primer framework que vais a aprender es el más versátil y el que vais a usar más. Lo llamamos ROLE + TASK + CONTEXT + OUTPUT."

**Prompt débil:** `Escríbeme un email para suscriptores.`

**Prompt con framework:**
```
[ROLE] Eres el responsable de marketing de un periódico digital español.
[TASK] Escribe un email de reactivación para suscriptores que llevan 60 días sin abrir la newsletter.
[CONTEXT] El periódico cubre política y economía nacional. Tono cercano y directo. Sin palabras como "exclusivo" o "imperdible". El lector paga 4,99€/mes.
[OUTPUT] Asunto + cuerpo del email. Máximo 120 palabras. Incluye una llamada a la acción al final.

```