import streamlit as st
import json
import os
import pandas as pd
import altair as alt
#NEW
# Set page configuration
st.set_page_config(page_title="Sanrio Vote", page_icon="😺", layout="centered")

# File to store votes
VOTES_FILE = "votes.json"

# Sanrio character list
characters = ["Hello Kitty", "My Melody", "Cinnamoroll", "Kuromi", "Keroppi", "Badtz-Maru"]
character_images = {
    "Hello Kitty": "images/hellokitty.png",
    "My Melody": "images/mymelo.webp",
    "Cinnamoroll": "images/cinna.webp",
    "Kuromi": "images/kuromi.webp",
    "Keroppi": "images/kerropi.png",
    "Badtz-Maru": "images/badtz.png"
}

# Check if votes.json exists, if not, create it
if not os.path.exists(VOTES_FILE):
    votes_data = {char: 0 for char in characters}
    with open(VOTES_FILE, "w") as file:
        json.dump(votes_data, file)
else:
    with open(VOTES_FILE, "r") as file:
        votes_data = json.load(file)

# Function to update votes in JSON
def update_votes(character):
    votes_data[character] += 1
    with open(VOTES_FILE, "w") as file:
        json.dump(votes_data, file)

# Set session states for "About Me" section
if 'favourite_character' not in st.session_state:
    st.session_state['favourite_character'] = ''

def setFavouriteCharacter(character):
    st.session_state['favourite_character'] = character

# Title based on selected character in "About Me"
match st.session_state['favourite_character']:
    case 'Hello Kitty':
        st.title('🐱 About Me Data')
    case 'Kuromi':
        st.title('💀 About Me Data')
    case 'My Melody':
        st.title('🎀 About Me Data')
    case _:
        st.title('About Me Data')
#NEW st.button
# Display "About Me Data" section
st.header('Choose your theme')
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button('My Melody', on_click=setFavouriteCharacter, args=('My Melody',))
    with col2:
        st.button('Kuromi', on_click=setFavouriteCharacter, args=('Kuromi',))
    with col3:
        st.button('Hello Kitty', on_click=setFavouriteCharacter, args=('Hello Kitty',))
#NEW st.session_state
# Voting Section
st.header("✨ Vote for Your Favorite Character! ✨")
if "has_voted" not in st.session_state:
    st.session_state["has_voted"] = False
#NEW st.radio
if not st.session_state["has_voted"]:
    selected_character = st.radio("Choose your favorite character:", characters, format_func=lambda x: f"{x} 🐱")

    st.image(character_images[selected_character], width=100)

    if st.button("Vote! 💖"):
        update_votes(selected_character)
        st.session_state["has_voted"] = True
        st.success(f"Thank you for voting for {selected_character}! 🎉")
    
    # Display the bar chart right after voting
    # Convert votes dictionary into DataFrame for character votes
    df_votes = pd.DataFrame({"Character": list(votes_data.keys()), "Votes": list(votes_data.values())})
    df_votes = df_votes.set_index("Character")  # Streamlit's charts require an index

    # Display Bar Chart (Character Votes)
    st.subheader("Votes per Character")
    st.bar_chart(df_votes["Votes"])
#NEW st.info
else:
    st.info("You've already voted! Refresh the page to vote again.")

# New Section: Checkbox for Categories
st.header("📊 Assign Characters to Categories 📊")

# Create dictionary to store categories (initially empty)
character_categories = {character: None for character in characters}

# Loop through each character and create checkboxes for "Cute" and "Cool"
for character in characters:
    st.subheader(character)
    character_categories[character] = st.radio(
        f"Select a category for {character}:",
        options=["Cute", "Cool"],
        key=character
    )

# Button to submit the category selections
if st.button("Submit Category Selections"):

    # Count the number of "Cute" and "Cool" votes
    category_counts = {"Cute": 0, "Cool": 0}
    
    for category in character_categories.values():
        if category is not None:  # Make sure the category is selected
            category_counts[category] += 1

    # Display Pie Chart for Cute and Cool Votes using Altair
    st.subheader("Votes by Category")
    
    # Creating Pie chart data using Pandas
    pie_data = pd.DataFrame(list(category_counts.items()), columns=["Category", "Votes"])

    # Altair Pie Chart
    pie_chart = alt.Chart(pie_data).mark_arc().encode(
        theta=alt.Theta(field="Votes", type="quantitative"),
        color=alt.Color(field="Category", type="nominal"),
        tooltip=["Category", "Votes"]
    ).properties(title="Votes by Category")

    st.altair_chart(pie_chart, use_container_width=True)

# Simple Line Chart for Hello Kitty's Personality Traits
st.header("🌟 Hello Kitty's Personality Traits")

# Defining Hello Kitty's personality traits with values (1-10 scale)
personality_traits = {
    "Cuteness": 10,
    "Friendliness": 9,
    "Adventure": 6,
    "Playfulness": 8,
    "Creativity": 7,
    "Curiosity": 8
}

# Convert to a DataFrame for Altair
traits_df = pd.DataFrame(list(personality_traits.items()), columns=["Trait", "Value"])

# Create a simple line chart for personality traits using Altair
line_chart = alt.Chart(traits_df).mark_line(point=True).encode(
    x=alt.X('Trait:N', sort=None),
    y='Value:Q',
    color='Trait:N',
    tooltip=['Trait', 'Value']
).properties(title="Hello Kitty's Personality Traits")

st.altair_chart(line_chart, use_container_width=True)


