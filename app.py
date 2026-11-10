import pandas as pd
import plotly.express as px
import streamlit as st

from finscope.calculations import (
    compound_interest,
    inflation_adjusted_value,
    investment_return,
    simple_interest,
)
from finscope.world_bank import fetch_indicator

st.set_page_config(page_title="FinScope | Finance & Economics", page_icon="📊", layout="wide")

st.title("FinScope")
st.caption("An open-source learning dashboard for personal finance and economic indicators.")
st.info(
    "Educational project, not investment, tax, or financial advice. "
    "Economic data is retrieved from the World Bank API when available."
)

page = st.sidebar.radio(
    "Explore FinScope",
    ["Overview", "Finance calculators", "Economic indicators", "About the project"],
)

if page == "Overview":
    st.subheader("Make financial and economic ideas easier to explore")
    c1, c2, c3 = st.columns(3)
    c1.metric("Project stage", "MVP")
    c2.metric("Core modules", "3")
    c3.metric("Data source", "World Bank")
    st.markdown(
        """
        **What you can do**
        - Calculate simple and compound interest.
        - Estimate investment returns.
        - Understand how inflation changes purchasing power.
        - Explore GDP growth, inflation and unemployment indicators.

        **Why FinScope exists:** to make reliable financial calculations and
        public economic data more accessible to students, learners and curious
        citizens.
        """
    )
    st.subheader("Start here")
    st.write("Choose **Finance calculators** in the sidebar to try the tools.")

elif page == "Finance calculators":
    st.subheader("Finance calculators")
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Simple interest", "Compound interest", "Investment return", "Inflation"]
    )

    with tab1:
        st.markdown("#### Simple interest")
        p = st.number_input("Principal", min_value=0.0, value=10000.0, step=1000.0, key="si_p")
        r = st.number_input("Annual interest rate (%)", min_value=0.0, value=7.0, step=0.5, key="si_r")
        t = st.number_input("Time (years)", min_value=0.0, value=3.0, step=0.5, key="si_t")
        interest = simple_interest(p, r, t)
        st.metric("Interest earned", f"₹{interest:,.2f}")
        st.metric("Final amount", f"₹{p + interest:,.2f}")

    with tab2:
        st.markdown("#### Compound interest")
        p = st.number_input("Initial amount", min_value=0.0, value=10000.0, step=1000.0, key="ci_p")
        r = st.number_input("Annual rate (%)", min_value=0.0, value=8.0, step=0.5, key="ci_r")
        t = st.number_input("Years", min_value=0.0, value=5.0, step=1.0, key="ci_t")
        n = st.selectbox("Compounding frequency", [1, 2, 4, 12, 365], format_func=lambda x: {
            1: "Annually", 2: "Half-yearly", 4: "Quarterly", 12: "Monthly", 365: "Daily"
        }[x])
        amount = compound_interest(p, r, t, n)
        st.metric("Future value", f"₹{amount:,.2f}")
        st.metric("Interest earned", f"₹{amount-p:,.2f}")

    with tab3:
        st.markdown("#### Investment return")
        initial = st.number_input("Initial investment", min_value=0.0, value=25000.0, step=1000.0)
        final = st.number_input("Current/final value", min_value=0.0, value=30000.0, step=1000.0)
        result = investment_return(initial, final)
        if result is None:
            st.warning("Enter an initial investment greater than zero.")
        else:
            st.metric("Total return", f"{result:.2f}%")
            st.metric("Profit / loss", f"₹{final-initial:,.2f}")

    with tab4:
        st.markdown("#### Inflation and purchasing power")
        amount = st.number_input("Amount today (₹)", min_value=0.0, value=10000.0, step=1000.0)
        inflation = st.number_input("Annual inflation (%)", min_value=0.0, value=5.0, step=0.5)
        years = st.number_input("Number of years", min_value=0.0, value=5.0, step=1.0)
        future_cost = inflation_adjusted_value(amount, inflation, years)
        st.metric("Equivalent future cost", f"₹{future_cost:,.2f}")
        st.caption("This estimates the future amount needed to buy the same basket of goods.")

elif page == "Economic indicators":
    st.subheader("Explore World Bank indicators")
    st.write("Select an indicator and country. The app retrieves annual observations from the World Bank API.")
    country_options = {
        "India": "IND",
        "United States": "USA",
        "United Kingdom": "GBR",
        "Singapore": "SGP",
        "Japan": "JPN",
        "Germany": "DEU",
        "Brazil": "BRA",
        "South Africa": "ZAF",
    }
    country = st.selectbox("Country", list(country_options))
    indicators = {
        "GDP growth (annual %)": "NY.GDP.MKTP.KD.ZG",
        "Inflation, consumer prices (annual %)": "FP.CPI.TOTL.ZG",
        "Unemployment (% of labour force)": "SL.UEM.TOTL.ZS",
        "GDP per capita (current US$)": "NY.GDP.PCAP.CD",
    }
    indicator_label = st.selectbox("Indicator", list(indicators))
    start_year, end_year = st.slider("Year range", 1960, 2025, (2000, 2024))
    if st.button("Load data", type="primary"):
        with st.spinner("Retrieving data from the World Bank..."):
            try:
                df = fetch_indicator(country_options[country], indicators[indicator_label], start_year, end_year)
                if df.empty:
                    st.warning("No observations were returned for this selection.")
                else:
                    st.line_chart(df.set_index("year")["value"])
                    st.dataframe(df.sort_values("year", ascending=False), use_container_width=True)
                    st.download_button(
                        "Download observations as CSV",
                        df.to_csv(index=False).encode("utf-8"),
                        file_name=f"finscope_{country_options[country]}_{indicators[indicator_label]}.csv",
                        mime="text/csv",
                    )
                    st.caption("Source: World Bank Open Data API. Values may be revised by the source.")
            except Exception as exc:
                st.error(f"Could not load the data. Check your internet connection and try again. Details: {exc}")

else:
    st.subheader("About FinScope")
    st.markdown(
        """
        FinScope is an early-stage open-source project intended to help people
        learn about finance and explore public economic data.

        ### Principles
        - **Transparency:** show where data comes from.
        - **Accessibility:** explain concepts in plain language.
        - **Reproducibility:** keep calculations testable and documented.
        - **Community:** welcome thoughtful issues, feedback and contributions.

        ### Current limitations
        - Economic data requires an internet connection.
        - This MVP supports a small set of countries and indicators.
        - Calculators are educational estimates and do not include taxes, fees,
          changing rates, or individual circumstances.
        """
    )
    st.markdown("[Project documentation](https://github.com/) · [World Bank Open Data](https://data.worldbank.org/)")
