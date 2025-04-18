import streamlit as st
import requests
import json

# ---------------------- Fetch Function ----------------------
def fetch_country_data(country_name):
    URL = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        currency = ", ".join(country_data.get("currencies", {}).keys())
        region = country_data.get("region", "N/A")
        flag_url = country_data.get("flags", {}).get("png", "")
        return name, capital, population, area, currency, region, flag_url
    else:
        return None

# ---------------------- Main App ----------------------
def main():
    st.set_page_config(page_title="Country Info App", page_icon="🌍", layout="centered")
    st.markdown("## 🌍 Country Information App")
    st.markdown("Enter the name of a country to get real-time info below 👇")

    # st.markdown("---")
    country_name = st.text_input("🔎 Enter a country name:")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region, flag_url = country_info

            st.success(f"📌 Showing information for **{name}**")
            if flag_url:
                st.image(flag_url, width=150)

            st.markdown("### 🗺️ Country Details")
            st.write(f"**🏛️ Capital:** {capital}")
            st.write(f"**👥 Population:** {population:,}")
            st.write(f"**📏 Area:** {area:,} km²")
            st.write(f"**💰 Currency:** {currency}")
            st.write(f"**🌐 Region:** {region}")
        else:
            st.error("❌ Country not found. Please check the spelling and try again.")

    st.markdown("---")
    st.caption("✨ Crafted with ❤️ by Nisha Nazar")


if __name__ == "__main__":
    main()
