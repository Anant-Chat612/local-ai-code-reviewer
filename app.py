import streamlit as st
import ast
import requests

# Page Configuration
st.set_page_config(page_title="AI Python Code Reviewer (Local)", page_icon="🐍", layout="wide")

st.title("🐍 Local AI-Powered Python Code Reviewer")
st.write("Powered by Ollama running locally on your Mac—no internet or API keys required!")

# Main Layout: Two columns (Input on left, Output on right)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Python Code")
    code_input = st.text_area(
        "Paste code here:", 
        height=300, 
        placeholder="def add(a, b):\n    return a + b"
    )
    analyze_btn = st.button("Analyze Code", type="primary")

with col2:
    st.subheader("Analysis & Feedback")
    
    if analyze_btn:
        if not code_input.strip():
            st.warning("Please enter some Python code first!")
        else:
            # 1. Show the code with line numbers first for easy reference
            st.markdown("### 📄 Code Reference (with Line Numbers)")
            st.code(code_input, language="python", line_numbers=True)

            # 2. Local AST Systematic Syntax Check
            syntax_ok = True
            try:
                ast.parse(code_input)
                st.success("✅ **Local Syntax Check:** Valid (No syntax errors detected)")
            except SyntaxError as e:
                syntax_ok = False
                st.error(
                    "### ❌ Syntax Error Detected\n\n"
                    f"* **Line Number:** `{e.lineno}`\n"
                    f"* **Error Type:** `SyntaxError`\n"
                    f"* **Issue Description:** {e.msg}\n"
                    f"* **Problematic Code:** `{e.text.strip() if e.text else 'N/A'}`\n\n"
                    f"👉 **How to Fix:** Look at **Line {e.lineno}** above and fix the syntax issue."
                )
            
            # 3. AI Code Review using Local Ollama (Only if syntax is clean)
            if syntax_ok:
                with st.spinner("Local AI is analyzing your code quality and logic..."):
                    try:
                        prompt = (
                            "You are an expert Python software engineer and code reviewer.\n"
                            "Analyze the following Python code and format your response systematically with these exact sections:\n"
                            "1. **Code Quality Evaluation:** (Brief overview)\n"
                            "2. **Bugs & Performance Issues:** (Line numbers and descriptions if any)\n"
                            "3. **Refactored Code:** (Clean, Pythonic code snippet)\n\n"
                            f"Here is the code:\n{code_input}"
                        )
                        
                        response = requests.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": "llama3",
                                "prompt": prompt,
                                "stream": False
                            }
                        )
                        
                        if response.status_code == 200:
                            result = response.json().get("response", "No response generated.")
                            st.markdown("### 🤖 Systematic AI Review")
                            st.markdown(result)
                        else:
                            st.error("Could not connect to local Ollama server. Make sure the Ollama app is running.")
                            
                    except Exception as e:
                        st.error(f"An error occurred: {e}")