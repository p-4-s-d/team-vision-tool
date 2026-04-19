import streamlit as st

# App Configuration
st.set_page_config(page_title="Team Giving Vision Evaluator", page_icon="🎓")

# Branding based on EBS 222
st.title("🎓 EBS 222: Visionary Evaluator")
st.subheader("Week 4: Problem Definition & Theory of Change")

st.markdown("""
Upload a student group's **'Team Giving Vision'** document. 
The tool will analyze the text for alignment with course materials and provide TA feedback.
""")

# File Upload Section
uploaded_file = st.file_uploader("Upload Student Submission (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    # In a live app, you would use a library like PyPDF2 to extract text here.
    # For this template, we simulate the analysis based on your TA requirements.
    
    st.divider()
    st.header("📋 TA Evaluation Results")
    
    # Placeholder for student group name (could be extracted from file)
    group_name = "Sample Student Group"
    st.info(f"Analyzing submission for: **{group_name}**")

    # --- FEEDBACK GENERATION LOGIC ---
    col1, col2 = st.columns(2)

    with col1:
        st.success("### ✅ Positive Feedback")
        st.write("- **Strategic Alignment:** The vision clearly moves beyond 'charitable impulse' toward an 'impact-driven practice'[cite: 819].")
        st.write("- **Values-Based:** Strong evidence of using the 'Values Exercise' or 'Issue Cards' to define the group's core mission[cite: 312, 405].")
        st.write("- **Problem Framing:** The group successfully narrowed down a broad issue into a concise, solvable problem[cite: 544].")

    with col2:
        st.warning("### 💡 Room for Development")
        st.write("- **Causal Assumptions:** The pathway to change is slightly 'invisible.' Consider asking the group to explicitly test their hypotheses[cite: 625].")
        st.write("- **Stakeholder Voice:** The vision remains donor-centric. Suggest they incorporate 'trust-based' or 'participatory' elements[cite: 813].")
        st.write("- **Approach Diversity:** Is there a mix of direct service and systems change? Encourage them to explore policy or research-based solutions.")

    # --- CREATIVE RESOURCES SECTION ---
    st.divider()
    st.header("📚 Recommended Resources for this Group")
    st.write("Based on their submission, suggest these specific readings:")
    
    resources = {
        "Theory of Change": "Paul Brest, 'The Power of Theories of Change' (SSIR, 2010)[cite: 570].",
        "The RCT Debate": "Marwell & Mosley, 'The Nonprofit Sector Has an RCT Problem' (SSIR, 2025).",
        "Effective Givers": "Phil Buchanan, 'Giving Done Right'[cite: 823].",
        "Problem Deep-Dive": "PACS Guide Chapter 5: 'Understanding Problems and Approaches to Solutions'[cite: 531]."
    }
    
    for title, link in resources.items():
        st.markdown(f"* **{title}**: {link}")

    # --- TA ACTION ITEM ---
    st.button("Export Feedback to PDF for Students")
