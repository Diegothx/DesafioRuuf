# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Deja acá el link a tu video explicando tu solución con tus palabras

https://youtu.be/j0mBRWfDkTw

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:



### Bonus Implementado
*[Indica cuál bonus implementaste: Opción 1 (techo triangular) o Opción 2 (rectángulos superpuestos)]*

Resolvi Opción 2 (rectángulos superpuestos)
### Explicación del Bonus
*[Explica cómo adaptaste tu algoritmo para resolver el bonus]*
En primer lugar, se agregaron los parámetros overlapW y overlapH a la función calculate_panels para representar el rectángulo que queda solapado. Adicionalmente, cree pruebas en test_cases_bonus.json para verificar el correcto funcionamiento de la función con los nuevos parámetros. Estas pruebas fueron con casos que me asegure de poder resolver manualmente para verificar que el resultado de la función era correcto.

Para resolver el bonus, se utilizó como base la misma función recursiva que busca rellenar el techo según distintas orientaciones de los paneles. La diferencia es que ahora, al momento de iniciar el algoritmo, en lugar de comenzar con una grilla que representa un techo rectangular vacío, se inicializa una grilla rectangular de tamaño (2 * roofW - overlapW) por (2 * roofH - overlapH), y se marca como ocupada toda el área que quedaría fuera de este techo. De esta forma, el algoritmo funciona exactamente igual que antes, sin considerar que se trata de dos rectángulos superpuestos, tratándolos como si fuera un techo rectangular normal con un área ocupada.
 
---

## 🤔 Supuestos y Decisiones

*[Si tuviste que tomar algún supuesto o decisión de diseño, explícalo aquí]*

Como la geometria del techo sigue siendo simetrica, se asume que el solapamiento se da en la parte inferior derecha del techo, para definir concretamente la forma de la grilla.


