import streamlit as st

st.set_page_config(
    page_title="JalRakshak AI",
    page_icon="🌧️",
    layout="wide"
)

st.title("🌧️ JalRakshak AI")
st.subheader(
    "Intelligent Urban Waterlogging Risk Assessment System"
)

st.write(
    "Helping citizens assess potential waterlogging risks "
    "in Warangal, Hanamkonda, and Kazipet, Telangana."
)

st.info(
    "Prototype notice: Risk levels are estimates based on "
    "user-provided inputs, not verified flood predictions."
)

# Sidebar inputs
st.sidebar.header("📍 Location & Weather")

location = st.sidebar.selectbox(
    "Select your location",
    [
        "Warangal",
        "Hanamkonda",
        "Kazipet"
    ]
)

rainfall = st.sidebar.number_input(
    "Expected rainfall (mm over the next 24 hours)",
    min_value=0.0,
    max_value=500.0,
    value=20.0,
    step=5.0
)

recent_rainfall = st.sidebar.number_input(
    "Rainfall in the previous 24 hours (mm)",
    min_value=0.0,
    max_value=500.0,
    value=10.0,
    step=5.0
)

drainage = st.sidebar.selectbox(
    "Local drainage condition",
    ["Good", "Moderate", "Poor", "Unknown"]
)

previous_waterlogging = st.sidebar.selectbox(
    "Previous waterlogging reports",
    ["None known", "Some reports", "Frequent reports", "Unknown"]
)

# Estimate risk
if drainage == "Unknown" or previous_waterlogging == "Unknown":
    st.warning(
        "Some local information is missing. "
        "Treat the result cautiously."
    )

score = 0

if rainfall >= 50:
    score += 3
elif rainfall >= 25:
    score += 2
elif rainfall >= 10:
    score += 1

if recent_rainfall >= 50:
    score += 2
elif recent_rainfall >= 25:
    score += 1

if drainage == "Poor":
    score += 2
elif drainage == "Moderate":
    score += 1

if previous_waterlogging == "Frequent reports":
    score += 2
elif previous_waterlogging == "Some reports":
    score += 1

if score >= 6:
    risk = "HIGH"
    recommendation = (
        "Avoid known waterlogged roads where possible. "
        "Check local advisories and never enter floodwater."
    )
elif score >= 3:
    risk = "MEDIUM"
    recommendation = (
        "Monitor weather and local reports. "
        "Allow extra travel time and use caution."
    )
else:
    risk = "LOW"
    recommendation = (
        "Continue monitoring conditions. "
        "Low estimated risk does not guarantee road safety."
    )

# Main dashboard
st.divider()

left, middle, right = st.columns(3)

with left:
    st.metric("📍 Selected location", location)

with middle:
    st.metric("🌧️ Forecast rainfall input", f"{rainfall:.1f} mm")

with right:
    st.metric("💧 Estimated risk", risk)

st.subheader("🛡️ Safety recommendation")
st.write(recommendation)

st.subheader("📊 Assessment details")

st.write(f"- Previous 24-hour rainfall input: {recent_rainfall:.1f} mm")
st.write(f"- Drainage condition: {drainage}")
st.write(f"- Previous waterlogging reports: {previous_waterlogging}")
st.write(f"- Internal risk score: {score}")

st.caption(
    "JalRakshak AI Hackathon Prototype | "
    "Rule-based assessment, not a validated predictive model. "
    "Rainfall inputs are manually entered and are not live weather data."
)
