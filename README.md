# 🧠 Emotion Intelligence — NLP Emotion Classifier

An AI-powered web application that detects human emotions from text using Natural Language Processing and Machine Learning, built with **Streamlit**.

> 🎯 Built as part of a hands-on NLP learning journey — from raw text preprocessing to a fully deployed ML web app.

---

## ✨ Features

- Classifies text into **6 emotions**: Joy, Sadness, Anger, Fear, Love, Surprise
- Displays **confidence score** for the predicted emotion
- Interactive **emotion probability distribution** bar chart
- Sleek dark-themed UI with modern 3D gold-accent styling
- Real-time prediction with a clean, minimal interface
- Handles noisy text — removes punctuation, numbers, emojis, and stopwords automatically

---

## 🖥️ Live Demo

> Enter any sentence → Click **Analyze Emotion** → Get instant results with confidence scores and a full emotion probability breakdown.

---

## 🗂️ Project Structure

```
emotion-intelligence-nlp/
│
├── app.py                  # Streamlit web application
├── model.pkl               # Trained ML classification model
├── vectorizer.pkl          # Bag-of-Words vectorizer
├── train.txt               # Training dataset
├── 1. NLP_Basic.ipynb      # Jupyter notebook (EDA + Model Training)
└── README.md
```

---

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/Namanbansal9414/emotion-intelligence-nlp.git
cd emotion-intelligence-nlp
```

**2. Install dependencies**
```bash
pip install streamlit scikit-learn nltk pandas
```

**3. Download NLTK stopwords**
```python
import nltk
nltk.download('stopwords')
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 🧪 How It Works

### 🔹 Step 1 — Text Preprocessing
Raw input text goes through a cleaning pipeline:
- Converted to **lowercase**
- **Punctuation** removed
- **Numbers** removed
- **Emojis** removed
- **Stopwords** removed using NLTK

### 🔹 Step 2 — Vectorization
The cleaned text is transformed into a numerical feature vector using a **Bag-of-Words (BoW)** approach via a pre-trained `CountVectorizer`.

### 🔹 Step 3 — Prediction
A trained **Machine Learning classifier** predicts the most likely emotion and outputs a probability score for all 6 emotion classes.

### 🔹 Step 4 — Visualization
Results are displayed as:
- A **highlighted emotion card** with the predicted label
- A **confidence percentage**
- A **bar chart** showing the full probability distribution across all emotions

---

## 🏷️ Emotion Labels

| Label | Emotion     | Description                               |
|-------|-------------|-------------------------------------------|
| 0     | 😢 Sadness  | Expressions of grief, loss, or sorrow     |
| 1     | 😡 Anger    | Frustration, rage, or irritation          |
| 2     | 🩷 Love     | Affection, warmth, or romantic feelings   |
| 3     | 😲 Surprise | Shock, amazement, or unexpectedness       |
| 4     | 😨 Fear     | Anxiety, dread, or worry                  |
| 5     | 😄 Joy      | Happiness, excitement, or delight         |

---

## 🛠️ Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| Python        | Core language                    |
| Scikit-learn  | Model training & vectorization   |
| NLTK          | Text preprocessing & stopwords   |
| Streamlit     | Interactive web interface        |
| Pandas        | Data manipulation                |
| Pickle        | Model serialization              |

---

## 📓 Notebook

The `1. NLP_Basic.ipynb` notebook covers the complete ML pipeline:
- Exploratory Data Analysis (EDA)
- Text cleaning & preprocessing
- Feature extraction with Bag-of-Words
- Model training & evaluation
- Exporting the model and vectorizer

---

## 🚀 Future Improvements

-  Add support for **multilingual** emotion detection
-  Upgrade to **TF-IDF** or **transformer-based** embeddings (BERT)
-  Add **history log** to track past predictions
-  Deploy on **Streamlit Cloud** or **Hugging Face Spaces**
-  Add **real-time** character and word count display

---

## 👨‍💻 Author

**Naman Bansal**

Passionate about Machine Learning, NLP, and building intelligent applications that bridge the gap between data and real-world problems.

---

## 📬 Contact

Feel free to reach out for collaborations, feedback, or just to connect!

| Platform   | Link |
|------------|------|
| 🐙 GitHub   | [Namanbansal9414](https://github.com/Namanbansal9414) |
| 💼 LinkedIn | [namanbansal9509](https://www.linkedin.com/in/namanbansal9509/) |
| 📧 Email    | [namanbansal9509@gmail.com](mailto:namanbansal9509@gmail.com) |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---