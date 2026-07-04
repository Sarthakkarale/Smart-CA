import streamlit as st
import pandas as pd
import numpy as np

# ==========================================================
# CUSTOM HTML COMPONENTS
# ==========================================================
def render_metric_card(title, amount, delta_text, is_positive=True):
    color = "#10B981" if is_positive else "#EF4444" 
    arrow = "↑" if is_positive else "↓"
    return f"""
    <div style="background-color: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); height: 100%;">
        <p style="color: #6B7280; font-size: 14px; margin: 0 0 8px 0; font-weight: 500;">{title}</p>
        <h2 style="color: #111827; font-size: 32px; margin: 0 0 12px 0; font-weight: 700;">{amount}</h2>
        <p style="color: {color}; font-size: 13px; margin: 0; font-weight: 600;">
            {arrow} {delta_text}
        </p>
    </div>
    """

def render_health_card(score, status):
    return f"""
    <div style="background-color: #171B29; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <p style="color: white; font-size: 15px; margin: 0 0 15px 0; font-weight: 500; width: 100%; text-align: left;">Financial Health</p>
        <div style="position: relative; width: 100px; height: 100px; border-radius: 50%; border: 6px solid #23293D; border-right-color: #10B981; border-top-color: #10B981; display: flex; align-items: center; justify-content: center;">
            <h2 style="color: white; font-size: 36px; margin: 0; font-weight: 700;">{score}</h2>
        </div>
        <p style="color: #10B981; font-size: 15px; margin: 15px 0 0 0; font-weight: 500;">{status}</p>
    </div>
    """

def render_ai_suggestion(icon, icon_bg, title, subtitle, icon_color):
    return f"""
    <div style="display: flex; align-items: flex-start; margin-bottom: 24px;">
        <div style="background-color: {icon_bg}; padding: 12px; border-radius: 50%; margin-right: 16px; display: flex; align-items: center; justify-content: center; width: 45px; height: 45px;">
            <span style="font-size: 20px; color: {icon_color};">{icon}</span>
        </div>
        <div>
            <p style="color: #111827; font-size: 15px; font-weight: 600; margin: 0 0 4px 0;">{title}</p>
            <p style="color: #6B7280; font-size: 13px; margin: 0;">{subtitle}</p>
        </div>
    </div>
    """

# ==========================================================
# MAIN DASHBOARD PAGE
# ==========================================================
def dashboard_page():
    
    # --- HEADER ---
    head_col1, head_col2 = st.columns([3, 1])
    
    with head_col1:
        st.markdown("<h2 style='margin-bottom: 0;'>Good Evening, Sarthak 👋</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; font-size: 15px;'>Here is your financial overview for today.</p>", unsafe_allow_html=True)
        
    with head_col2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 20px; padding-top: 10px;">
            <span style="font-size: 20px; cursor: pointer;">🔍</span>
            <span style="font-size: 20px; cursor: pointer;">🔔<span style="color: red; font-size: 24px; position: absolute; margin-left: -8px; margin-top: -10px;">•</span></span>
            <div style="display: flex; align-items: center; gap: 10px; background: white; padding: 8px 15px; border-radius: 8px; border: 1px solid #E5E7EB;">
                <span style="font-weight: 500;">30 June 2026</span>
                <span>🔽</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- TOP METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(render_metric_card("Monthly Income", "₹75,000", "10% vs last month", True), unsafe_allow_html=True)
    with m2:
        st.markdown(render_metric_card("Monthly Expenses", "₹28,000", "5% vs last month", False), unsafe_allow_html=True)
    with m3:
        st.markdown(render_metric_card("Monthly Savings", "₹47,000", "15% vs last month", True), unsafe_allow_html=True)
    with m4:
        st.markdown(render_health_card("82", "Good"), unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # --- MAIN CONTENT ROW ---
    col_chart, col_ai = st.columns([1.8, 1], gap="large")

    # Cash Flow Chart
    with col_chart:
        with st.container(border=True):
            header_left, header_right = st.columns([3, 1])
            with header_left:
                st.markdown("<h4 style='margin: 0;'>Cash Flow Overview</h4>", unsafe_allow_html=True)
            with header_right:
                st.selectbox("period", ["This Month", "Last Month", "This Year"], label_visibility="collapsed")
            
            st.write("")
            
            dates = pd.date_range(start="2026-06-01", end="2026-06-30")
            income_base = np.linspace(40000, 95000, 30) + np.random.normal(0, 3000, 30)
            expense_base = np.linspace(20000, 65000, 30) + np.random.normal(0, 2000, 30)
            savings_base = np.linspace(5000, 35000, 30) + np.random.normal(0, 1500, 30)
            
            chart_data = pd.DataFrame({
                "Income": income_base,
                "Expenses": expense_base,
                "Savings": savings_base
            }, index=dates)
            
            st.line_chart(chart_data, color=["#10B981", "#EF4444", "#3B82F6"], height=350)

    # AI Suggestions
    with col_ai:
        with st.container(border=True):
            header_left, header_right = st.columns([3, 1])
            with header_left:
                st.markdown("<h4 style='margin: 0;'>AI Suggestions</h4>", unsafe_allow_html=True)
            with header_right:
                st.markdown("<p style='color: #4F46E5; font-weight: 600; text-align: right; cursor: pointer;'>View All</p>", unsafe_allow_html=True)
            
            st.write("")
            st.write("")
            
            st.markdown(render_ai_suggestion("💰", "#D1FAE5", "Increase SIP by ₹5,000", "You can build wealth faster.", "#10B981"), unsafe_allow_html=True)
            st.markdown(render_ai_suggestion("🛡️", "#D1FAE5", "Save up to ₹12,000 tax", "Invest in ELSS before 31 Mar.", "#10B981"), unsafe_allow_html=True)
            st.markdown(render_ai_suggestion("⚠️", "#FEE2E2", "Emergency fund is low", "Save at least 6 months expenses.", "#EF4444"), unsafe_allow_html=True)
            
            st.write("")
            st.write("")