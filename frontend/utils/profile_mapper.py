def map_profile(raw_profile_data: dict) -> dict:
    """
    Transforms the Streamlit session state profile dictionary 
    into a clean JSON payload for the FastAPI backend.
    """
    
    mapped_data = {
        "personal_info": {
            "full_name": raw_profile_data["personal"]["full_name"],
            "date_of_birth": str(raw_profile_data["personal"]["dob"]),
            "gender": raw_profile_data["personal"]["gender"],
            "phone_number": raw_profile_data["personal"]["phone"],
            "email": raw_profile_data["personal"]["email"],
            "address": {
                "city": raw_profile_data["personal"]["city"],
                "state": raw_profile_data["personal"]["state"],
                "pincode": raw_profile_data["personal"]["pincode"]
            }
        },
        "tax_info": raw_profile_data["tax"],
        "professional_info": raw_profile_data["professional"],
        "financial_info": raw_profile_data["financial"],
        "financial_goals": raw_profile_data["goals"]
    }
    
    return mapped_data