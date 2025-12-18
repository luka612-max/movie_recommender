# 🎬 Movie Matcher: Content-Based Recommendation System

Movie Matcher is a machine learning-powered web application that suggests films based on structural similarities. By analyzing metadata from the TMDB 5000 dataset, the app calculates the "distance" between movies to provide highly relevant suggestions.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 🚀 Overview

The project consists of a full-stack data science pipeline:
1.  **Modeling (`movie_recommeder.ipynb`):** Handles data cleaning, merging the `tmdb_5000_movies` and `tmdb_5000_credits` datasets, and generating a similarity matrix.
2.  **Deployment (`main.py`):** A modern Streamlit interface that utilizes the TMDB API to fetch live posters and display recommendations in a responsive 5-column layout.

## 🧠 Technical Workflow

### Data Preprocessing
* **Feature Engineering**: Combined `overview`, `genres`, `keywords`, `cast`, and `crew` into a single `tags` column.
* **Data Sanitization**: Removed spaces from names (e.g., "James Cameron" to "JamesCameron") to prevent the model from confusing different people with the same first name.
* **Text Processing**: Converted all tags to lowercase and utilized `ast.literal_eval` to parse JSON-formatted metadata.

### Machine Learning Logic
* **Vectorization**: Used `CountVectorizer` to convert text tags into 5000-dimensional vectors, excluding English stop words.
* **Similarity Metric**: Implemented **Cosine Similarity** to calculate the distance between movie vectors.
* **Persistence**: The processed dataframe and similarity matrix are exported as `movie_list.pkl` and `similarity.pkl` using Pickle for use in the web app.

## 📂 Project Structure

```text
├── data/
│   ├── tmdb_5000_movies.csv     # Raw movie data
│   └── tmdb_5000_credits.csv    # Raw credits data
├── movie_recommeder.ipynb       # Data processing & Model building
├── main.py                      # Streamlit frontend code
├── movie_list.pkl               # Processed movie dataframe (Generated)
├── similarity.pkl               # Similarity matrix (Generated)
└── README.md                    # Project documentation

## 🛠️  Installation & Setup
# 1. Clone the repository
git clone [https://github.com/your-username/movie-matcher.git](https://github.com/your-username/movie-matcher.git)
cd movie-matcher

# 2. Install required dependencies
pip install streamlit pandas requests scikit-learn urllib3

# 3. Process the data and generate models
# Open movie_recommeder.ipynb and run all cells to create the .pkl files

# 4. Launch the Streamlit application
streamlit run main.py 
