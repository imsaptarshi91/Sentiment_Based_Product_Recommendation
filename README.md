Demo URL: https://senti-cart-8426d23d7955.herokuapp.com/

Problem Statement:

The e-commerce sector has gained immense popularity in contemporary times. The traditional method of manually receiving orders from each customer has been replaced by the convenience of online shopping platforms. Companies establish websites where customers can browse and purchase products at their convenience. Prominent examples of such e-commerce giants include Amazon, Flipkart, Myntra, Paytm, and Snapdeal.

Imagine you’re employed as a Machine Learning Engineer at a rapidly growing e-commerce company named Ebuss. Ebuss has successfully captured a substantial market share in various sectors and offers products across diverse categories such as household essentials, books, personal care items, medicines, cosmetics, beauty products, electrical appliances, kitchenware, and healthcare items.

In an era of rapid technological advancements, it is crucial for Ebuss to expand aggressively within the e-commerce industry to compete with established market leaders such as Amazon and Flipkart.

As a senior ML Engineer, you have been tasked with developing a model that enhances the recommendations provided to users based on their historical reviews and ratings.

To address this challenge, you have devised a plan to build a sentiment-driven product recommendation system, encompassing the following steps:

Key Tasks:
	1.	Data Sourcing and Sentiment Analysis
	2.	Development of a Recommendation System
	3.	Enhancement of Recommendations Using Sentiment Analysis
	4.	Deployment of an End-to-End Solution with a User Interface

The dataset for this project is inspired by a Kaggle competition, and we’ve created a subset for this use case. Detailed steps for the first task are as follows:

Task 1: Data Preprocessing & Feature Engineering:
	•	Exploratory Data Analysis (EDA)
	•	Data Cleaning
	•	Text Preprocessing (tokenization, stemming, etc.)
	•	Feature Extraction: You can choose from methods such as Bag-of-Words, TF-IDF Vectorization, or Word Embeddings.

Task 2: Model Training:

Develop at least three machine learning models and evaluate their performance. Choose the best performing model for sentiment classification. Possible models include:
	•	Logistic Regression
	•	AdaBoostClassifier
	•	GradientBoostingClassifier
	•	Decision Tree
	•	Random Forest

Handle class imbalance issues if necessary and perform hyperparameter tuning to optimize model performance.

Task 3: Building a Recommendation System:

You’ll implement and evaluate two types of recommendation systems:
	•	User-Based Recommendation System
	•	Item-Based Recommendation System

After analysis, select the most appropriate recommendation system for this scenario.

Task 4: Enhancing Recommendations with Sentiment Analysis:

Link the sentiment analysis model to the recommendation system. Once you generate recommendations for a user based on the recommendation engine, filter out the top 5 products based on sentiment analysis of the product reviews. This step integrates the sentiment model with the recommendation engine to deliver more tailored and accurate suggestions.

Task 5: Deployment:

After building the sentiment analysis and recommendation system models, the next step is to deploy the entire end-to-end solution. You’ll use Flask to create a web application for model deployment, which will allow users to interact with the system via a user interface. Deployment will be hosted on Heroku, a Platform-as-a-Service (PaaS) for seamless cloud-based app hosting.

User Interface Features:
	•	Allow users to input a username.
	•	Provide a Submit button that, when pressed, will trigger the recommendation of 5 products based on the submitted username.
	•	Note: This project will only work with users and products that have existing reviews or ratings in the dataset.

Assumption: The number of users and products is fixed, and no new users or products will be considered for model training or prediction.

Deliverables for Evaluation:
	1.	Jupyter Notebook: An end-to-end notebook containing the entire workflow, including data cleaning, preprocessing, feature extraction, machine learning models, recommendation system implementation, and evaluations.
	2.	Deployment Files:
	•	model.py: Contains the final ML model and recommendation system used in the project, along with code for deployment via Flask and Heroku.
	•	index.html: The HTML file for the user interface.
	•	app.py: The Flask application that connects the machine learning backend to the frontend interface.
	•	Pickle Files: The serialized models (saved using pickle) that were trained for sentiment analysis and recommendations.

This project aims to provide a comprehensive solution to building and deploying a sentiment-based product recommendation system with a user-friendly interface, leveraging machine learning to enhance the e-commerce experience.