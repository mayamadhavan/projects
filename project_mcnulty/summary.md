# Overall Process
1. Data Cleaning pt.1
	+ Feature Selection 1
	+ Fill NA’s
	+ Feature Selection 2
	+ Dummify Variables

2. Data Cleaning pt. 2
	+ Undersample
	+ Aply Standard Scalar

3. Modeling
	+ Compare ROC Curves
	+ Compare Confusion Matrices
	+ Run Final Model

4. Make Predictions
=======

# Data Pt 1
I used 3 datasets, 1 from Kaggle (my main dataset, with application info and outcomes) and 2 scraped from the web.

Data Cleaning was a huge and time consuming part of my project.

There were originally ~150 categorical features in my dataset.

If I'd had time, I would have cleaned the train set and then applied that same cleaning to the test set. I didn't do that in this case though.

The first step in cleaning the data was combining repeated columns.

Then I filled gaps using either mode or mean values of each column when group by related other columns.

I also feature engineered a new column, job type, which had ~14 different job categories. I made the divisions using value counts. 

Finally, I took the other two datasets and used one to fix some repeated values in a column, and the other to transform city of origin to a population metric.


# Data Pt 2
I scaled my data with the standard scalar.

I also under sampled to make up for imbalances because there were way more people certified than denied.

# Models
I ran multiple models and compared using both ROC and precision/recall. I decided to be agnostic and go with area under the curve for my final decision making.

The models I ran were: 
Random Forest, A Decision Tree, Logistic Regression, SGD-Log, Naive-Bayes Gaussian, Naive-Bayes Bernoulli, and Naive-Bayes Multinomial

I also checked with Random Forest which features were most important, but I didn't update my model to reflect that because it wasn't relevant to my end goals.

Random Forest and Logistic Regression had close scores, so I ran both on my full train and test set. Random Forest did slightly better, so I went with that.

# Application
After running the model I made a prediction function and threw that into a Bootstrapped Flask App where users could either select values from a dropdown or input them. If a value they inputed for city wasn't in my dataset, the city was automatically assigned a population.