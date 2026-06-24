import streamlit as st
from recommender import recommend_meals

st.set_page_config(
    page_title="Kajal's MealMate AI",
    page_icon="🍽️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background */
.stApp{
    background: #FFF8F0;
}

/* Hero Section */
.hero{
    background: linear-gradient(
        135deg,
        #5B0E2D,
        #7B1436,
        #A61C4F
    );

    padding: 55px;
    border-radius: 30px;

    text-align:center;

    color:white;

    margin-bottom:20px;

    box-shadow:
    0px 10px 30px rgba(0,0,0,0.25);

    position:relative;
    overflow:hidden;
}
.hero::before{

    content:"";

    position:absolute;

    width:300px;

    height:300px;

    background:rgba(255,255,255,0.08);

    border-radius:50%;

    top:-100px;

    right:-50px;
}

.hero h1{
    font-family:'Cinzel', serif;

    font-size:72px;

    font-weight:700;

    letter-spacing:2px;

    margin-bottom:10px;

    text-shadow:
    0px 0px 15px rgba(255,255,255,0.25);
}
.hero p{
    font-size:24px;
    opacity:0.95;
}

/* Gold Divider */
.gold-line{
    height:4px;
    background:#D4AF37;
    border-radius:20px;
    margin:25px 0;
}

/* Form Card */
.form-card{
    background:white;

    padding:25px;

    border-radius:20px;

    border:2px solid #D4AF37;

    box-shadow:
    0px 6px 18px rgba(0,0,0,0.08);

    margin-bottom:25px;
}

/* Best Match */
.best-card{

    background:linear-gradient(
        135deg,
        #FFF8E7,
        #FFF3C4
    );

    border:3px solid #D4AF37;

    border-radius:25px;

    padding:25px;

    text-align:center;

    margin-bottom:25px;

    box-shadow:
    0px 10px 25px rgba(0,0,0,0.1);
}

/* Recommendation Cards */
.meal-card{

    background:white;

    border-radius:20px;

    padding:20px;

    border-left:8px solid #A61C4F;

    box-shadow:
    0px 5px 15px rgba(0,0,0,0.08);

    margin-bottom:15px;
}

/* Button */
.stButton > button{

    width:100%;

    background:#D4AF37;

    color:black;

    font-size:18px;

    font-weight:bold;

    border:none;

    border-radius:15px;

    padding:12px;

    transition:0.3s;
}

.stButton > button:hover{

    background:#A61C4F;

    color:white;
}

/* Stats */
.stats-card{

    background:white;

    border-radius:20px;

    padding:20px;

    text-align:center;

    border:2px solid #D4AF37;

    box-shadow:
    0px 4px 12px rgba(0,0,0,0.08);

    min-height:180px;

    display:flex;

    flex-direction:column;

    justify-content:center;

}
/* Form Labels */

.stSelectbox label{

    font-size:18px !important;

    font-weight:600 !important;

    color:#5B0E2D !important;
}

/* Dropdown Text */

.stSelectbox div[data-baseweb="select"]{

    font-size:17px !important;
}

/* Meal Cards */

.meal-card{

    min-height:220px;
}

/* Best Match */

.best-card{

    min-height:320px;
}
.footer{

    text-align:center;

    margin-top:40px;

    color:#666;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class='hero'>

<h1>🍽️ Kajal's MealMate AI</h1>

<p>
Discover India's Flavours<br>
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
"<div class='gold-line'></div>",
unsafe_allow_html=True
)
# ---------------- FORM ---------------- #
st.markdown("""
<div class='form-card'>
<h3>✨ Find Your Perfect Meal</h3>
</div>
""", unsafe_allow_html=True)

st.subheader("✨ Tell Us Your Preferences")

col1, col2 = st.columns(2)

with col1:

    meal_type = st.selectbox(
        "Meal Time",
        [
            "Breakfast",
            "Brunch",
            "Lunch",
            "Evening Snacks",
            "Dinner"
        ]
    )

    cuisine = st.selectbox(
        "Cuisine",
        [
            "Gujarati",
            "Punjabi",
            "South Indian",
            "North Indian",
            "Maharashtrian",
            "Bengali",
            "Hyderabadi",
            "Rajasthani"
        ]
    )

with col2:

    diet = st.selectbox(
        "Diet",
        [
            "Vegetarian",
            "Non Vegetarian"
        ]
    )

    goal = st.selectbox(
        "Goal",
        [
            "Weight Loss",
            "Weight Gain",
            "Balanced",
            "High Protein"
        ]
    )

mood = st.selectbox(
    "Mood",
    [
        "Healthy",
        "Comfort Food",
        "Party",
        "Festive",
        "Energetic",
        "Spicy"
    ]
)

# ---------------- BUTTON ---------------- #

if st.button("🍛 Recommend Meals"):

    results = recommend_meals(
        meal_type,
        cuisine,
        diet,
        goal,
        mood
    )

    if results is None or len(results) == 0:

        st.warning(
            "No meals found for selected preferences."
        )

    else:

        best_match = results.iloc[0]

        remaining = results.iloc[1:]

        score = max(
            60,
            round(best_match["score"] * 100)
        )

        st.markdown(f"""
        <div class='best-card'>

        <h2>🏆 PERFECT MATCH</h2>

        <h1>{best_match['meal_name']}</h1>

        <h3>⭐ {score}% Match</h3>

        <p>📍 {best_match['cuisine']}</p>

        <p>🎯 {best_match['goal']}</p>

        <p>😊 {best_match['mood']}</p>

        </div>
        """,
        unsafe_allow_html=True)

        if len(remaining) > 0:                                                                                                                                                            

            st.subheader("🍛 More Recommendations")

        for _, row in remaining.iterrows():

            score = max(
                60,
                round(row["score"] * 100)
            )

            st.markdown(f"""
            <div class='meal-card'>

            <h3>🍽️ {row['meal_name']}</h3>

            <p>⭐ {score}% Match</p>

            <p>📍 {row['cuisine']}</p>

            <p>🎯 {row['goal']}</p>

            <p>😊 {row['mood']}</p>

            </div>
            """,
            unsafe_allow_html=True)  
            
      
st.markdown(
"<div class='gold-line'></div>",
unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='stats-card'>
    <h2>🍛</h2>
    <h4>150+ Meals</h4>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='stats-card'>
    <h2>🌶️</h2>
    <h4>Indian Flavours</h4>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='stats-card'>
    <h2>🤖</h2>
    <h4>AI Powered</h4>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='stats-card'>
    <h2>❤️</h2>
    <h4>Personalized</h4>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
Made with ❤️ by Kajal
</div>
""",
unsafe_allow_html=True)

