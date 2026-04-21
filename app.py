import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(
    page_title="Anime Recommender",
    layout="wide"
)

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter your anime preferences. E.g.: a light hearted anime in a school setting")

if st.button("Build Database"):
    with st.spinner("Building database..."):
        pipeline.build_database()
        st.write("Successfully built database")

if query:
    with st.spinner("Fetching recommendations for you..."):
        response = pipeline.recommend(query=query)
        st.markdown("### Recommendations")
        st.write(response)