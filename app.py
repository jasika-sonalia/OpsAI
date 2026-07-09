import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Agentic Facility Ops AI", layout="wide")

# --- MOCK DATA GENERATION FOR ANALYTICS ---
@st.cache_data
def get_mock_data():
    np.random.seed(42)
    dates = pd.date_range(start="2026-06-01", end="2026-07-07", freq='D')
    
    energy_df = pd.DataFrame({
        'Date': dates,
        'Energy Consumption (kWh)': np.random.randint(300, 500, size=len(dates)),
        'Cost Savings (Rs)': np.random.randint(3000, 5000, size=len(dates))
    })
    
    maintenance_df = pd.DataFrame({
        'Date': dates,
        'Active Work Orders': np.random.randint(5, 25, size=len(dates)),
        'Downtime Hours': np.random.uniform(0, 4, size=len(dates))
    })
    
    occupancy_df = pd.DataFrame({
        'Date': dates,
        'Avg Space Utilization (%)': np.random.randint(55, 85, size=len(dates)),
        'Desk Bookings': np.random.randint(100, 250, size=len(dates))
    })
    
    security_df = pd.DataFrame({
        'Date': dates,
        'Threats Detected': np.random.choice([0, 1, 2], size=len(dates), p=[0.8, 0.15, 0.05]),
        'Incidents Resolved': np.random.randint(0, 5, size=len(dates))
    })
    
    return energy_df, maintenance_df, occupancy_df, security_df

energy_data, maint_data, occ_data, sec_data = get_mock_data()


# --- SESSION STATE MANAGEMENT ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'current_view' not in st.session_state:
    st.session_state.current_view = "Overview"


# --- VIEW 1: LOGIN PAGE ---
def show_login_page():
    st.markdown("<h2 style='text-align: center;'>Agentic Facility Ops AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Sign in to manage your facility operations</p>", unsafe_allow_html=True)
    
    _, col, _ = st.columns([1, 2, 1])
    with col:
        with st.form("login_form"):
            username_input = st.text_input("User ID / Email", value="Arjun Mehta")
            password_input = st.text_input("Password", type="password", value="password123")
            submit = st.form_submit_button("Sign In", use_container_width=True)
            
            if submit:
                if username_input and password_input:
                    st.session_state.logged_in = True
                    st.session_state.username = username_input
                    st.rerun()
                else:
                    st.error("Please enter both User ID and Password.")


