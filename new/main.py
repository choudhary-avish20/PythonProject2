import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


st.markdown(
    """
    <h1 style="text-align: center; font-size: 4rem; font-weight: bold; color: #4A90E2;">
        Logi<span style="color: #FF6F61;">कल</span>
    </h1>
    <h3 style="text-align: center; font-size: 1.3rem; color: #6C757D;">
        Rapid Compliance Checker
    </h3>
    """,
    unsafe_allow_html=True
)

# Horizontal navigation menu with only Home, Logs, and FAQs
page = option_menu(
    menu_title=None,  # Hide title
    options=["Home", "Logs", "FAQs"],
    icons=["house", "file-earmark-text", "question-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Display content based on selection
if page == "Home":

    st.markdown(
        """  
        ### **:blue[Streamlining Compliance, Ensuring Smooth Shipments]**  
        In the fast-paced world of international shipping, small exporters often face compliance hurdles that lead to delays, penalties, or even shipment rejections.  
        **Logiकल** is a smart compliance checker designed to **quickly verify the regulatory requirements** of each parcel before it reaches the courier.  

        #### **:red[Why Logiकल?]**  
        - ✅ **Real-Time Compliance Checks** – Instantly flag missing fields, restricted items, or destination conflicts.  
        - 📦 **Easy Data Input** – Manually enter shipment details or upload bulk data via CSV.  
        - 🔍 **Transparent Rule-Based Validation** – Clearly see why a parcel is flagged and how to resolve issues.  
        - 📊 **Interactive Dashboard** – Get a quick overview of shipment status: **Compliant ✅** or **Flagged ⚠️**.  
        - 📝 **Auto-Generated Reports** – Download a **Shipping Form** or **Compliance Report** for record-keeping.  

        #### **:red[How It Works]**  
        1️⃣ **Data Ingestion** – Enter shipment details manually or upload them in a structured format.  
        2️⃣ **Rule-Based Validation** – Our system applies compliance rules, checking for missing fields, restricted items, or value limits.  
        3️⃣ **Instant Feedback** – Flagged shipments display a clear explanation of issues and corrective steps.  
        4️⃣ **Compliance Reports** – Generate and export compliant shipment reports in PDF or HTML format.  

        #### **:red[Beyond the Basics]**  
        💡 **Custom Rules & Updates** – Modify rules dynamically via an admin panel.  
        💰 **Tariff & Tax Calculation** – Factor in exchange rates and duty estimates.  
        🌍 **AI-Powered Predictions** – Use intelligent insights to anticipate compliance risks.  

        #### **:red[The Logiकल Advantage]**  
        - 🚀 **Reduces shipment delays**  
        - 🔄 **Minimizes compliance risks**  
        - ⏳ **Saves time with automated validation**  
        - 📈 **Enhances business efficiency**  
        \n
        ### **Get started with :blue[Logi]:red[कल] – ensuring compliance, one shipment at a time!** 🚛📦  
        """,
        unsafe_allow_html=True
    )

    import streamlit as st

    # Custom CSS to increase button size
    st.markdown(
        """ 
        <style>
        div.stButton > button {
            font-size: 20px !important;
            padding: 15px 30px !important;
            border-radius: 10px !important;
            width: 100% !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create empty columns with adjusted spacing
    col1, col2, col3 = st.columns([1.25, 3, 1])  # Increased left column width by 25%

    # Place the button in the middle column
    with col2:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        if st.button("🚀 Get Started"):
            st.switch_page("pages/home2.py")
        st.markdown("</div>", unsafe_allow_html=True)


elif page == "Logs":
    #st.set_page_config(page_title="📦 Shipment Log", page_icon="📊", layout="wide")

    # Custom Styling
    st.markdown("""
        <style>
        .main {
            background-color: #1E1E2E;
            color: white;
        }
        h1, h2 {
            text-align: center;
        }
        .dataframe {
            background-color: #2A2A3C;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Title
    st.title("📦 Shipment Compliance Log")

    # Sample Data
    data = [
        ["China", "123 Tech Park, Shenzhen", "United States", "Smartphone", "8517.12", 1.2, 700, "Passed"],
        ["Germany", "45 Logistics St, Berlin", "India", "Laptop", "8471.30", 2.5, 1200, "Passed"],
        ["India", "678 Business Ave, Mumbai", "United Kingdom", "Headphones", "8518.30", 0.5, 150, "Failed"],
        ["Japan", "89 Shibuya District, Tokyo", "Canada", "Gaming Console", "9504.50", 3.8, 500, "Passed"],
        ["Brazil", "202 Trade Hub, São Paulo", "France", "Television", "8528.72", 10.5, 900, "Failed"],
        ["South Korea", "10 Digital Way, Seoul", "Australia", "Smartwatch", "8517.62", 0.3, 250, "Passed"],
        ["United States", "789 Silicon Blvd, California", "Germany", "External Hard Drive", "8471.70", 0.8, 120,
         "Passed"],
        ["Russia", "67 Export Lane, Moscow", "Italy", "Refrigerator", "8418.10", 40.0, 1300, "Failed"],
        ["United Kingdom", "55 Import St, London", "Spain", "Electric Scooter", "8711.60", 12.5, 600, "Passed"],
        ["Mexico", "321 Avenida Comercial, Mexico City", "Netherlands", "Car", "8703.21", 1500.0, 25000, "Passed"]
    ]

    columns = [
        "Country of Origin", "Importer Address", "Country of Destination",
        "Product Type", "HS Code", "Weight (kg)", "Declared Value ($)", "Compliance Status"
    ]

    # Store in Session State
    if "shipment_log" not in st.session_state:
        st.session_state["shipment_log"] = pd.DataFrame(data, columns=columns)

    # Display Log Table
    st.subheader("📋 Shipment Entries Log")
    st.dataframe(st.session_state["shipment_log"], use_container_width=True)

    # Visualization: Compliance Status Breakdown
    st.subheader("📊 Compliance Status Overview")

    if not st.session_state["shipment_log"].empty:
        fig = px.pie(st.session_state["shipment_log"], names="Compliance Status", title="Shipment Compliance Breakdown",
                     color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No shipment logs available yet.")

    # Download Log as CSV
    st.subheader("⬇️ Export Shipment Log")
    csv = st.session_state["shipment_log"].to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Download Log", data=csv, file_name="shipment_log.csv", mime="text/csv")

    # Back to Home Button
    st.button("⬅️ Back to Home", on_click=lambda: st.switch_page("pages/home.py"))



elif page == "FAQs":
    st.title("❓ Frequently Asked Questions")
    faqs = {
        "What is shipment compliance?": "Shipment compliance ensures parcels meet legal and regulatory requirements before international shipping.",
        "What happens if my parcel is flagged?": "If flagged, the system will explain why and suggest corrective actions.",
        "Can I add new compliance rules?": "Currently, rules are predefined, but future versions may allow admin rule customization.",
        "How does the chatbot help?": "The chatbot provides instant answers regarding compliance rules and flagged shipments."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)

