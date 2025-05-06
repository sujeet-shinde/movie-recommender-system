import streamlit as st
import pickle
import pandas as pd

# Load the data
movies = pickle.load(open('movies.pkl', 'rb'))      # full DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values                # dropdown list

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose a movie to see what matches your taste',
    movies_list)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
