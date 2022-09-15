---
title: Module 02: Overview
body-class: index-page
---

## Module 02 - Overview

This week you'll learn about supervised learning, decision trees, and more about model evaluation.

!!! warning "Subject to Change"
	
	Keep in mind that your instructor may deviate somewhat from the following guide, and they have final say on assignment requirements, delivery methods, and due dates. So be sure to pay attention to both in-class and Canvas announcements.

## Module 02 Assignments

For your convenience, here are links to the module 02 readings and assignments:

#### Readings

* [Preparation Reading](./reading.html)
* [Case Study Intro](./intro.html)
* [In-class Case Study Discussion](./discussion.html)
* [Case Study Project](./project.html)

#### Data

* [Bank Dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank.csv)
* [Bank Data Dictionary](./bank-dictionary.txt)
* [Bank Holdout Dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank_holdout_test.csv)
* [Bank Holdout MINI Dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank_holdout_test_mini.csv)
* [Sample CSV predictions](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bank_csv_answers_sample.csv)
* [Google Colab Notebook](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_bank.ipynb)

## Use a decision tree

If you're really struggling with how to make a decision tree, you should try reading through the documentation a couple more times.

If that still doesn't help, this notebook can give you some more guidance:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_decisiontrees.ipynb)

!!!note "Holdout Dataset"
	Most of the modules contain a "holdout dataset" which is used by the instructor to see how well your model performs. This dataset has the same fields as the training set except we have removed the value you will be predicting. Your model will not have seen this information before, and the results will indicate how well the model has "learned" during training. 

	Once your team is confident your model has been adequately trained, load the data from the holdout dataset and make predictions on it. You are required to make predictions for ALL rows in the holdout dataset. 

	*Don't Forget:*
		
	*	Perform the same transformations on the dataset. (MinMaxScaling, add/remove features, etc.)
	*	Do NOT remove any rows from the holdout dataset
	*	Do NOT sort or shuffle the holdout dataset

!!! def "Holdout Mini Dataset"
	This module has a mini holdout dataset. You can test your model against this mini holdout dataset as many times as you'd like. It is here to

	*	Verify that your CSV is in the correct format
	*	Verify that your model is making good predictions
	*	Give you an idea of what your grade might be on the final holdout set 

	Once your team is confident your model has been adequately trained, load the data from the mini holdout dataset and make predictions on it. Save the predictions as a CSV.

	[Open and run this colab](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/module02_bank_grading_mini.ipynb) (follow the instructions at the top of the notebook)

	*Don't Forget:*
		
	*	Perform the same transformations on the dataset. (MinMaxScaling, add/remove features, etc.)
	*	Do NOT remove any rows from the holdout dataset
	*	Do NOT sort or shuffle the holdout dataset
	*	You can test the mini holdout as many times as you'd like, but be careful not to overfit to the mini holdout set. Ideally, you should get similar results to the test dataset you created.

#### Templates

* [Team Executive Summary Template]({{URLROOT}}/course/executive-summary.docx)
* [Individual Reflection Template]({{URLROOT}}/course/reflection.docx)

#### Hints and Helps

* [Hints](./hints.html)