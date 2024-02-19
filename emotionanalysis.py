# -*- coding: utf-8 -*-
"""EmotionAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mRJLalAD0Hyi4ExqIDcpu3Q2GNm89oPs
"""

import pandas as pd

# Load the CSV file
data = pd.read_csv('data.csv')

pip install vaderSentiment

pip install keras

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Here, 'User reviews' is the column containing user reviews from imdb website in dataset
reviews = data['User Reviews']

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define threshold values for each emotion
thresholds = {
    'Fabulous': 0.3,
    'disappointed': -0.3,
    'anger': -0.3,
    'surprise': 0.1,
    'fear': -0.1,
    'disgust': -0.1
}

# Function to classify emotions based on sentiment scores
def classify_emotion(sentiment_score):
    for emotion, threshold in thresholds.items():
        if sentiment_score >= threshold:
            return emotion
    return 'Satisfy'  # If sentiment score does not fall into any threshold, consider it as 'Satisfy'

# List to store the predicted emotions for each review
predicted_emotions = []

# Perform sentiment analysis on each review and classify emotions
for review in reviews:
    sentiment_score = analyzer.polarity_scores(review)['compound']
    emotion = classify_emotion(sentiment_score)
    predicted_emotions.append(emotion)

# Add the predicted emotions to the DataFrame
data['Emotion_imdb'] = predicted_emotions

# Display the DataFrame with the predicted emotions
print(data)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Here, 'RT_review' is the column containing user reviews from rotten tomatoes in dataset
reviews = data['RT_review']

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define threshold values for each emotion
thresholds = {
    'Fabulous': 0.3,
    'disappointed': -0.3,
    'anger': -0.3,
    'surprise': 0.1,
    'fear': -0.1,
    'disgust': -0.1
}

# Function to classify emotions based on sentiment scores
def classify_emotion(sentiment_score):
    for emotion, threshold in thresholds.items():
        if sentiment_score >= threshold:
            return emotion
    return 'Satisfy'  # If sentiment score does not fall into any threshold, consider it as 'Satisfy'

# List to store the predicted emotions for each review
predicted_emotions = []

# Perform sentiment analysis on each review and classify emotions
for review in reviews:
    sentiment_score = analyzer.polarity_scores(review)['compound']
    emotion = classify_emotion(sentiment_score)
    predicted_emotions.append(emotion)

# Add the predicted emotions to the DataFrame
data['Emotion_RT'] = predicted_emotions

# Display the DataFrame with the predicted emotions
print(data)

data

#Drop Columns which is irrelevant
data.drop(columns='Unnamed: 0', inplace=True)
data.drop(columns='Name', inplace=True)
data.drop(columns='Unnamed: 0.1', inplace=True)

data

import seaborn as sns
import matplotlib.pyplot as plt

# Let's convert the 'Emotion_imdb' column to categorical data
data['Emotion_imdb'] = data['Emotion_imdb'].astype('category')

# Now we can do countplot
sns.set(style="darkgrid", font_scale=1.2)
sns.countplot(x='Emotion_imdb', data=data)
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Distribution of Emotions on IMDB data')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Let's convert the 'Emotion_RT' column to categorical data
data['Emotion_RT'] = data['Emotion_RT'].astype('category')

# Now we can do countplot
sns.set(style="darkgrid", font_scale=1.2)
sns.countplot(x='Emotion_RT', data=data)
plt.xlabel('Emotion')
plt.ylabel('Count')
plt.title('Distribution of Emotions on RT data')
plt.show()

#Converting into integers value for comparing and ranking.
data.sentiment_imdb.replace("Positive" , 10 , inplace = True)
data.sentiment_imdb.replace("Negative" , -10 , inplace = True)

data.sentiment_rt.replace("Positive" , 10 , inplace = True)
data.sentiment_rt.replace("Negative" , -10 , inplace = True)

