import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ==========================================================
SMART CA DESIGN SYSTEM
========================================================== */

.stApp{
    background:#F4F7FC;
}

.block-container{
    max-width:1400px;
    padding:1.5rem 2.5rem;
}

/* Hide Streamlit */

#MainMenu,
header,
footer{
    visibility:hidden;
}

/* ==========================================================
Typography
========================================================== */

h1{
    color:#1E293B;
    font-weight:700;
}

h2{
    color:#1E293B;
    font-weight:700;
}

h3{
    color:#334155;
}

p{
    color:#64748B;
    line-height:1.7;
}

/* ==========================================================
Inputs
========================================================== */

.stTextInput input{

    height:52px;

    border-radius:12px;

    border:1px solid #DCE3ED;

    background:white;

    font-size:15px;

}

.stTextInput input:focus{

    border:1px solid #6C4CF1;

    box-shadow:none;

}

/* ==========================================================
Buttons
========================================================== */

.stButton button{

    height:50px;

    border-radius:12px;

    font-size:16px;

    font-weight:600;

    color:white !important;

}
/* Primary (Login) Button */

button[kind="primary"]{

    background:#6C4CF1 !important;

    color:#FFFFFF !important;

    border:none !important;

}

button[kind="primary"] p{

    color:#FFFFFF !important;

    font-weight:600 !important;

}

button[kind="primary"]:hover{

    background:#5B3AE5 !important;

}

/* Login button */

div[data-testid="stForm"] .stButton button{

    width:100%;

}

/* Register button */

button[kind="secondary"]{

    border:2px solid #6C4CF1 !important;

    color:#6C4CF1 !important;

    background:white !important;

}

button[kind="secondary"]:hover{

    background:#F3F0FF !important;

}

/* ==========================================================
Forms
========================================================== */

.stForm{

    background:white;

    border:1px solid #E5E7EB;

    border-radius:20px;

    padding:30px;

}

/* ==========================================================
Images
========================================================== */

img{

    border-radius:14px;

}

</style>
""",
        unsafe_allow_html=True,
    )