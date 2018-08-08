# Background
Getting a US visa is a long and occasionally confusing process. Applicants can sink a considerable amount of resources into all the appointments and forms they have.

On the other hand, the government has to deal with masses of applications from a diverse range of countries. Take a look at the map below to see a sample of just how many different types of people came into the county between 2012-2016.

# Goals
In order to minimize the amount of effort needed on both sides of the equation, I wanted to try and predict whether or not someone would get their US Visa approved using only features that an applicant would easily know about. This way, they would easily be able to find out whether they would be accepted before they even apply.

# Overall Process
Data Cleaning pt.1
	Feature Selection 1
	Fill NA’s
	Feature Selection 2
	Dummify Variables

Data Cleaning pt. 2
Undersample
Aply Standard Scalar

Modeling
	Compare ROC Curves
	Compare Confusion Matrices
	Run Final Model

Make Predictions

Flask App

# Data


# Models


# Application


# Going Forward



Given this and the aforementioned goals, feature selection and Data Cleaning were a huge part of my project


In my opinion, it would be better for the app to more often tell someone that they would get their visa when they won’t than the reverse. I’d rather not deter someone who would in actuality be accepted.

I suppose that that’s a matter of personal preference, but assuming my viewpoint holds, I would go back and look at the precision score when calculating my model.



Random forests= weighted average for the prediction for each model
