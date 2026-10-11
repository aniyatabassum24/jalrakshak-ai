import streamlit as st
import requests

st.set_page_config(
    page_title="JalRakshak AI",
    page_icon="🌧️",
    layout="wide"
)

# ====== CONFIG ======
API_KEY = "327f37c30e060a4155684109601a2c89" # <-- Your OpenWeather Key
CITY_MAP = {
    "Warangal": "Warangal,IN",
    "Hanamkonda": "Hanamkonda,IN", 
    "Kazipet": "Kazipet,IN"
}

# ====== FUNCTION TO GET LIVE RAIN ======
def get_live_rainfall(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        # Rain in last 1 hour, if available
        rain_1h = data.get("rain", {}).get("1h", 0)
        return round(rain_1h, 1)
    except:
        return 0.0 # fallback if API fails

# ====== HEADER ======
st.title("🌧️ JalRakshak AI")
st.subheader("Intelligent Urban Waterlogging Risk Assessment System")
st.write("Helping citizens assess potential waterlogging risks in Warangal, Hanamkonda, and Kazipet, Telangana.")
st.info("Prototype notice: Risk levels are estimates based on inputs + live data. Not verified flood predictions.")

# ====== SIDEBAR INPUTS ======
st.sidebar.header("📍 Location & Weather")

location = st.sidebar.selectbox("Select your location", ["Warangal", "Hanamkonda", "Kazipet"])

# NEW: Live data fetch
live_rain = get_live_rainfall(CITY_MAP[location])

st.sidebar.success(f"Live rainfall for {location}: {live_rain} mm in last 1hr")

rainfall = st.sidebar.number_input(
    "Expected rainfall next 24 hours (mm)",
    min_value=0.0,
    max_value=500.0,
    value=live_rain * 6, # estimate: 1hr * 6 as placeholder
    step=5.0,
    help="Auto-filled from live data. You can edit manually."
)

recent_rainfall = st.sidebar.number_input(
    "Rainfall in previous 24 hours (mm)",
    min_value=0.0,
    max_value=500.0,
    value=live_rain,
    step=5.0,
    help="Auto-filled from live data. You can edit manually."
)

drainage = st.sidebar.selectbox("Local drainage condition", ["Good", "Moderate", "Poor", "Unknown"])
previous_waterlogging = st.sidebar.selectbox("Previous waterlogging reports", ["None known", "Some reports", "Frequent reports", "Unknown"])

# ====== RISK LOGIC - SAME AS YOURS ======
if drainage == "Unknown" or previous_waterlogging == "Unknown":
    st.warning("Some local information is missing. Treat the result cautiously.")

score = 0
if rainfall >= 50: score += 3
elif rainfall >= 25: score += 2
elif rainfall >= 10: score += 1

if recent_rainfall >= 50: score += 2
elif recent_rainfall >= 25: score += 1

if drainage == "Poor": score += 2
elif drainage == "Moderate": score += 1

if previous_waterlogging == "Frequent reports": score += 2
elif previous_waterlogging == "Some reports": score += 1

if score >= 6:
    risk = "HIGH 🔴"
    recommendation = "Avoid known waterlogged roads. Check local advisories and never enter floodwater."
elif score >= 3:
    risk = "MEDIUM 🟡"
    recommendation = "Monitor weather and local reports. Allow extra travel time and use caution."
else:
    risk = "LOW 🟢"
    recommendation = "Continue monitoring. Low estimated risk does not guarantee road safety."

# ====== MAIN DASHBOARD ======
st.divider()
left, middle, right = st.columns(3)
with left: st.metric("📍 Selected location", location)
with middle: st.metric("🌧️ Forecast rainfall input", f"{rainfall:.1f} mm")
with right: st.metric("💧 Estimated risk", risk)

st.subheader("🛡️ Safety recommendation")
st.write(recommendation)

st.subheader("📊 Assessment details")
st.write(f"- Live 1hr rainfall from API: {live_rain:.1f} mm")
st.write(f"- Previous 24-hour rainfall input: {recent_rainfall:.1f} mm")
st.write(f"- Drainage condition: {drainage}")
st.write(f"- Previous waterlogging reports: {previous_waterlogging}")
st.write(f"- Internal risk score: {score}")

st.caption("JalRakshak AI Hackathon Prototype | Uses OpenWeather API + Manual inputs. Not IMD official data.")
