# Ventilator-Guide-App (prototipo)

Prototipo interactivo desarrollado en **Streamlit** que guía paso a paso en la programación inicial y comprobaciones básicas de un ventilador mecánico. Diseñado como herramienta educativa para médicos no especialistas en ambientes de emergencia/guardia.

> **IMPORTANTE**: Esta aplicación es un **prototipo educativo**. No sustituye la evaluación clínica ni la supervisión por parte de un especialista en terapia intensiva. Usar sólo como apoyo y confirmar siempre con un intensivista.

---

## Características
- Cálculo automático de PBW (peso corporal predicho) a partir de altura y sexo.
- Sugerencia de Vt protectora (6 ml/kg PBW, ajustable).
- Propuesta de PEEP según FiO₂ (tabla simplificada).
- Cálculo y alertas de seguridad: Pplat, Driving Pressure (ΔP).
- Checklist de seguridad y export simple del resumen (feature a implementar).

---

## Contenido del repo
- `ventilador_app.py` — archivo principal (Streamlit).
- `requirements.txt` — dependencias.
- `README.md` — este archivo.
- `.gitignore`

---

## Requisitos
- Python 3.8+  
- Streamlit (ver `requirements.txt`)

---

## Ejecutar localmente (desarrollador)
1. Cloná o descargá el repo.  
2. Instalá dependencias:
   ```bash
   pip install -r requirements.txt