# --- VIEW 2: MAIN DASHBOARD APPLICATION ---
def show_dashboard():
    # --- SIDEBAR NAV ---
    with st.sidebar:
        st.markdown("### 🌐 Facility Ops AI")
        st.write("---")
        
        options = ["Overview", "Energy Agent Analytics", "Maintenance Agent Analytics", "Occupancy Agent Analytics", "Security Agent Analytics"]
        
        default_index = 0
        if st.session_state.current_view in options:
            default_index = options.index(st.session_state.current_view)
            
        choice = st.radio("Navigation Menu", options, index=default_index)
        st.session_state.current_view = choice
        
        st.write("---")
        st.markdown(f"👤 **Logged in as:**\n`{st.session_state.username}`")
        st.caption("Role: Facility Manager")
        
        if st.button("Logout", use_container_width=True, type="secondary"):
            st.session_state.logged_in = False
            st.session_state.current_view = "Overview"
            st.rerun()

    # --- TOP HEADER BAR ---
    st.markdown("## 🏢 AI Agent Modules Dashboard")
    st.caption("Autonomous AI agents working together to optimize your facility operations.")
    st.write("---")

    # --- ROUTING LOGIC BASED ON NAVIGATION ---
    if st.session_state.current_view == "Overview":
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        with kpi1:
            st.metric(label="⚙️ Active Modules", value="4", delta="Running Smoothly")
        with kpi2:
            st.metric(label="📈 Avg. Efficiency Gain", value="12.4%", delta="+1.2% This Month")
        with kpi3:
            st.metric(label="⚡ Energy Savings", value="18.7%", delta="+0.5% Target")
        with kpi4:
            st.metric(label="💰 Cost Savings", value="Rs. 2.45L", delta="This Month")
            
        st.write("---")
        st.subheader("Available Autonomous AI Agents")
        
        # 1. Energy Agent
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            st.markdown("### ⚡ 1. Energy Agent")
            st.markdown("*Monitors and optimizes energy and utility consumption across facilities.*")
            st.markdown("- Check Energy Monitoring & Demand Forecasting\n- Check HVAC & Lighting Optimization")
        with c2:
            st.metric("Energy Savings This Month", "12.4%")
            st.metric("Cost Savings Generated", "Rs. 1.25L")
        with c3:
            st.write("")
            if st.button("View Energy Details", key="btn_eng", use_container_width=True):
                st.session_state.current_view = "Energy Agent Analytics"
                st.rerun()
        st.write("---")

        # 2. Maintenance Agent
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            st.markdown("### 🔧 2. Maintenance Agent")
            st.markdown("*Predicts equipment failures and automates maintenance workflows.*")
            st.markdown("- Check Equipment Health Monitoring & Predictive Maintenance\n- Check Automated Work Order Generation")
        with c2:
            st.metric("MTBF Improvement", "92%")
            st.metric("Work Orders Closed", "156")
        with c3:
            st.write("")
            if st.button("View Maintenance Details", key="btn_maint", use_container_width=True):
                st.session_state.current_view = "Maintenance Agent Analytics"
                st.rerun()
        st.write("---")

        # 3. Occupancy Agent
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            st.markdown("### 👥 3. Occupancy Agent")
            st.markdown("*Analyzes space utilization and optimizes workspace allocation.*")
            st.markdown("- Check Space Utilization Metrics & Heatmaps\n- Check Usage Forecasting")
        with c2:
            st.metric("Avg Space Utilization", "65%")
            st.metric("Space Optimization Rate", "18%")
        with c3:
            st.write("")
            if st.button("View Occupancy Details", key="btn_occ", use_container_width=True):
                st.session_state.current_view = "Occupancy Agent Analytics"
                st.rerun()
        st.write("---")

        # 4. Security Agent
        c1, c2, c3 = st.columns([2, 1, 1])
        with c1:
            st.markdown("### 🛡️ 4. Security Agent")
            st.markdown("*Monitors security systems and detects anomalies to ensure a safe environment.*")
            st.markdown("- Check Access Control Monitoring & Threat Detection\n- Check Video Analytics Anomaly Alerts")
        with c2:
            st.metric("Threat Detection Rate", "98.6%")
            st.metric("Incidents Resolved", "15")
        with c3:
            st.write("")
            if st.button("View Security Details", key="btn_sec", use_container_width=True):
                st.session_state.current_view = "Security Agent Analytics"
                st.rerun()

    elif st.session_state.current_view == "Energy Agent Analytics":
        if st.button("<- Back to Overview"):
            st.session_state.current_view = "Overview"
            st.rerun()
        st.subheader("⚡ Energy Agent Analytics Engine")
        fig = px.line(energy_data, x='Date', y='Energy Consumption (kWh)', title='Real-time Daily Energy Track')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(energy_data, use_container_width=True)

    elif st.session_state.current_view == "Maintenance Agent Analytics":
        if st.button("<- Back to Overview"):
            st.session_state.current_view = "Overview"
            st.rerun()
        st.subheader("🔧 Maintenance Agent Automation Log")
        fig = px.bar(maint_data, x='Date', y='Active Work Orders', title='Active Preventive Maintenance Orders', color='Active Work Orders')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(maint_data, use_container_width=True)

    elif st.session_state.current_view == "Occupancy Agent Analytics":
        if st.button("<- Back to Overview"):
            st.session_state.current_view = "Overview"
            st.rerun()
        st.subheader("👥 Space Occupancy Engine Tracking")
        fig = px.line(occ_data, x='Date', y='Avg Space Utilization (%)', title='Workspace Desk Utilization % Over Time')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(occ_data, use_container_width=True)

    elif st.session_state.current_view == "Security Agent Analytics":
        if st.button("<- Back to Overview"):
            st.session_state.current_view = "Overview"
            st.rerun()
        st.subheader("🛡️ Real-time Threat & Security Logs")
        fig = px.scatter(sec_data, x='Date', y='Threats Detected', size='Incidents Resolved', title='Anomalies Caught & Mitigated Matrix System')
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(sec_data, use_container_width=True)


# --- MAIN APP EXECUTION CONTROL ---
if __name__ == "__main__":
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_dashboard()
