Movie Recommendation System

Problem Statement : 
Building a movie recommendation system is a popular project in the field of data science and machine learning. It involves leveraging user data and movie information to create personalized movie recommendations for users. Here's a step-by-step breakdown of the project, from requirements to conclusion.

How to get the API key?
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

How to run the project?
Clone or download this repository to your local machine.
Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
Replace YOUR_API_KEY in both the places (line no. 15 and 29) of static/recommend.js file and hit save.
Open your terminal/command prompt from your project directory and run the file app.py by executing the command python app.py.
Go to your browser and type http://192.168.1.15:8501 in the address bar.

Similarity Score :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

Requirements Gathering:
Understand the project's scope and goals. Identify the data sources: You will need movie metadata (titles, genres, release dates, etc.) and user interaction data (ratings, views, etc.). Choose the programming language and libraries (e.g., Python, pandas, scikit-learn, TensorFlow, PyTorch). Decide the type of recommendation system to build (collaborative filtering, content-based, hybrid, matrix factorization, etc.).

Data Collection and Preprocessing:
Collect movie data from sources like IMDb, TMDb, or Kaggle datasets. Obtain user interaction data, which can be obtained through surveys, user logs, or mock data generation. Clean and preprocess the data, handling missing values, outliers, and inconsistencies.

Exploratory Data Analysis (EDA):
Perform statistical analysis on the data to understand its characteristics. Visualize the data distribution, movie genres, user ratings, etc. Gain insights into popular genres, highly-rated movies, user preferences, etc.

Feature Engineering:
Extract relevant features from the data that will be used to create recommendations. For content-based systems, features might include movie genres, actors, directors, and more. For collaborative filtering, features might include user interactions and ratings.

Building the Recommendation System:
Implement the chosen recommendation algorithm(s) based on the selected approach. For collaborative filtering, you might use techniques like user-based or item-based filtering, or matrix factorization. For content-based, use methods like TF-IDF, word embeddings, or deep learning models. For hybrid systems, combine collaborative and content-based approaches.

Model Training and Evaluation:
Split the data into training and testing sets. Train the recommendation model using the training data. Evaluate the model's performance using appropriate metrics like RMSE, precision, recall, F1-score, etc. Tune hyperparameters to optimize the model's performance.

Deployment:
Deploy the trained recommendation system, making it accessible to users. Implement a user interface (web app, mobile app, or command-line interface) for users to interact with the system.

User Testing and Feedback:
Invite users to test the recommendation system and gather feedback. Monitor user interactions and collect more data for continuous improvement.

Conclusion: 
Summarize the achievements of the project. Discuss the strengths and limitations of the recommendation system. Reflect on what you've learned during the project. Consider future enhancements or additional features that could be implemented.
