---
title: Preparation Reading 01: Introduction
---

![Credit Card Transaction]({{URLROOT}}/shared/img/cc.jpg)
*[Photo by Blake Wisz on Unsplash](https://unsplash.com/photos/q3o_8MteFM0)*

## Overview

!!!time "Estimated Reading Time"
	Plan on around 90 - 120 minutes for this preparation reading.

Broadly speaking, there are three main types of machine learning: reinforcement learning, unsupervised learning, and supervised learning.

In this course, we'll focus on supervised learning, but we'll present a quick overview of the other two branches:

### Reinforcement Learning
Reinforcement learning is what most people think of when they think of artificial intelligence. 

Reinforcement learning is used in robotics development to train robots to respond to varying environmental factors in order to achieve a goal. 

!!! def "Reinforcement Learning"
	Reinforcement learning is an iterative process where an algorithm seeks to maximize some value based on rewards received for being right.


### Unsupervised Learning

A grocery store chain might wish to decide which customers to target for a particular sales promotion. Historic shopping data can be analyzed using a technique known as *cluster analysis* to determine which groups of customers would be most likely to respond to a particular ad campaign.

A geneticist tracking how a plant cell responds to drought conditions might take measurements of tens of thousands of proteins every few seconds. With that many features to analyze, it can be difficult to find any kind of useful pattern. 

A technique known as *dimensional reduction* can aggregate the features into groups based on their response patterns, reducing the number of features that need to be analyzed.

Cluster analysis and dimensional reduction are examples of unsupervised learning.

!!! def "Unsupervised Learning"
	Unsupervised learning algorithms generate models that allow us to identify patterns in data, make inferences about those patterns, and predict where future data might fall within those patterns. 


## An Example of Supervised Learning

Credit card companies use supervised learning to develop models that can predict if a transaction looks fraudulent. 

They start with a large set of transactions that they've already analyzed for fraud. This is called the *training data*. Each transaction in this set is referred to as an *instance* or *sample*.

Each sample will  have a set of interesting attributes, such as the time the transaction occurred, the amount, the location of the purchase, etc... 

These attributes are called *predictors*, *independent variables*, or *features*. Data scientists usually refer to them as *features*.

!!! warning "Synonym Madness"
	
	The concepts and techniques used in machine learning have been around for a long time, and have been developed and refined through work in many different fields. 

	Because of this, there are many terms like "predictors" and "features" that came from different fields, but which mean the same thing and are sometimes used interchangeably.

Since these are historic transactions, one of the attributes will be whether or not the transaction really was fraudulent. Since this is the attribute we're trying to predict in future transactions, it is referred to as the *response variable*, or the *target*.

With that background, we can formally define supervised learning as:

!!! def "Supervised Learning"

	Supervised learning algorithms use *labeled* training data, (data that starts with known values for the target variable) to generate models that relate the features to the target. 

	More formally, given:

	* An $n$ x $m$ matrix, of $X$, where $n$ is the number of samples, and $m$ is the number of features
	* A vector of $n$ target values, $y$ 

	A supervised learning algorithm is one that "fits" $X$ to $y$ to create a model capable of predicting the target values of new samples.

The purpose of these models is to accurately predict the response for future observations (prediction) or to help us better understand the relationship between the response and the predictors (inference). 


## Supervised Machine Learning Tasks

Most prediction problems addressed by supervised machine learning can be divided into two groups, regression and classification. These are sometimes referred to as "regression tasks" and "classification tasks".

!!! def "Regression"

	The process of generating a model that can be used to predict a numeric value.

Examples of regression problems include:

* Predicting the likelihood that someone will contract a disease
* Calculating the value of a house
* Predicting a student's most likely GPA based on their ACT scores.

If you're trying to predict a number, that is usually a regression task.

!!! def "Classification"

	The process of generating a model that can be used to predict a particular value from a set of discrete choices.

Examples of classification problems include:

* Facial recognition software
* Fraud detection
* Disease diagnosis 
* Text recognition

If you're trying to predict whether something belongs to a certain class ("picture of dog" vs "picture of cat", "has disease" vs "does not have disease", etc...), that is usually a classification task.

!!! warning "Regression vs Classification"

	While there are some algorithms that are designed to be used in regression or classification scenarios, most can be used in either one. In addition, with a few modifications to the problem statement, many classification problems can be restated as regression problems and vice versa.

	Depending on how the final model is going to be used, one approach might make more sense than another. As you'll soon realize is the case for many aspects of machine learning, the right approach will depend on many factors. And it's unusual for there to be one "best" way.

## Numeric vs Categorical Features

When analyzing a feature of our data, one of the first things we need to know is whether or not we are looking at a numeric or categorical feature.

!!!def "Numeric Feature"
	
	A numeric, or quantitative feature is a property of the data ($x$) that can take on a range of quantitative values between two numeric limits: $ x_{min} \leq x \leq x_{max} $.

If we were to measure the height of everyone on campus, we might find that their heights span a range between 100 cm and 200 cm. We would say that `height` is a numeric feature of our data, with a minimum value of 100 cm and a maximum value of 200 cm.

Other examples of numeric features for this dataset might include the student's weight, age, GPA, number of credits completed, hours of Netflix watched each week, and bank account balance.

If we asked students which academic class they were in (Freshman, Sophomore, Junior, or Senior), we would be measuring a *categorical feature*.

!!!def "Categorical Feature"
	
	A property of the data that can have one or more qualitative values.

Other examples of categorical measurements for this dataset might include the student's favorite flavor of ice cream, their eye color, their relationship status, and whether or not they've completed an internship.

!!!warning "Features in Disguise"

	Beware of categorical features that *look* like numeric features. For example, if students in our survey live in three different apartment complexes, we might ask "Which apartment complex do you live in, 1, 2, or 3?".

	Even though this is technically a numeric value between two limits, it is really a categorical feature because there's no quantitative difference between the apartment complexes. Later on, we'll see how to make sure our machine learning algorithms know that a feature really is a categorical feature, even when it uses numeric values.

	Even more tricky is the case of features that could go either way. In our first categorical feature example, we could have asked "Which academic year are you currently in, 1, 2, 3, or 4?". 

	There might actually be an important relationship in our data that relies on the fact that senior students have been at school 4 times longer than freshman students. In cases like these, we sometimes have to try treating a feature both ways to see which gives us better results.

## The Pandas Library

The pandas library is a python library used for data analysis and manipulation. It will provide the core functionality for most of what you do in the data exploration and preprocessing stages of most machine learning projects.

You'll want to read through the [Getting Started Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) and keep them handy for reference as you work on the Data Exploration materials this week.