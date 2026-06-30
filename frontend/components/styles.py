import streamlit as st


def load_styles():
    st.markdown("""
<style>

/* ===========================================================
   GOOGLE FONT
=========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}


/* ===========================================================
   COLORS
=========================================================== */

:root{

    --primary:#6D5EF8;
    --primary-dark:#5B4CE6;

    --sidebar:#0F172A;

    --background:#F8FAFC;

    --card:#FFFFFF;

    --text:#1E293B;

    --subtitle:#64748B;

    --success:#22C55E;

    --warning:#F59E0B;

    --danger:#EF4444;

}


/* ===========================================================
   HIDE STREAMLIT DEFAULT UI
=========================================================== */

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

[data-testid="collapsedControl"]{
display:none;
}


/* ===========================================================
   MAIN APP
=========================================================== */

.stApp{

background:var(--background);

}


/* ===========================================================
   SIDEBAR
=========================================================== */

section[data-testid="stSidebar"]{

background:var(--sidebar);

width:260px !important;

border-right:none;

}

section[data-testid="stSidebar"] *{

color:white;

}


/* ===========================================================
   LOGO
=========================================================== */

.logo{

font-size:28px;

font-weight:700;

margin-top:10px;

margin-bottom:2px;

}

.logo-sub{

color:#CBD5E1;

font-size:13px;

margin-bottom:30px;

}


/* ===========================================================
   PAGE TITLE
=========================================================== */

.page-title{

font-size:34px;

font-weight:700;

color:var(--text);

margin-bottom:5px;

}

.page-subtitle{

font-size:16px;

color:var(--subtitle);

margin-bottom:30px;

}


/* ===========================================================
   CARD
=========================================================== */

.card{

background:white;

padding:24px;

border-radius:18px;

box-shadow:

0 10px 25px rgba(15,23,42,.08);

margin-bottom:25px;

}


/* ===========================================================
   INPUTS
=========================================================== */

.stTextInput input{

border-radius:12px;

padding:12px;

border:1px solid #CBD5E1;

}

.stNumberInput input{

border-radius:12px;

padding:12px;

border:1px solid #CBD5E1;

}

div[data-baseweb="select"]{

border-radius:12px;

}


/* ===========================================================
   BUTTON
=========================================================== */

.stButton>button{

background:var(--primary);

color:white;

border:none;

border-radius:12px;

height:48px;

font-size:16px;

font-weight:600;

width:100%;

transition:.3s;

}

.stButton>button:hover{

background:var(--primary-dark);

}


/* ===========================================================
   METRIC CARD
=========================================================== */

.metric{

background:white;

padding:20px;

border-radius:18px;

box-shadow:

0 8px 20px rgba(15,23,42,.08);

text-align:center;

}

.metric-title{

font-size:15px;

color:var(--subtitle);

}

.metric-value{

font-size:30px;

font-weight:700;

color:var(--text);

margin-top:10px;

}


/* ===========================================================
   PROGRESS BAR
=========================================================== */

.progress{

width:100%;

height:12px;

background:#E2E8F0;

border-radius:50px;

overflow:hidden;

margin:20px 0;

}

.progress-fill{

height:12px;

background:linear-gradient(
90deg,
#6D5EF8,
#8B5CF6
);

}


/* ===========================================================
   SUCCESS
=========================================================== */

.success-card{

background:#ECFDF5;

border-left:5px solid #22C55E;

padding:20px;

border-radius:12px;

}


/* ===========================================================
   WARNING
=========================================================== */

.warning-card{

background:#FFF7ED;

border-left:5px solid #F59E0B;

padding:20px;

border-radius:12px;

}


/* ===========================================================
   ERROR
=========================================================== */

.error-card{

background:#FEF2F2;

border-left:5px solid #EF4444;

padding:20px;

border-radius:12px;

}


/* ===========================================================
   TABLE
=========================================================== */

table{

border-collapse:collapse;

width:100%;

}

th{

background:#F8FAFC;

padding:12px;

}

td{

padding:12px;

}


/* ===========================================================
   SCROLLBAR
=========================================================== */

::-webkit-scrollbar{

width:8px;

}

::-webkit-scrollbar-thumb{

background:#CBD5E1;

border-radius:10px;

}


/* ===========================================================
   ANIMATION
=========================================================== */

.card{

animation:fadeIn .4s ease;

}

@keyframes fadeIn{

from{

opacity:0;

transform:translateY(15px);

}

to{

opacity:1;

transform:translateY(0);

}

}

</style>

""", unsafe_allow_html=True)