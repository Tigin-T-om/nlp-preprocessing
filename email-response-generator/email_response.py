import streamlit as st
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from datetime import datetime
import re

# Page configuration
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="✉️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for new look
st.markdown("""
<style>
.stApp { background: linear-gradient(to right, #3d1f5c, #6c2c83); color: #f0f0f0; }
.title { font-size: 3rem; font-weight: 700; color: #f3e8ff; text-align: center; margin-bottom: 0.5rem; }
.subtitle { font-size: 1.2rem; color: #ddd; text-align: center; margin-bottom: 2rem; }
.input-box { background-color: #4a2673; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); margin-bottom: 1rem; color: #f0f0f0; }
.output-box { background-color: #5b3a8c; padding: 1.5rem; border-radius: 12px; border-left: 6px solid #f0a500; margin-bottom: 1rem; color: #f0f0f0; }
.stButton>button { background: linear-gradient(90deg,#6c2c83,#9b5de5); color: white; font-weight: bold; border-radius: 30px; padding: 0.6rem 2.5rem; transition: 0.3s; }
.stButton>button:hover { background: linear-gradient(90deg,#4a1d6f,#7f3fbf); }
textarea, input, select { background-color: #4a2673 !important; color: #f0f0f0 !important; border: 1px solid #9b5de5 !important; }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-small"  # can upgrade to flan-t5-base for better results
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

# Extract sender name from email
def extract_sender_name(email_text: str) -> str:
    match = re.search(r"(Best|Regards|Sincerely|Thanks)[,\s]+([A-Z][a-zA-Z]+)", email_text, re.IGNORECASE)
    if match:
        return match.group(2)
    return "[Name]"

# Main app
def main():
    st.markdown('<div class="title">✉️ AI Email Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Generate professional or casual email responses in seconds</div>', unsafe_allow_html=True)

    tokenizer, model = load_model()
    if tokenizer is None or model is None:
        st.error("Failed to load AI model.")
        return

    col1, col2 = st.columns([1,1])

    with col1:
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.subheader("Original Email 📨")
        original_email = st.text_area(
            "Paste email here:",
            height=250,
            placeholder="Hi Team, I wanted to discuss the upcoming project deadlines..."
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        st.subheader("Settings ⚙️")
        tone = st.selectbox("Select Tone:", ["Professional", "Casual", "Apologetic", "Grateful", "Urgent"])
        context = st.text_input("Email Context/Subject:", placeholder="e.g., Project update, meeting request")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="output-box">', unsafe_allow_html=True)
        st.subheader("Generated Response ✨")

        if st.button("Generate Response"):
            if original_email.strip() and context.strip():
                with st.spinner("Generating response..."):
                    response = generate_email_response(original_email, tone, context, tokenizer, model)
                    st.session_state.generated_response = response
            else:
                st.warning("Please provide both email and context.")

        if hasattr(st.session_state, 'generated_response'):
            st.text_area("Your Response:", value=st.session_state.generated_response, height=300)
            st.download_button(
                "Download Response 📥",
                data=st.session_state.generated_response,
                file_name=f"email_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("💡 Tips")
    st.markdown("""
    - Include full email for better context  
    - Be clear about the tone and urgency  
    - Check generated response before sending  
    """)

# Generate email response
def generate_email_response(original_email, tone, context, tokenizer, model):
    sender_name = extract_sender_name(original_email)

    tone_instructions = {
        "Professional": "Write a professional and formal email response.",
        "Casual": "Write a casual and friendly email response.",
        "Apologetic": "Write an apologetic and understanding email response.",
        "Grateful": "Write a grateful and appreciative email response.",
        "Urgent": "Write an urgent but polite email response."
    }

    prompt = f"""
You are an AI email assistant. Your task is to write a {tone.lower()} email response.

Tone: {tone}
Instruction: {tone_instructions[tone]}
Context: {context}

Original email:
{original_email}

Write a polite and well-formatted email reply. 
Start with an appropriate greeting using the sender's name ({sender_name}) if available, 
then address the context, and end with a closing and signature.
"""

    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=400,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,  # allow randomness to prevent repetition
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Fallback if too short or model fails
    if len(response) < 40:
        response = generate_template_response(original_email, tone, context, sender_name)

    return response

# Fallback template generator
def generate_template_response(original_email, tone, context, sender_name):
    templates = {
        "Professional": f"Dear {sender_name},\n\nThank you for your email regarding {context}. I will review the details and get back to you shortly.\n\nBest regards,\n[Your Name]",
        "Casual": f"Hi {sender_name},\n\nThanks for reaching out about {context}. Let's catch up soon!\n\nCheers,\n[Your Name]",
        "Apologetic": f"Dear {sender_name},\n\nI apologize for any inconvenience regarding {context}. I'll do my best to resolve this quickly.\n\nBest regards,\n[Your Name]",
        "Grateful": f"Dear {sender_name},\n\nThank you for your message about {context}. I really appreciate it.\n\nWith appreciation,\n[Your Name]",
        "Urgent": f"Dear {sender_name},\n\nI understand the urgency regarding {context}. I'll prioritize this matter immediately.\n\nBest regards,\n[Your Name]"
    }
    return templates.get(tone, templates["Professional"])

if __name__ == "__main__":
    main()
