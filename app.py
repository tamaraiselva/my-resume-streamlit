from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "styles" / "TAMARAI SELVAN Resume.pdf"
profile_pic = current_dir / "styles" / "IMG_4898.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tamarai selvan Ravi"
PAGE_ICON = ":wave:"
NAME = "Tamarai  Selvan Ravi"
DESCRIPTION = """
A fresher Python developer is someone new to the field who's learning to specialize in using the Python programming language for tasks such as web development (with frameworks like Django or Flask), data science, machine learning, scripting, and automation. 
They're focused on writing clean, efficient code while collaborating with teams using version control systems like Git. 
They're also beginning to understand the importance of testing and documentation for ensuring code quality. 
Even as fresher, Python developers are budding problem solvers who contribute to building diverse software solutions.
"""
EMAIL = "tamaraiselvan98@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
}
PROJECTS = {
    "🏆 UNIVERSITY ADMIN ELIGIBILITY PREDICTOR (Domain: Applied Data Science) IBM PROJECT": "https://github.com/tamaraiselva/E_VOTING_SYSTEM_USING_BLOCKCHAIN",
    "🏆 TEXT SUMMARIZER USING NLP": "https://github.com/tamaraiselva/TEXT_SUMMARIZER_USING_NLP",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE ---
st.write('\n')
st.subheader("**EXPERIENCE CERTIFICATE & INTERNSHIP**")
st.write(
    """
- **Xplore It Corp**
    - ✔️ E-VOTING SYSTEM USING BLOCKCHAIN project 
        tamaraiselva/E_VOTING_SYSTEM_USING_BLOCKCHAIN 
        (github.com). python, database, Django. 
    - ✔️ Image detection with data science 
    - ✔️ Attendance detection system with data science
- **Live Stream Technologies**
    - ✔️ PYTHON/ MYSQL.
- **VERZEO**
    - ✔️ Cyber security engineer.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy, SciPy,), SQL, Twinker.
- ⚙️ Tools and Frameworks
- ✨ Languages : HTML, CSS, JavaScript, C++,
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 🗄️ Databases:MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")