data.Emotion_imdb.replace("Fabulous" , 10 , inplace = True)
data.Emotion_imdb.replace("disappointed" , -10 , inplace = True)
data.Emotion_imdb.replace("anger" , -8 , inplace = True)
data.Emotion_imdb.replace("surprise" , 7 , inplace = True)
data.Emotion_imdb.replace("fear" , -6 , inplace = True)
data.Emotion_imdb.replace("disgust" , -7 , inplace = True)
data.Emotion_imdb.replace("Satisfy" , 5 , inplace = True)

data.Emotion_RT.replace("Fabulous" , 10 , inplace = True)
data.Emotion_RT.replace("disappointed" , -10 , inplace = True)
data.Emotion_RT.replace("anger" , -8 , inplace = True)
data.Emotion_RT.replace("surprise" , 7 , inplace = True)
data.Emotion_RT.replace("fear" , -6 , inplace = True)
data.Emotion_RT.replace("disgust" , -7 , inplace = True)
data.Emotion_RT.replace("Satisfy" , 5 , inplace = True)
data.head(20)

data.head(20)

#storing data into csv file, this will be the data which we will be using for recommendation system.
data.to_csv('dataset_website.csv')

#RNN model on Imdb data
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

texts = data['sentiment_imdb'].astype(str).tolist()
labels = data['Emotion_imdb'].values

# Create a mapping from emotion labels to integers
label_to_int = {label: i for i, label in enumerate(set(labels))}

# Convert string labels to integers
labels = [label_to_int[label] for label in labels]

# Tokenize and create word index
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Convert text to sequences of integers
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to a fixed length
max_sequence_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Convert labels to categorical format
num_classes = len(set(labels))
labels_categorical = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels_categorical, test_size=0.2, random_state=42)

# Build the RNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_sequence_length))
model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print model summary
print(model.summary())

# Train the model
batch_size = 32
epochs = 10
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}, Test accuracy: {accuracy}")

pip install tabulate

from tabulate import tabulate
# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert predicted probabilities to class labels (0, 1, 2, etc.)
y_pred_labels = np.argmax(y_pred, axis=1)

# Convert one-hot encoded test labels back to integer labels
y_test_labels = np.argmax(y_test, axis=1)

# Calculate evaluation metrics
recall = recall_score(y_test_labels, y_pred_labels, average='macro')
precision = precision_score(y_test_labels, y_pred_labels, average='macro')
f1 = f1_score(y_test_labels, y_pred_labels, average='macro')
accuracy = accuracy_score(y_test_labels, y_pred_labels)

# Create the table with square boxes
table = [["Metric", "Value"],
         ["Recall", f"□ {recall:.4f}"],
         ["Precision", f"□ {precision:.4f}"],
         ["F1-score", f"□ {f1:.4f}"],
         ["Accuracy", f"□ {accuracy:.4f}"]]

# Print the table
print(tabulate(table, headers="firstrow", tablefmt="grid"))

#CNN model on Imdb data

texts = data['sentiment_imdb'].astype(str).tolist()
labels = data['Emotion_imdb'].values


# Create a mapping from emotion labels to integers
label_to_int = {label: i for i, label in enumerate(set(labels))}

# Convert string labels to integers
labels = [label_to_int[label] for label in labels]

# Tokenize and create word index
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Convert text to sequences of integers
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to a fixed length
max_sequence_length = 100  # Set a reasonable sequence length based on your data
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Convert labels to categorical format
num_classes = len(set(labels))
labels_categorical = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels_categorical, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_sequence_length))
model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print model summary
print(model.summary())

# Train the model
batch_size = 32
epochs = 10
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}, Test accuracy: {accuracy}")

# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert predicted probabilities to class labels (0, 1, 2, etc.)
y_pred_labels = np.argmax(y_pred, axis=1)

# Convert one-hot encoded test labels back to integer labels
y_test_labels = np.argmax(y_test, axis=1)

# Calculate evaluation metrics
recall = recall_score(y_test_labels, y_pred_labels, average='macro')
precision = precision_score(y_test_labels, y_pred_labels, average='macro')
f1 = f1_score(y_test_labels, y_pred_labels, average='macro')
accuracy = accuracy_score(y_test_labels, y_pred_labels)

