# JalRakshak AI 🌧️

### Urban Waterlogging Risk Assessment for Telangana

JalRakshak AI helps citizens in Warangal, Hanamkonda, and Kazipet check waterlogging risk instantly using live rainfall + local conditions.

## Features
- **Live Data**: Auto-fetches rainfall from OpenWeather API
- **Risk Score**: LOW 🟢 / MEDIUM 🟡 / HIGH 🔴 warning
- **Safety Tips**: Clear recommendations for citizens
- **Manual Override**: Edit rainfall if you have local news
- **Mobile Ready**: Works on phone via Streamlit Cloud

## Tech Stack
`Python` | `Streamlit` | `OpenWeather API` | `Git

### 1. Problem Statement
Urban waterlogging causes major disruptions in Warangal, Hanamkonda, and Kazipet during monsoons. Citizens lack a quick way to check if their route/area is at risk of flooding based on current rainfall + local drainage conditions.

JalRakshak AI provides an instant risk assessment using live weather data + citizen inputs to help people avoid waterlogged areas.

## 2. Proposed Solution
A web-based Streamlit application that:
1. Fetches live rainfall data from OpenWeather API for the 3 cities
2. Takes manual inputs: Expected rainfall, Drainage condition, Previous waterlogging history
3. Calculates a risk score and gives LOW / MEDIUM / HIGH warning
4. Provides safety recommendations to citizens

## 3. Key Features
- *Live Govt Data*: Auto-fetches rainfall for Warangal, Hanamkonda, Kazipet using OpenWeather API
- *Manual Override*: Users can edit rainfall if they have local news/info
- *Rule-based AI*: Risk scoring based on rainfall, drainage, and history
- *Safety First*: Clear recommendations: Avoid roads, Monitor, or Safe to travel
- *Mobile Friendly*: Works on phone via Streamlit Cloud

## 4. Tech Stack
| Component | Technology Used |
| --- | --- |
| Frontend | Streamlit |
| Backend Logic | Python |
| Live Data API | OpenWeather API |
| Deployment | Streamlit Cloud + GitHub |

## 5. How to Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/aniyatabassum24/jalrakshak-ai.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
## 6. How to Use
1. Select your location: Warangal / Hanamkonda / Kazipet
2. Check auto-filled live rainfall in sidebar
3. Enter expected rainfall, drainage condition, and history
4. View Risk Level and Safety Recommendation on dashboard

## 7. Project Structure
jalrakshak-ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
## 8. Future Improvements
- Integrate IMD rainfall radar data
- Add map with historical waterlogging hotspots
- Citizen reporting feature with photo upload
- SMS/WhatsApp alerts for HIGH risk areas

## 9. Disclaimer
This is a hackathon prototype. Risk levels are estimates based on user inputs and API data. Not an official flood prediction from IMD or Govt. Always follow local authority advisories.

## 10. Team
Team Name: JalRakshak-AI 
Member: Aniya Tabassum
