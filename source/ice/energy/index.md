---
title: Module ICE: In-Class Exercise
body-class: index-page
---

## Module ICE - Energy Useage

This activity will be completed individually. This will give you a chance to use the skills you've gained throughout the semester. You have the class period to complete this challenge.

## Task

You will be **predicting the Applicances** column which represents the average amount of Watts being used during that time frame. Make sure you keep the predictions in order when you submit them.

Save your answers as a csv with a single column and a column heading of "Appliances".

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

* [Energy Data](./data/energy-training.csv)
* [Energy Holdout](./data/energy-holdout.csv)

#### Data Dictionary

* **Year**, year the reading was taken
* **Month**, month the reading was taken
* **Day**, day the reading was taken
* **Hours**, hour of the day in 0-23 hour format that the reading was taken
* **Minutes**, beginning of the 10 minute interval during which the reading was * taken (0-50, where 0 means minute 0 through 9)
* **Time-since-start**, 10 minute increments since the start of the experiment on Jan 11, 2:00 pm.
* **Appliances**, energy use in Wh 
* **lights**, energy use of light fixtures in the house in Wh
* **T1**, Temperature in kitchen area, in Celsius
* **RH_1**, Humidity in kitchen area, in %
* **T2**, Temperature in living room area, in Celsius
* **RH_2**, Humidity in living room area, in %
* **T3**, Temperature in laundry room area
* **RH_3**, Humidity in laundry room area, in %
* **T4**, Temperature in office room, in Celsius
* **RH_4**, Humidity in office room, in %
* **T5**, Temperature in bathroom, in Celsius
* **RH_5**, Humidity in bathroom, in %
* **T6**, Temperature outside the building (north side), in Celsius
* **RH_6**, Humidity outside the building (north side), in %
* **T7**, Temperature in ironing room , in Celsius
* **RH_7**, Humidity in ironing room, in %
* **T8**, Temperature in teenager room 2, in Celsius
* **RH_8**, Humidity in teenager room 2, in %
* **T9**, Temperature in parents room, in Celsius
* **RH_9**, Humidity in parents room, in %
* **To**, Temperature outside (from nearest weather station), in Celsius
* **Pressure** (from nearest weather station), in mm Hg
* **RH_out**, Humidity outside (from nearest weather station), in %
* **Wind speed** (from nearest weather station), in m/s
* **Visibility** (from nearest weather station), in km
* **Tdewpoint** (from nearest weather station), °C
* **rv1**, mystery variable 1
* **rv2**, mystery variable 2