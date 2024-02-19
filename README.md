# ReviewFlix: Social-Media Powered Movie Recommender with Sentiment and Emotion Analysis

Introduction

The Movie Recommendation System is an innovative project that aims to enhance traditional movie recommendations by incorporating sentiment and emotion analysis. The system utilizes data from IMDb and Rotten Tomatoes to provide personalized movie suggestions based on users' emotional states and sentiments towards films.

Key Features

Sentiment Analysis: The system uses advanced sentiment analysis techniques, including the BERT transformer model, to classify movie reviews and tweets as positive and negative sentiments.

Emotion Detection: Emotion analysis is performed using Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN) to detect emotions like Fabulous, Satisfy, disappointed, etc.in movie-related text.

Recommendation Engine: The recommendation engine generates personalized movie suggestions by combining sentiment, emotion, and rating scores from IMDb and Rotten Tomatoes.

User-Friendly Website: The system features a user-friendly website interface that allows users to input preferences, view personalized recommendations, and explore movie details, ratings, and reviews.


Prerequisites: Python (>=3.6)

Getting Started

Data Collection:
* Use the provided data collection script "dataset_creation.py" to gather movie-related data from IMDb and Rotten Tomatoes through web scraping.
* Our final dataset is “dataset.csv”
Sentiment and Emotion Analysis:
* Execute the sentiment analysis files "EDA_Bert_Analysis_RT.py" and "EDA_Bert_Analysis_imdb.py" to perform data preprocessing, analysis, and sentiment analysis using BERT for movie reviews.
* The analysis and outputs can be found in the "EDA_Bert_Analysis_RT.ipynb" notebook.
* Sentiment analysis execution time may vary based on RAM size, taking approximately 6 -7 hours for IMDb data and 3 - 4 hours for Rotten Tomatoes data.
* After sentiment analysis, two additional columns "sentiment_imdb" and "sentiment_rt" will be added for each review, classifying sentiments as positive or negative.
* Refer to the dataset in the "sentiment analysis" folder for the sentiment analysis results which is “data.csv”.
* For emotion analysis, execute the "EmotionAnalysis.py" script to classify emotions (e.g., Fabulous, Satisfy, Disappointed) in movie reviews individually.
* After emotion analysis, two additional columns "Emotion_imdb" and "Emotion_RT" will be added for each review, indicating the detected emotions.
* Refer to the dataset in the "Emotion analysis" folder for the emotion analysis results which is “final_data.csv”.
* The analysis and outputs can be found in the "EmotionAnalysis.ipynb" notebook.
Recommendation Engine
* Run score_compute.py to compute scores for movies and save them in a new CSV file.
* Start the Flask application by running app.py.
* Open your web browser and visit http://localhost:5004/ to start using the movie recommendation system. 
* Start using the movie recommendation system.
