# import pickle
# import string
# import nltk
# import streamlit as st
# from nltk.corpus import stopwords

# stop_words = set(stopwords.words("english"))

# def remove_punc(txt):
#     return txt.translate(str.maketrans('','',string.punctuation))

# def remove_nums(txt):
#     new = ""
#     for i in txt:
#         if not i.isdigit():
#             new = new +i
#     return new

# def remove_emojis(txt):
#     new = ""
#     for i in txt:
#         if i.isascii():
#             new +=i
#     return new

# def remove_stopword(txt):
#     words = txt.split()
#     cleaned =[]
#     for i in words:
#         if not i in stop_words:
#             cleaned.append(i)
#     return ' '.join(cleaned)


# bow = pickle.load(open('vectorizer.pkl','rb'))
# model = pickle.load(open('model.pkl', 'rb'))


# st.title("Emotion Classifer")

# input_sms = st.text_area("Enter the message")

# if st.button('predict'):
#     lower_word = input_sms.lower()

#     punc_rem_sms = remove_punc(lower_word)

#     remove_nums_sms = remove_nums(punc_rem_sms)

#     remove_emojis_sms = remove_emojis(remove_nums_sms)

#     remove_stopword_sms = remove_stopword(remove_emojis_sms)


#     vector_input = bow.transform([remove_stopword_sms])


#     result = model.predict(vector_input)[0]


#     if result == 0:
#         st.header("Sadness")
#     elif result == 1:
#         st.header("Anger")
#     elif result == 2:
#         st.header("Love")
#     elif result == 3:
#         st.header("Surprise")
#     elif result == 4:
#         st.header("Fear")
#     elif result == 5:
#         st.header("Joy")
#     else:
#         st.header("error")



import pickle
import string
import nltk
import streamlit as st
import pandas as pd
from nltk.corpus import stopwords

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Emotion Intelligence",
    page_icon="🖤",
    layout="centered"
)

# ---------------- MODERN 3D STYLE ----------------
st.markdown("""
<style>

/* Remove Streamlit top spacing */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem;
    max-width: 750px;
}

/* Background */
.stApp {
    background: radial-gradient(circle at 20% 20%, #1a1a1a, #0d0d0d 70%);
    color: #f0f0f0;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
h1 {
    text-align: center;
    font-size: 38px !important;
    font-weight: 600 !important;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #9c9c9c;
    margin-bottom: 25px;
}


/* Text Area */
div[data-baseweb="textarea"] textarea {
    background: #161616 !important;
    color: #ffffff !important;
    border-radius: 14px !important;
    border: 1px solid #2c2c2c !important;
    padding: 14px !important;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.6);
}



/* Button 3D Gold */
.stButton>button {
    background: linear-gradient(145deg, #d4af37, #b8962e);
    color: black;
    border-radius: 35px;
    height: 50px;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
    box-shadow:
        0 6px 15px rgba(0,0,0,0.6),
        inset 0 1px 1px rgba(255,255,255,0.5);
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 10px 20px rgba(0,0,0,0.8),
        0 0 15px rgba(212,175,55,0.5);
}

/* Result Card */
.result {
    text-align: center;
    padding: 25px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow:
        0 10px 30px rgba(0,0,0,0.7);
    margin-top: 25px;
}

/* Chart title */
.chart-title {
    margin-top: 30px;
    font-weight: 500;
    color: #c9c9c9;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>Emotion Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered emotion detection system</div>", unsafe_allow_html=True)

# ---------------- PREPROCESSING ----------------
stop_words = set(stopwords.words("english"))

def remove_punc(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

def remove_nums(txt):
    return ''.join([i for i in txt if not i.isdigit()])

def remove_emojis(txt):
    return ''.join([i for i in txt if i.isascii()])

def remove_stopword(txt):
    words = txt.split()
    return ' '.join([i for i in words if i not in stop_words])

# ---------------- LOAD MODEL ----------------
bow = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

emotion_labels = {
    0: "Sadness",
    1: "Anger",
    2: "Love",
    3: "Surprise",
    4: "Fear",
    5: "Joy"
}

# ---------------- INPUT SECTION ----------------
st.markdown("<div class='glass'>", unsafe_allow_html=True)

input_sms = st.text_area("Enter your message")
predict = st.button("Analyze Emotion")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if predict:

    if input_sms.strip() == "":
        st.warning("Please enter text before analyzing.")
    else:
        with st.spinner("Analyzing..."):

            processed = remove_stopword(
                remove_emojis(
                    remove_nums(
                        remove_punc(
                            input_sms.lower()
                        )
                    )
                )
            )

            vector_input = bow.transform([processed])
            result = model.predict(vector_input)[0]
            probabilities = model.predict_proba(vector_input)[0]

            predicted_emotion = emotion_labels[result]
            confidence = max(probabilities) * 100

        st.markdown(f"""
        <div class='result'>
            <h2>{predicted_emotion}</h2>
            <p style='color:#d4af37; font-size:20px;'>Confidence: {confidence:.2f}%</p>
        </div>
        """, unsafe_allow_html=True)

        prob_df = pd.DataFrame({
            "Emotion": emotion_labels.values(),
            "Probability": probabilities
        })

        st.markdown("<div class='chart-title'>Emotion Distribution</div>", unsafe_allow_html=True)
        st.bar_chart(prob_df.set_index("Emotion"))