import pickle
import streamlit as st
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# --- 1. Robust API Setup ---
def get_session():
    session = requests.Session()
    # Corrected typo: status_forcelist
    retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    return session


session = get_session()

# --- 2. Stylish UI Configuration ---
st.set_page_config(page_title="Movie Match", layout="wide")

# Custom CSS for a modern look
# Corrected typo: unsafe_allow_html=True
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff1a1a;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)


# --- 3. Functions with Caching ---
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f1be139845e670c0b523b9de4eb5d053&language=en-US"
    try:
        response = session.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"


@st.cache_data
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        posters.append(fetch_poster(movie_id))
        names.append(movies.iloc[i[0]].title)
    return names, posters


# --- 4. Main App Interface ---
st.title('🎬 Movie Matcher')
st.caption('Discover your next favorite film based on millions of data points.')

# Load Data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
    "What movie did you like?",
    movies['title'].values
)

if st.button('Find Similar Movies'):
    with st.spinner('Analyzing your taste...'):
        names, posters = recommend(selected_movie)

        st.write("---")
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.markdown(f"**{names[i]}**")
                st.image(posters[i], use_container_width=True)

    st.balloons()