---
title: Module 04: Overview
body-class: index-page
---

## Module 04 - Overview

This week you'll learn about basic Neural Networks.

!!! warning "Subject to Change"
	
	Keep in mind that your instructor may deviate somewhat from the following guide, and they have final say on assignment requirements, delivery methods, and due dates. So be sure to pay attention to both in-class and Canvas announcements.

## Module 04 Assignments

For your convenience, here are links to the module 04 readings and assignments:

#### Readings

* [Preparation Reading](./reading.html)
* [Case Study Intro](./intro.html)
* [In-class Case Study Discussion](./discussion.html)
* [Case Study Project](./project.html)

#### Data
* [Bike Data](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bikes.csv)
* [Data Dictionary](./bikes-dictionary.txt)
* [Bike Holdout Dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bikes_december.csv)
* [Bike Holdout MINI Dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/biking_holdout_test_mini.csv)
* [Google Colab Notebook](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_bikes.ipynb)

!!! def "Holdout Mini Dataset"
	This module has a mini holdout dataset. You can test your model against this mini holdout dataset as many times as you'd like. It is here to

	*	Verify that your CSV is in the correct format
	*	Verify that your model is making good predictions
	*	Give you an idea of what your grade might be on the final holdout set 

	Once your team is confident your model has been adequately trained, load the data from the mini holdout dataset and make predictions on it. Save the predictions as a CSV.

	[Open and run this colab](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/module04_biking_grading_mini.ipynb) (follow the instructions at the top of the notebook)

	*Don't Forget:*
		
	*	Perform the same transformations on the dataset. (MinMaxScaling, add/remove features, etc.)
	*	Do NOT remove any rows from the holdout dataset
	*	Do NOT sort or shuffle the holdout dataset
	*	You can test the mini holdout as many times as you'd like, but be careful not to overfit to the mini holdout set. Ideally, you should get similar results to the test dataset you created.

#### Templates

* [Individual Reflection Template]({{URLROOT}}/course/reflection.docx)