---
title: Module ICE: In-Class Exercise
body-class: index-page
---

## Module ICE - Wine

This activity will be completed individually. This will give you a chance to use the skills you've gained throughout the semester. You have the class period to complete this challenge.

## Task

You will be predicting the classification of a wine (0, 1, or 2). Make sure you keep the predictions in order when you submit them.

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

Here are the datasets for this challenge. These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines. 

* [Wine Data](./data/wine-training.csv)
* [Wine Holdout](./data/wine-holdout.csv)

#### Data Dictionary

Attribute Information:

* **Alcohol**: The percentage of alcohol content in the wine, usually expressed as a volume percentage
* **Malic acid**: A type of acid found in grapes, which contributes to the tartness or sourness of the wine. It's often associated with green apple flavors.
* **Ash**: The inorganic residue left after the organic material in wine has been burned off. It consists mainly of minerals.
* **Alcalinity of ash**: A measure of the basicity (alkalinity) of the ash left after combustion, which can be an indicator of soil composition and grape growing conditions.
* **Magnesium**: A mineral found in wine that can affect its taste and mouthfeel, though typically present in relatively low concentrations.
* **Total phenols**: A measure of the total phenolic compounds present in wine, including various antioxidants, tannins, and flavonoids. These compounds contribute to the wine's color, flavor, and mouthfeel.
* **Flavanoids**: A subgroup of phenolic compounds found in wine, which contribute to its flavor and mouthfeel. They are responsible for some of the wine's bitterness, astringency, and antioxidant properties.
* **Nonflavanoid phenols**: Another subgroup of phenolic compounds found in wine, which include compounds such as stilbenes and hydroxycinnamic acids. They also contribute to the wine's sensory characteristics.
* **Proanthocyanins**: A type of flavonoid compound found in wine, which contributes to its color, bitterness, and astringency. They are also antioxidants.
* **Color intensity**: The depth or darkness of the color of the wine, which can be affected by various factors including grape variety, winemaking techniques, and aging.
* **Hue**: The shade or tint of the color of the wine.
* **OD280/OD315 of diluted wines**: This refers to the optical density of a wine sample measured at two specific wavelengths, 280 nm and 315 nm, typically used to assess protein content and color stability in wine.
* **Proline**: An amino acid found in grapes and wine, which can affect the taste, mouthfeel, and aging potential of the wine. It is often associated with certain flavors and aromas, such as nuttiness and bitterness.
* **Wine**: Wine classification to predict