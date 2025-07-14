from yield_boost.yield_diagnosis import diagnose_yield

inputs = {
    "soil_fertility": st.selectbox("Soil Fertility", ["high", "medium", "low"]),
    "water_access": st.selectbox("Water Access", ["adequate", "moderate", "poor"]),
    "pest_control": st.selectbox("Pest Control Used", ["none", "basic", "organic"]),
    "crop_rotation": st.selectbox("Practicing Crop Rotation?", ["yes", "no"]),
    "seed_quality": st.selectbox("Seed Quality", ["certified", "unknown"])
}

if st.button("Diagnose"):
    findings, tips = diagnose_yield(inputs)
    for f in findings:
        st.warning(f)
    for t in tips:
        st.success(t)
