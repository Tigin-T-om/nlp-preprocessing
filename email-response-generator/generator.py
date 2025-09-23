# generator_ui_v2.py

import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Email Template Generator",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
.stApp { 
    background: linear-gradient(to right, #3d1f5c, #6c2c83); 
    color: #f0f0f0; 
}
.title { 
    font-size: 2.8rem; font-weight: 700; 
    color: #f3e8ff; 
    text-align:center; margin-bottom:0.5rem; 
}
.subtitle { 
    font-size:1.2rem; color:#ddd; 
    text-align:center; margin-bottom:2rem; 
}
.input-box, .output-box {
    background:#4a2673; 
    padding:1.5rem; 
    border-radius:12px; 
    box-shadow:0 4px 12px rgba(0,0,0,0.3); 
    margin-bottom:1rem; 
    color:#f0f0f0;
}
.output-box { 
    border-left:6px solid #f0a500; 
    background:#5b3a8c; 
}
.stButton>button {
    background: linear-gradient(90deg,#6c2c83,#9b5de5); 
    color:white; font-weight:bold; border-radius:30px; padding:0.6rem 2.5rem; transition:0.3s;
}
.stButton>button:hover { 
    background: linear-gradient(90deg,#4a1d6f,#7f3fbf);
}
textarea, input, select {
    background-color: #4a2673 !important; 
    color: #f0f0f0 !important; 
    border: 1px solid #9b5de5 !important;
}
</style>
""", unsafe_allow_html=True)

# Template logic (kept intact)
def generate_template_response(original_email, tone, context):
    sender_name = "there"
    for line in original_email.split('\n'):
        if any(word in line.lower() for word in ['best', 'regards', 'sincerely', 'thanks']):
            words = line.split()
            if len(words) > 1: sender_name = words[-1].replace(',',''); break
    templates = {
        "Professional": f"Dear {sender_name},\n\nThank you for your email regarding {context}.\n\nBest regards,\n[Your Name]",
        "Casual": f"Hi {sender_name}!\n\nThanks for reaching out about {context}.\n\nCheers,\n[Your Name]",
        "Apologetic": f"Dear {sender_name},\n\nI apologize for any inconvenience regarding {context}.\n\nBest regards,\n[Your Name]",
        "Grateful": f"Dear {sender_name},\n\nThank you for your message about {context}.\n\nWith appreciation,\n[Your Name]",
        "Urgent": f"Dear {sender_name},\n\nI understand the urgency regarding {context}.\n\nBest regards,\n[Your Name]",
        "Follow-up": f"Dear {sender_name},\n\nI hope this email finds you well. I wanted to follow up on {context}.\n\nBest regards,\n[Your Name]",
        "Meeting Request": f"Dear {sender_name},\n\nThank you for your email regarding {context}.\n\nI would be happy to schedule a meeting. Let me know your availability.\n\nBest regards,\n[Your Name]"
    }
    return templates.get(tone, templates["Professional"])

def enhance_response_with_context(response, original_email, context):
    email_lower = original_email.lower()
    if "meeting" in email_lower or "schedule" in email_lower:
        response = response.replace("I will look into this matter","I would be happy to schedule a meeting")
    if "urgent" in email_lower or "asap" in email_lower:
        response = response.replace("shortly","as soon as possible").replace("within the next few hours","immediately")
    if "thank" in email_lower: response = response.replace("Thank you for your email","Thank you for your kind message")
    if "question" in email_lower or "help" in email_lower:
        response = response.replace("I will look into this matter","I'll be happy to help answer your questions")
    return response

# Main UI
def main():
    st.markdown('<div class="title">✉️ AI Email Template Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Generate smart email responses using templates</div>', unsafe_allow_html=True)
    st.info("🚀 Template Version: Smart templates with context-aware enhancements!")

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        tone = st.selectbox("Select Tone:", ["Professional", "Casual", "Apologetic", "Grateful", "Urgent", "Follow-up", "Meeting Request"])
        context = st.text_input("Email Context/Subject:", placeholder="e.g., project update, meeting request")
        st.subheader("📋 Quick Templates")
        if st.button("Meeting Request"): st.session_state.template_context, st.session_state.template_tone = "meeting request","Meeting Request"
        if st.button("Project Update"): st.session_state.template_context, st.session_state.template_tone = "project update","Professional"
        if st.button("Thank You"): st.session_state.template_context, st.session_state.template_tone = "thank you message","Grateful"
        if st.button("Apology"): st.session_state.template_context, st.session_state.template_tone = "apology","Apologetic"

    # Columns
    col1,col2 = st.columns([1,1])

    with col1:
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.subheader("📨 Original Email")
        original_email = st.text_area("Paste email here:", height=300, placeholder="Hi John, ...")
        if hasattr(st.session_state,'template_context'): context = st.session_state.template_context
        if hasattr(st.session_state,'template_tone'): tone = st.session_state.template_tone
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.subheader("✨ Generated Response")
        if st.button("🚀 Generate Response"):
            if original_email.strip() and context.strip():
                response = generate_template_response(original_email, tone, context)
                enhanced = enhance_response_with_context(response, original_email, context)
                st.session_state.generated_response = enhanced
                st.session_state.generation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                st.warning("Provide both email and context!")
        if hasattr(st.session_state,'generated_response'):
            st.text_area("Your Response:", value=st.session_state.generated_response, height=300)
            st.download_button("📥 Download Response", data=st.session_state.generated_response, file_name=f"email_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", mime="text/plain")
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer tips
    st.markdown("---")
    st.subheader("💡 Tips")
    col1,col2,col3 = st.columns(3)
    with col1: st.markdown("**📝 Original Email**\n- Include full email\n- Keep sender's name\n- Include context")
    with col2: st.markdown("**🎯 Context**\n- Be specific about topic\n- Mention urgency if needed\n- Include keywords")
    with col3: st.markdown("**✨ Tone**\n- Professional: Business emails\n- Casual: Friends/colleagues\n- Apologetic: Mistakes/delays")

    # Sidebar stats
    if hasattr(st.session_state,'generated_response'):
        st.sidebar.markdown("---")
        st.sidebar.subheader("📊 Session Stats")
        st.sidebar.info(f"Last generated: {st.session_state.generation_time}")
        st.sidebar.success("✅ Template engine ready")

if __name__ == "__main__":
    main()
