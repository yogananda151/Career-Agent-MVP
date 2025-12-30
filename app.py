import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

# --- CONFIGURATION ---
# PASTE YOUR API KEY HERE
GOOGLE_API_KEY = "AIzaSyC-cli2_GtvuepVAqKTzY8FnvNJ1rmm2XA"

genai.configure(api_key=GOOGLE_API_KEY)

# --- PAGE SETUP ---
st.set_page_config(page_title="CareerFlow.ai", layout="wide")
st.title("🚀 CareerFlow.ai: The Agentic Career Companion")
st.markdown("""
*An Autonomous System that Plans, Acts, and Learns with you.*
""")

# --- SMART MODEL SELECTOR ---
def get_model():
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name: return genai.GenerativeModel(m.name)
        return genai.GenerativeModel('gemini-pro')
    except:
        return genai.GenerativeModel('gemini-pro')

# --- AGENT FUNCTIONS ---
def analyze_market_trends(role):
    model = get_model()
    prompt = f"""
    Act as a 'Market Scout Agent'. 
    Analyze the CURRENT job market trends for: {role}.
    Output 3 distinct bullet points:
    1. **Trending Skills:** What specific tech is hot right now?
    2. **Salary Outlook:** General trend (Rising/Stable) and range.
    3. **Hidden Opportunities:** Which industries are hiring this role unexpectedly?
    """
    return model.generate_content(prompt).text

def interview_post_mortem(question, role):
    model = get_model()
    prompt = f"""
    Act as a 'Learning Agent'. The user failed an interview for {role}.
    The hard question was: "{question}"
    
    1. **The Concept Gap:** Identify exactly what concept the user lacks.
    2. **The Fix:** Provide a 2-sentence explanation.
    3. **The Resource:** Suggest a specific search term or documentation link.
    """
    return model.generate_content(prompt).text

def full_career_analysis(text, role):
    model = get_model()
    prompt = f"""
    Act as a 'Senior Career Coach'. Review resume: {text} for Role: {role}.
    Output a Markdown report:
    1. **Match Score:** (0-100%)
    2. **Critical Gaps:** List 3 missing skills.
    3. **1-Week Sprint Plan:** Day-by-day schedule to fix gaps.
    """
    return model.generate_content(prompt).text

def draft_email(text, role):
    model = get_model()
    prompt = f"""
    Act as a 'Recruitment Agent'. 
    Write a high-impact cold email to a hiring manager for {role}.
    Use details from this resume: {text}
    Keep it professional, concise, and persuasive.
    """
    return model.generate_content(prompt).text

def generate_interview_question(role, topic):
    model = get_model()
    prompt = f"Ask me one tough technical interview question for a {role} specifically about {topic}. Do not give the answer yet."
    return model.generate_content(prompt).text

# --- UI LAYOUT ---
tab1, tab2, tab3, tab4 = st.tabs(["📈 Profiler & Planner", "🌍 Market Intel", "🧠 Learning Loop", "🎤 Mock Interview"])

# Global State
if 'resume_text' not in st.session_state: st.session_state['resume_text'] = ""
if 'role' not in st.session_state: st.session_state['role'] = "AI Engineer"

# --- TAB 1: PROFILER (Memory & Planning & Action) ---
with tab1:
    st.header("Career Strategist Agent")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
    role_input = st.text_input("Target Role", value=st.session_state['role'])
    
    if uploaded_file:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages: text += page.extract_text()
        st.session_state['resume_text'] = text
        st.session_state['role'] = role_input
        
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 Run Gap Analysis"):
            if st.session_state['resume_text']:
                with st.spinner("Analyzing profile..."):
                    res = full_career_analysis(st.session_state['resume_text'], role_input)
                    st.markdown(res)
    with col2:
        if st.button("✉️ Auto-Draft Email (Action)"):
            if st.session_state['resume_text']:
                with st.spinner("Drafting application..."):
                    email = draft_email(st.session_state['resume_text'], role_input)
                    st.subheader("Ready-to-Send Draft")
                    st.code(email, language='markdown')

# --- TAB 2: MARKET SCOUT (Reasoning) ---
with tab2:
    st.header("Real-Time Market Scout")
    if st.button("📊 Scout Trends"):
        with st.spinner("Scouting market..."):
            trends = analyze_market_trends(st.session_state['role'])
            st.markdown(trends)

# --- TAB 3: LEARNING LOOP (Learning) ---
with tab3:
    st.header("Active Feedback Loop")
    tough_question = st.text_input("What interview question stumped you?")
    if st.button("💡 Analyze Failure"):
        with st.spinner("Updating learning model..."):
            feedback = interview_post_mortem(tough_question, st.session_state['role'])
            st.warning("New Learning Module Added:")
            st.markdown(feedback)

# --- TAB 4: MOCK INTERVIEW (Go Beyond) ---
with tab4:
    st.header("AI Interview Simulator")
    topic = st.selectbox("Select Topic", ["Python", "System Design", "Behavioral", "Data Structures"])
    if st.button("🎤 Start Simulation"):
        with st.spinner(f"Agent is preparing {topic} questions..."):
            q = generate_interview_question(st.session_state['role'], topic)
            st.chat_message("assistant").write(q)
            st.info("Answer this question aloud to practice, then click 'Analyze Failure' in Tab 3 if you get stuck!")