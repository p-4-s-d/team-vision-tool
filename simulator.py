import streamlit as st
import pandas as pd

# App Configuration
st.set_page_config(page_title="Stakeholder Simulator", page_icon="⚖️")

st.title("⚖️ Philanthropy Stakeholder Simulator")
st.subheader("EBS 222 / POLI SCI 236 Evaluator Tool")

st.markdown("""
As a TA, upload a student group's **Theory of Change** or proposed **Impact Metric**. 
The tool will generate critical questions from different philanthropic perspectives.
""")

# Input Section
impact_metric = st.text_input("Enter Student's Proposed Impact Metric (e.g., 'Number of meals served'):")
uploaded_file = st.file_uploader("Or upload student's Theory of Change (PDF/TXT)", type=["pdf", "txt"])

if impact_metric or uploaded_file:
    st.divider()
    st.header("🔍 Stakeholder Perspectives & 'Tough Questions'")
    
    # Logic derived from Course Syllabus & PACS Guide
    perspectives = {
        "Effective Altruism": {
            "focus": "Cost-effectiveness and 'highest and best use' of dollars.",
            "question": f"How does '{impact_metric}' compare to other global interventions in terms of cost-per-outcome? Is this the most 'effective' use of $50k compared to a malaria net intervention?",
            "resource": "MacAskill, 'Doing Good Better'"
        },
        "Trust-Based Philanthropy": {
            "focus": "Reducing burden and shifting power to the grantee.",
            "question": f"Is tracking '{impact_metric}' placing an undue reporting burden on the nonprofit staff? How does this metric serve the organization's own internal growth versus just satisfying the donor's curiosity?",
            "resource": "PACS Guide Chapter 13"
        },
        "Participatory Philanthropy": {
            "focus": "Beneficiary involvement in decision-making.",
            "question": f"Did the community members actually identify '{impact_metric}' as the most important indicator of success, or was this determined by your team from a distance?",
            "resource": "Gibson, 'Deciding Together'"
        },
        "Justice Orientation": {
            "focus": "Addressing root causes and systemic inequality.",
            "question": f"Does focusing on '{impact_metric}' address the systemic reasons why the problem exists, or is it a 'charitable impulse' that treats a symptom while leaving the status quo intact?",
            "resource": "Darren Walker, 'Toward a New Gospel of Wealth'"
        }
    }

    for school, data in perspectives.items():
        with st.expander(f"🏫 Perspective: {school}"):
            st.write(f"**Primary Focus:** {data['focus']}")
            st.error(f"**Tough Question:** {data['question']}")
            st.caption(f"📚 Related Reading: {data['resource']}")

    # Creative Resource Suggester
    st.divider()
    st.subheader("🎨 Creative Resource Suggestions")
    st.write("To help this group develop further, suggest they consider:")
    st.info("- **The Contrarian View:** Suggest the Marwell & Mosley piece on why RCTs might be problematic for this specific metric.")
    st.info("- **The PRD Connection:** Map their issue area to the Philanthropist Resource Directory (PRD) to find 'competitive' organizations.")

else:
    st.info("Please enter a metric or upload a file to begin the simulation.")
