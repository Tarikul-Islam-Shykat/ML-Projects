import streamlit as st
import pickle
import pandas as pd
import requests # this is for api heat

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=__&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster




movie_dictionary = pickle.load(open('movies_model.pkl','rb'))
movies = pd.DataFrame(movie_dictionary)

similarity = pickle.load(open('similarity_model.pkl','rb'))



# title
st.title('Movie Recommendation System')

# selecte box
options = st.selectbox(
    'How Would you like to select the recommendations ?',
    (movies['title'].values) # we get all the 5000 movies here
)

# button
if st.button('Recommned'):
    name, posters = recommend(options)

    col1, col2 , col3, col4, col5 = st.columns((5))
    with col1:
        st.text(name[0])
        st.image(posters[0])

    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])
