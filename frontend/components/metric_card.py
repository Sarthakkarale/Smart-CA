import streamlit as st


def metric_card(title, value, icon):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:25px;
            border-radius:18px;
            box-shadow:0 8px 20px rgba(0,0,0,.08);
            text-align:center;
            height:150px;
        ">

        <div style="
            font-size:30px;
        ">
            {icon}
        </div>

        <div style="
            color:#64748B;
            font-size:16px;
            margin-top:10px;
        ">
            {title}
        </div>

        <div style="
            font-size:28px;
            font-weight:700;
            color:#1E293B;
            margin-top:10px;
        ">
            {value}
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )