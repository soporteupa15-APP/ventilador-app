import streamlit as st

st.title("Asistente de Programación de Ventilador Mecánico")

# Datos de entrada
sexo = st.selectbox("Sexo del paciente", ["Hombre", "Mujer"])
altura = st.number_input("Altura del paciente (cm)", min_value=100, max_value=220, step=1)

# Cálculo PBW
if sexo == "Hombre":
    pbw = 50 + 0.91 * (altura - 152.4)
else:
    pbw = 45.5 + 0.91 * (altura - 152.4)

st.write(f"**Peso Corporal Predicho (PBW): {pbw:.1f} kg**")

# Volumen corriente sugerido
vt = pbw * 6
st.write(f"**Volumen corriente recomendado (6 ml/kg): {vt:.0f} ml**")
st.write(f"Rango aceptable: {pbw*4:.0f} – {pbw*8:.0f} ml")

# Otros parámetros iniciales
fio2 = st.slider("FiO₂ inicial", 0.21, 1.0, 1.0, 0.01)
peep = st.number_input("PEEP inicial (cmH₂O)", 5, 20, 5)
fr = st.slider("Frecuencia respiratoria (rpm)", 10, 30, 16)

# Alertas de seguridad
pplat = st.number_input("Presión meseta (Pplat, cmH₂O)", 0, 60, 25)
dp = pplat - peep
if pplat > 30:
    st.error("⚠️ Pplat > 30 cmH₂O → Reducir Vt y consultar especialista")
if dp > 15:
    st.warning("⚠️ Driving Pressure > 15 cmH₂O → Reevaluar parámetros")

# Resumen
st.subheader("Resumen de configuración sugerida:")
st.write(f"- Vt: {vt:.0f} ml ({vt/pbw:.1f} ml/kg PBW)")
st.write(f"- FR: {fr} rpm")
st.write(f"- FiO₂: {fio2:.2f}")
st.write(f"- PEEP: {peep} cmH₂O")