# Create the table with square boxes
table = [["Metric", "Value"],
         ["Recall", f"□ {recall:.4f}"],
         ["Precision", f"□ {precision:.4f}"],
         ["F1-score", f"□ {f1:.4f}"],
         ["Accuracy", f"□ {accuracy:.4f}"]]

# Print the table
print(tabulate(table, headers="firstrow", tablefmt="grid"))

#RNN model on RT data

texts = data['sentiment_rt'].astype(str).tolist()
labels = data['Emotion_RT'].values

# Create a mapping from emotion labels to integers
label_to_int = {label: i for i, label in enumerate(set(labels))}

# Convert string labels to integers
labels = [label_to_int[label] for label in labels]

# Tokenize and create word index
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Convert text to sequences of integers
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to a fixed length
max_sequence_length = max(len(seq) for seq in sequences)
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Convert labels to categorical format
num_classes = len(set(labels))
labels_categorical = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels_categorical, test_size=0.2, random_state=42)

# Build the RNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_sequence_length))
model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print model summary
print(model.summary())

# Train the model
batch_size = 32
epochs = 10
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}, Test accuracy: {accuracy}")

from tabulate import tabulate
# Make predictions on the test data

y_pred = model.predict(X_test)

# Convert predicted probabilities to class labels (0, 1, 2, etc.)
y_pred_labels = np.argmax(y_pred, axis=1)

# Convert one-hot encoded test labels back to integer labels
y_test_labels = np.argmax(y_test, axis=1)

# Assuming you have already defined y_test_labels and y_pred_labels
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

# Calculate evaluation metrics
accuracy = accuracy_score(y_test_labels, y_pred_labels)
recall = recall_score(y_test_labels, y_pred_labels, average='macro')
precision = precision_score(y_test_labels, y_pred_labels, average='macro')
f1 = f1_score(y_test_labels, y_pred_labels, average='macro')

# Create the table with square boxes
table = [["Metric", "Value"],
         ["Recall", f"□ {recall:.4f}"],
         ["Precision", f"□ {precision:.4f}"],
         ["F1-score", f"□ {f1:.4f}"],
         ["Accuracy", f"□ {accuracy:.4f}"]]


# Print the table
print(tabulate(table, headers="firstrow", tablefmt="grid"))

#CNN model on RT data
texts = data['sentiment_rt'].astype(str).tolist()
labels = data['Emotion_RT'].values


# Create a mapping from emotion labels to integers
label_to_int = {label: i for i, label in enumerate(set(labels))}

# Convert string labels to integers
labels = [label_to_int[label] for label in labels]

# Tokenize and create word index
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

# Convert text to sequences of integers
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences to a fixed length
max_sequence_length = 100  # Set a reasonable sequence length based on your data
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# Convert labels to categorical format
num_classes = len(set(labels))
labels_categorical = tf.keras.utils.to_categorical(labels, num_classes=num_classes)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(padded_sequences, labels_categorical, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_sequence_length))
model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Print model summary
print(model.summary())

# Train the model
batch_size = 32
epochs = 10
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}, Test accuracy: {accuracy}")

# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert predicted probabilities to class labels (0, 1, 2, etc.)
y_pred_labels = np.argmax(y_pred, axis=1)

# Convert one-hot encoded test labels back to integer labels
y_test_labels = np.argmax(y_test, axis=1)

# Calculate evaluation metrics
recall = recall_score(y_test_labels, y_pred_labels, average='macro')
precision = precision_score(y_test_labels, y_pred_labels, average='macro')
f1 = f1_score(y_test_labels, y_pred_labels, average='macro')
accuracy = accuracy_score(y_test_labels, y_pred_labels)

# Create the table with square boxes
table = [["Metric", "Value"],
         ["Recall", f"□ {recall:.4f}"],
         ["Precision", f"□ {precision:.4f}"],
         ["F1-score", f"□ {f1:.4f}"],
         ["Accuracy", f"□ {accuracy:.4f}"]]

# Print the table
print(tabulate(table, headers="firstrow", tablefmt="grid"))