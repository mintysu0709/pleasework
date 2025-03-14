import streamlit as st
import pandas as pd
with open('styles.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "WebDevLab02/images/hellokitty.png"
about_me = "I'm Hello Kitty. I am the mayor of Sanrioville and love to hang out with my friends. "


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/spongebob-squarepants-44b857281/"
my_github_url = "https://github.com/your-github-username"
my_email_address = "hyun.sumin0709@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Computer Science',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'Never',
    'GPA': '4.0'
}
course_data = {
    "code":["🎀CS 1301", "🍞CS 1331", "☕MATH 1554", "🌸CS 2050"], 
    "names":["Intro to CS", "Intro to OOP", "Linear Algebra", "Discrete Mathematics"], 
    "semester_taken":["2nd", "3rd", "2nd", "2nd"],
    "skills":["Python is not my favorite snake anymore", "OOP(S!) (Java Edition)", "Basically row reduction", "If only my grade was discrete too..."],
    }
experience_data = {
    "Owner & Baker at Hello Kitty Café ☕🍰": (["- Worked on designing a cookie recipe for everyone in Sanrioville",
                                                                          "- Increased Company Revenue by 10000000 dollars", "- Won the best baker award"],"WebDevLab02/images/kittycook.jpeg"),
    "Dishwasher at Hello Kitty Café ☕🍰":(["- Washed 100 plates per day",
                                                           "- Kept the kitchen spotless"],"WebDevLab02/images/hellokittycleaning.jpg"),
    "Architect & Founder of Sanrioville 🏗️🏡":(["- Designed and constructed the entire town of Sanrioville, ensuring it was the cutest, most functional, and happiest place to live."],"WebDevLab02/images/hellokittywork.jpeg")

}

projects_data = {
    "Sanrio Character Popularity Poll": """
    **Sanrio Character Popularity Poll** 🎀  
    This app lets you vote for your favorite Sanrio character and instantly see live results!  
    - Displays **dynamic bar chart** for voting results.  
    - Displays a **simple line chart** for Hello Kitty's personality traits.  
    - Displays a **pie chart** for votes categorized as "Cute" or "Cool".  
    """,
    # Add other projects here
}


programming_data = {
    "Python": 90,
    "Java": 70,
    "C": 40,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {"Japanese": "🇯🇵",
    "Sanriovian(Official language of Sanrioville)": "🐱",
    "ASL(American Sign Language)":"🤟"
}

#CHANGE BELOW
spoken_data = {
    "Sanriovian(Official language of Sanrioville)": "Native",
    "Japanese": "Fluent",
    "ASL(American Sign Language)": "Fluent",
}
leadership_data = {
    "Mayor of Sanrioville": (["- Elected best mayor"],"WebDevLab02/images/hellokittydrive.jpeg"),

}
activity_data={
    "Sanrio Friendship Club 💕": ["- Picking flowers with MyMelody", 
            "- Hosting Cozy Nap Time Under a Giant Mushroom 🍄💤"]
}



#About Me
def about_me_section():
    st.header("About Me")
    st.image(profile_picture,width=200)
    st.write(about_me)
    st.write('---')
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link=f'<a href="{my_linkedin_url}"><img src="{linkedin_image_url}" alt="LinkedIn" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link,unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link=f'<a href="{my_github_url}"><img src="{github_image_url}" alt="Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link,unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html= f'<a href= "mailto:{my_email_address}"><img src="{email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data,course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.markdown(f"**Degree:** {education_data['Degree']}")
    st.markdown(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.markdown(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework,column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("---")
education_section(education_data, course_data) 

#Professional Experience

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description,image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image,width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(experience_data)

#Projects

def project_section(projects_data):
    st.header("Projects")
    for project_name,project_description in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(projects_data)

#Skills

def skills_section(programming_data,spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{programming_icons.get(skill, '')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{spoken_icons.get(spoken, '')}: {proficiency}")
skills_section(programming_data, spoken_data)

#Activities

def activities_section(leadership_data, activities_data):
    st.header("Activities")
    tab1,tab2 = st.tabs(["Leadership","Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title,(details,image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image,width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activities_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(leadership_data,activity_data)


