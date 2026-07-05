import streamlit as st
import datetime
from services.profile_service import ProfileService
from utils.profile_mapper import map_profile

# ==========================================================
# MAIN PAGE FUNCTION
# ==========================================================
def profile_page():
    
    # ----------------------------------------------------------
    # SESSION STATE
    # ----------------------------------------------------------
    if "profile_step" not in st.session_state:
        st.session_state.profile_step = 1

    if "profile" not in st.session_state:
        # Fetch dynamic user data from login
        user = st.session_state.get("user", {})
        
        st.session_state.profile = {
            "personal": {
                "full_name": user.get("full_name", ""),
                "dob": datetime.date(2002, 7, 4),
                "gender": "Male",
                "phone": "+91 98765 43210",
                "email": user.get("email", ""),
                "city": "Pune",
                "state": "Maharashtra",
                "pincode": "411001"
            },
            "tax": {
                "pan": "", "aadhaar": "", "tax_regime": "", "resident_status": "",
                "gst_registered": False, "gst_number": "", "itr_history": "",
            },
            "professional": {
                "employment_type": "", "occupation": "", "company_name": "",
                "annual_income": 0, "experience": 0, "business_type": "",
            },
            "financial": {
                "bank_name": "", "monthly_expense": 0, "existing_investments": 0,
                "loan_amount": 0, "insurance_cover": 0, "emergency_fund": 0,
            },
            "goals": {
                "retirement": False, "buy_house": False, "buy_car": False,
                "child_education": False, "wealth_creation": False, "travel": False,
                "other_goal": "", "target_year": 2035,
            }
        }

    profile = st.session_state.profile
    current = st.session_state.profile_step

    # =====================================================
    # SUCCESS SCREEN (STEP 6)
    # =====================================================
    if current == 6:
        st.balloons()
        st.write("")
        st.write("")
        st.write("")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.container(border=True):
                st.markdown(
                    """
                    <div style="text-align: center; padding: 30px 10px;">
                        <span style="font-size: 80px; color: #10B981;">✅</span>
                        <h2 style="color: #111827; margin-top: 20px;">Profile Complete!</h2>
                        <p style="color: #6B7280; font-size: 16px;">
                            Your financial profile has been securely saved. Smart CA is now ready to generate your personalized AI insights.
                        </p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                st.write("")
                
                def switch_to_dashboard():
                    st.session_state.main_menu = "Dashboard"

                st.button("🚀 Go to Dashboard", type="primary", use_container_width=True, on_click=switch_to_dashboard)
                    
        return 

    # ----------------------------------------------------------
    # PAGE HEADER 
    # ----------------------------------------------------------
    left_header, right_header = st.columns([5, 1])
    with left_header:
        st.title("Complete Your Profile")
        st.caption("Help us know you better to provide personalized financial insights.")
    with right_header:
        display_name = st.session_state.get("user", {}).get("full_name", "User")
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; justify-content: flex-end; gap: 10px;">
                <div style="font-size: 20px; color: gray;">❓</div>
                <div style="text-align: right; line-height: 1.2;">
                    <b>{display_name}</b><br>
                    <span style="color:#4B0082; font-size: 14px;">Individual</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.divider()

    # ----------------------------------------------------------
    # STEPPER
    # ----------------------------------------------------------
    step_names = [
        "Personal Information", "Tax Information", "Professional Details",
        "Financial Details", "Financial Goals",
    ]
    cols = st.columns(5)
    for i, col in enumerate(cols, start=1):
        with col:
            if i < current: icon, color = "🟣", "#4B0082"
            elif i == current: icon, color = "🟣", "#4B0082"
            else: icon, color = "⚪", "gray"
            st.markdown(f"<div style='text-align:center;font-size:24px'>{icon}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align:center;font-weight:600; font-size: 14px; color:{color}'>{step_names[i-1]}</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ----------------------------------------------------------
    # MAIN CONTENT
    # ----------------------------------------------------------
    left, right = st.columns([2.5, 1], gap="large")

    with left:
        with st.container(border=True):
            
            # STEP 1
            if current == 1:
                st.subheader("👤 Personal Information")
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["personal"]["full_name"] = st.text_input("Full Name *", value=profile["personal"]["full_name"])
                with col2: profile["personal"]["dob"] = st.date_input("Date of Birth *", value=profile["personal"]["dob"])
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["personal"]["gender"] = st.selectbox("Gender *", ["", "Male", "Female", "Other"], index=1 if profile["personal"]["gender"] == "Male" else 0)
                with col2: profile["personal"]["phone"] = st.text_input("Mobile Number *", value=profile["personal"]["phone"])
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["personal"]["email"] = st.text_input("Email *", value=profile["personal"]["email"])
                with col2: profile["personal"]["city"] = st.text_input("City", value=profile["personal"]["city"])
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["personal"]["state"] = st.selectbox("State", ["", "Maharashtra", "Delhi", "Karnataka", "Tamil Nadu"], index=1 if profile["personal"]["state"] == "Maharashtra" else 0)
                with col2: profile["personal"]["pincode"] = st.text_input("PIN Code", value=profile["personal"]["pincode"])

            # STEP 2
            elif current == 2:
                st.subheader("🧾 Tax Information")
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["tax"]["pan"] = st.text_input("PAN Number *", value=profile["tax"]["pan"], placeholder="ABCDE1234F")
                with col2: profile["tax"]["aadhaar"] = st.text_input("Aadhaar Number *", value=profile["tax"]["aadhaar"])
                st.write("")
                col1, col2 = st.columns(2)
                with col1: profile["tax"]["tax_regime"] = st.selectbox("Tax Regime *", ["", "Old Regime", "New Regime"], index=0)
                with col2: profile["tax"]["resident_status"] = st.selectbox("Resident Status *", ["", "Resident", "NRI", "RNOR"], index=0)
                st.write("")
                profile["tax"]["gst_registered"] = st.checkbox("GST Registered", value=profile["tax"]["gst_registered"])
                if profile["tax"]["gst_registered"]:
                    profile["tax"]["gst_number"] = st.text_input("GST Number *", value=profile["tax"]["gst_number"])
                st.write("")
                profile["tax"]["itr_history"] = st.selectbox("Last ITR Filed", ["", "Never Filed", "2023-24", "2024-25", "2025-26"], index=0)

            # STEP 3
            elif current == 3:
                st.subheader("💼 Professional Information")
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["professional"]["employment_type"] = st.selectbox("Employment Type *", ["", "Salaried", "Self Employed", "Business", "Freelancer", "Student", "Retired"])
                with c2: profile["professional"]["occupation"] = st.text_input("Occupation *", value=profile["professional"]["occupation"])
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["professional"]["company_name"] = st.text_input("Company / Business", value=profile["professional"]["company_name"])
                with c2: profile["professional"]["annual_income"] = st.number_input("Annual Income (₹) *", min_value=0, step=50000, value=profile["professional"]["annual_income"])
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["professional"]["experience"] = st.number_input("Years of Experience", min_value=0, max_value=50, value=profile["professional"]["experience"])
                with c2:
                    if profile["professional"]["employment_type"] in ["Business", "Self Employed", "Freelancer"]:
                        profile["professional"]["business_type"] = st.text_input("Business Type *", value=profile["professional"]["business_type"])

            # STEP 4
            elif current == 4:
                st.subheader("💰 Financial Information")
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["financial"]["bank_name"] = st.text_input("Primary Bank *", value=profile["financial"]["bank_name"])
                with c2: profile["financial"]["monthly_expense"] = st.number_input("Monthly Expenses (₹) *", min_value=0, step=1000, value=profile["financial"]["monthly_expense"])
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["financial"]["existing_investments"] = st.number_input("Existing Investments (₹)", min_value=0, step=10000, value=profile["financial"]["existing_investments"])
                with c2: profile["financial"]["loan_amount"] = st.number_input("Outstanding Loans (₹)", min_value=0, step=10000, value=profile["financial"]["loan_amount"])
                st.write("")
                c1, c2 = st.columns(2)
                with c1: profile["financial"]["insurance_cover"] = st.number_input("Insurance Cover (₹)", min_value=0, step=50000, value=profile["financial"]["insurance_cover"])
                with c2: profile["financial"]["emergency_fund"] = st.number_input("Emergency Fund (₹)", min_value=0, step=10000, value=profile["financial"]["emergency_fund"])

            # STEP 5
            elif current == 5:
                st.subheader("🎯 Financial Goals")
                st.write("")
                st.markdown("### Select Your Goals")
                profile["goals"]["retirement"] = st.checkbox("Retirement Planning", value=profile["goals"]["retirement"])
                profile["goals"]["buy_house"] = st.checkbox("Buy a House", value=profile["goals"]["buy_house"])
                profile["goals"]["buy_car"] = st.checkbox("Buy a Car", value=profile["goals"]["buy_car"])
                profile["goals"]["child_education"] = st.checkbox("Child Education", value=profile["goals"]["child_education"])
                profile["goals"]["wealth_creation"] = st.checkbox("Wealth Creation", value=profile["goals"]["wealth_creation"])
                profile["goals"]["travel"] = st.checkbox("Travel / Vacation", value=profile["goals"]["travel"])
                st.write("")
                profile["goals"]["other_goal"] = st.text_input("Other Financial Goal", value=profile["goals"]["other_goal"])
                st.write("")
                profile["goals"]["target_year"] = st.slider("Target Year", min_value=2026, max_value=2055, value=profile["goals"]["target_year"])

            # NAVIGATION AND VALIDATION
            st.write("")
            error_placeholder = st.empty()
            st.write("")
            
            btn_c1, empty_c, btn_c2 = st.columns([1, 4, 1])
            
            with btn_c1:
                if st.button("← Previous", disabled=(current == 1), use_container_width=True):
                    st.session_state.profile_step -= 1
                    st.rerun()
                    
            with btn_c2:
                button_text = "Finish ✅" if current == 5 else "Next →"
                if st.button(button_text, type="primary", use_container_width=True):
                    
                    # --- Validation Logic ---
                    is_valid = True
                    
                    if current == 1:
                        p = profile["personal"]
                        if not p["full_name"] or not p["gender"] or not p["phone"] or not p["email"]:
                            is_valid = False
                    
                    elif current == 2:
                        t = profile["tax"]
                        if not t["pan"] or not t["aadhaar"] or not t["tax_regime"] or not t["resident_status"]:
                            is_valid = False
                        if t["gst_registered"] and not t["gst_number"]:
                            is_valid = False
                            
                    elif current == 3:
                        pr = profile["professional"]
                        if not pr["employment_type"] or not pr["occupation"] or pr["annual_income"] <= 0:
                            is_valid = False
                        if pr["employment_type"] in ["Business", "Self Employed", "Freelancer"] and not pr["business_type"]:
                            is_valid = False
                            
                    elif current == 4:
                        f = profile["financial"]
                        if not f["bank_name"] or f["monthly_expense"] <= 0:
                            is_valid = False
                    
                    # --- Navigation & Integration ---
                    if is_valid:
                        # -----------------------------
                        # Next Step
                        # -----------------------------
                        if current < 5:
                            st.session_state.profile_step += 1
                            st.rerun()

                        # -----------------------------
                        # Save Profile
                        # -----------------------------
                        payload = map_profile(
                            st.session_state.profile
                        )

                        with st.spinner("Saving profile..."):
                            response = ProfileService.create_profile(
                                payload
                            )

                        if response is None:
                            st.error("Unable to connect to backend.")

                        elif response.status_code in [200, 201]:
                            st.session_state.profile_step = 6
                            st.success("Profile Saved Successfully")
                            st.rerun()

                        else:
                            try:
                                error = response.json()
                                st.error(error["detail"])
                            except Exception:
                                st.error(response.text)
                    else:
                        error_placeholder.error("⚠️ Please fill in all required fields marked with *")

    # ----------------------------------------------------------
    # RIGHT CARD (Info Panel)
    # ----------------------------------------------------------
    with right:
        with st.container(border=True):
            if current == 1:
                st.markdown('<div style="text-align: center; padding: 15px; background-color: #F8F9FA; border-radius: 10px; margin-bottom: 20px;"><span style="font-size: 50px;">📋</span></div>', unsafe_allow_html=True)
                st.subheader("💡 Why this matters")
                st.write("Complete your profile to unlock:\n\n✅ Personalized Tax Planning\n\n✅ AI Financial Insights\n\n✅ Better Investment Suggestions\n\n✅ Faster OCR Processing")
            elif current == 2:
                st.markdown('<div style="text-align: center; padding: 15px; background-color: #F8F9FA; border-radius: 10px; margin-bottom: 20px;"><span style="font-size: 50px;">🧾</span></div>', unsafe_allow_html=True)
                st.subheader("💡 Tax Profile")
                st.write("Providing tax information helps Smart CA:\n\n✅ Suggest the correct ITR\n\n✅ Estimate tax liability\n\n✅ Recommend deductions\n\n✅ Generate AI tax insights")
            elif current == 3:
                st.markdown('<div style="text-align: center; padding: 15px; background-color: #F8F9FA; border-radius: 10px; margin-bottom: 20px;"><span style="font-size: 50px;">💼</span></div>', unsafe_allow_html=True)
                st.subheader("💡 Professional Profile")
                st.write("Your professional information helps Smart CA:\n\n✅ Calculate income tax\n\n✅ Recommend tax-saving investments\n\n✅ Generate AI financial advice")
            elif current == 4:
                st.markdown('<div style="text-align: center; padding: 15px; background-color: #F8F9FA; border-radius: 10px; margin-bottom: 20px;"><span style="font-size: 50px;">💰</span></div>', unsafe_allow_html=True)
                st.subheader("💡 Financial Health")
                st.write("Providing financial information helps Smart CA:\n\n✅ Build your net worth\n\n✅ Recommend investments\n\n✅ Track liabilities\n\n✅ Improve AI recommendations")
            elif current == 5:
                st.markdown('<div style="text-align: center; padding: 15px; background-color: #F8F9FA; border-radius: 10px; margin-bottom: 20px;"><span style="font-size: 50px;">🎯</span></div>', unsafe_allow_html=True)
                st.subheader("💡 Future Planning")
                st.write("Your financial goals help Smart CA:\n\n✅ Build personalized investment plans\n\n✅ Calculate retirement corpus\n\n✅ Estimate goal timelines")
                st.success("Almost done! Click Finish to complete your profile.")