import streamlit as st
import pickle
import requests
import pandas as pd

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w185" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])

    recommended_movie= []
    recommended_movie_poster = []
    for i in movie_list[1:11]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_poster

movies_dict =pickle.load(open("movie_dict.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")
selected_movies =st.selectbox(
    "How would you lie to contacted?",
movies["title"].values)

if st.button("Show Recommendation"):
   recommended_movie, recommended_movie_poster = recommend(selected_movies)

   col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
   with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_poster[0])
   with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_poster[1])

   with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_poster[2])
   with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_poster[3])

   with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_poster[4])

