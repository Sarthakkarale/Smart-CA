import streamlit as st
import pandas as pd
from services.dashboard_service import DashboardService

# ==========================================================
# CUSTOM HTML COMPONENTS
# ==========================================================
def render_metric_card(title, amount, delta_text, is_positive=True):
    color = "#10B981" if is_positive else "#EF4444" 
    arrow = "↑" if is_positive else "↓"
    return f"""
    <div style="background-color: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); height: 100%;">
        <p style="color: #6B7280; font-size: 14px; margin: 0 0 8px 0; font-weight: 500;">{title}</p>
        <h2 style="color: #111827; font-size: 32px; margin: 0 0 12px 0; font-weight: 700;">₹{amount:,.0f}</h2>
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
    
    # --- FETCH DATA FROM FASTAPI ---
    with st.spinner("Loading financial data..."):
        summary_res = DashboardService.get_summary()
        charts_res = DashboardService.get_charts()
        ai_res = DashboardService.get_ai_suggestions()
        
    # Default fallbacks if backend is unreachable
    summary_data = summary_res.json() if summary_res and summary_res.status_code == 200 else {}
    charts_data = charts_res.json() if charts_res and charts_res.status_code == 200 else {}
    ai_data = ai_res.json() if ai_res and ai_res.status_code == 200 else []

    first_name = st.session_state.get("user", {}).get("full_name", "User").split()[0]

    # --- HEADER ---
    head_col1, head_col2 = st.columns([3, 1])
    
    with head_col1:
        st.markdown(f"<h2 style='margin-bottom: 0;'>Good Evening, {first_name} 👋</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color: #6B7280; font-size: 15px;'>Here is your financial overview.</p>", unsafe_allow_html=True)
        
    with head_col2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 20px; padding-top: 10px;">
            <span style="font-size: 20px; cursor: pointer;">🔍</span>
            <span style="font-size: 20px; cursor: pointer;">🔔<span style="color: red; font-size: 24px; position: absolute; margin-left: -8px; margin-top: -10px;">•</span></span>
            <div style="display: flex; align-items: center; gap: 10px; background: white; padding: 8px 15px; border-radius: 8px; border: 1px solid #E5E7EB;">
                <span style="font-weight: 500;">Today</span>
                <span>🔽</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- TOP METRICS ROW ---
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(render_metric_card(
            "Monthly Income", 
            summary_data.get("monthly_income", 0), 
            "Stable", True
        ), unsafe_allow_html=True)
    with m2:
        st.markdown(render_metric_card(
            "Monthly Expenses", 
            summary_data.get("monthly_expense", 0), 
            "In check", True
        ), unsafe_allow_html=True)
    with m3:
        savings = summary_data.get("monthly_savings", 0)
        st.markdown(render_metric_card(
            "Monthly Savings", 
            savings, 
            "Projected", savings >= 0
        ), unsafe_allow_html=True)
    with m4:
        st.markdown(render_health_card(
            str(summary_data.get("health_score", 0)), 
            summary_data.get("health_status", "Unknown")
        ), unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    # --- MAIN CONTENT ROW ---
    col_chart, col_ai = st.columns([1.8, 1], gap="large")

    # Dynamic Cash Flow Chart
    with col_chart:
        with st.container(border=True):
            header_left, header_right = st.columns([3, 1])
            with header_left:
                st.markdown("<h4 style='margin: 0;'>Projected Cash Flow</h4>", unsafe_allow_html=True)
            with header_right:
                st.selectbox("period", ["This Month", "Next 6 Months"], label_visibility="collapsed")
            
            st.write("")
            
            if "labels" in charts_data and "income_data" in charts_data:
                chart_df = pd.DataFrame({
                    "Income": charts_data.get("income_data", []),
                    "Expenses": charts_data.get("expense_data", []),
                    "Savings": charts_data.get("savings_data", [])
                }, index=charts_data.get("labels", []))
                
                st.line_chart(chart_df, color=["#10B981", "#EF4444", "#3B82F6"], height=350)
            else:
                st.info("Not enough chart data generated from backend yet.")

    # AI Suggestions directly from FastAPI
    with col_ai:
        with st.container(border=True):
            header_left, header_right = st.columns([3, 1])
            with header_left:
                st.markdown("<h4 style='margin: 0;'>AI Suggestions</h4>", unsafe_allow_html=True)
            with header_right:
                st.markdown("<p style='color: #4F46E5; font-weight: 600; text-align: right; cursor: pointer;'>View All</p>", unsafe_allow_html=True)
            
            st.write("")
            st.write("")
            
            if ai_data:
                for suggestion in ai_data:
                    # Map severity to colors (assuming your backend sends something like 'info', 'warning', 'critical')
                    icon = "💡"
                    bg_color = "#E0E7FF"
                    text_color = "#4F46E5"
                    
                    if suggestion.get("type") == "warning":
                        icon, bg_color, text_color = "⚠️", "#FEF3C7", "#F59E0B"
                    elif suggestion.get("type") == "critical":
                        icon, bg_color, text_color = "🚨", "#FEE2E2", "#EF4444"
                    elif suggestion.get("type") == "success":
                        icon, bg_color, text_color = "🛡️", "#D1FAE5", "#10B981"
                        
                    st.markdown(
                        render_ai_suggestion(icon, bg_color, suggestion.get("title", ""), suggestion.get("description", ""), text_color), 
                        unsafe_allow_html=True
                    )
            else:
                st.info("No AI suggestions generated yet.")
                
            st.write("")
            st.write("")