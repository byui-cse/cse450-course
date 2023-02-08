---
title: Module ICE: In-Class Exercise
body-class: index-page
---

## Module ICE - Grain Kernels

This activity will be completed individually. This will give you a chance to use the skills you've gained throughout the semester. You have the class period to complete this challenge.

## Task

You will be predicting the class of grain (Osmancik and Cammeo). Make sure you keep the predictions in order when you submit them.

Save your answers as a csv with a single column and a column heading of "Class".


!!! warning "One Hour Challenge"
	
	This activity is to be completed in an hour. You do NOT need to produce an executive summary for this challenge. 
	
You will still be required to do the following:

- **Prepare the data**
	- Cleaning the data to remove unwanted data, missing values, rows, and columns, duplicate values, data type conversion, etc. You might even have to restructure the dataset and change the rows and columns or index of rows and columns.
	- Visualize the data to understand how it is structured and understand the relationship between various variables and classes present.
	- Splitting the cleaned data into at least two sets - a training set and a testing set. You may wish to split the data again to get a validation set as well. The training set is the set your model learns from. A testing set is used to check the accuracy of your model after training.
- **Choose models**
	- You may use any models you'd like. You may use examples from your previous case studies. You can use any class notes or class resources, but you must complete your own work. 
	- You should use multiple models if time permits.
- **Train models**
	- Train the models on your training dataset
- **Evaluate the models**
	- Using the test dataset, evaluate how your model is performing. 
- **Parameter tuning**
	- Tune your model parameters to increase the model's performance.
- **Make predictions**
	- Using the holdout dataset, use your model to make predictions. Make sure you apply any needed transformations to the holdout set. Ensure that you do NOT delete any rows from the holdout set and that they remain in the same order.
- **Upload your predictions**
	- Upload your predictions to the assignment in canvas.
	- Post a comment on your submission with 
		- any insights you gained into the data.
		- a link to your colab notebook.

## Data

Here are the datasets for this challenge.

* [Grain Data](./data/grain-training.csv)
* [Grain Holdout](./data/grain-holdout.csv)

#### Data Dictionary

Attribute Information:

* **Area**: Gives the number of pixels within the boundaries of the grain.
* **Perimeter**: It measures the environment by calculating the distance between the boundaries of the grain and the pixels around it.
* **MajorAxisLength**: Gives the length of the main axis, which is the longest line that can be drawn on the grain.
* **MinorAxisLength**: Gives the length of the small axis, which is the shortest line that can be drawn on the grain.
* **Eccentricity**: It gives a measure of the eccentricity of the ellipse, which has the same moments as grain.
* **ConvexArea**: Gives the number of pixels of the smallest convex shell of the region formed by the grain.
* **Extent**: Gives the ratio of the region formed by the raisin to the total pixels in the bounding box.
* **Class**: Osmancik and Cammeo grain kernels. 