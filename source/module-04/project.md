---
title: Module 04 — Bike Rentals, Project
---

## Overview

After a few more meetings, your team has been assigned to address the following issues asked by the stakeholders:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>So, there's not a lot to discuss at this point. We need a neural network that can predict the number of bikes we can expect to rent on a given day. I'll leave it up to you to decide which factors matter there.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern</h5>
	<blockquote><p>Given how many variables there are in building neural networks, and how long it takes to train and test them, we probably need everyone on the team working on building and testing neural networks.</p><p>I'd suggest that you coordinate how to tackle that in a smart way.</blockquote>
</div>


<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>Oh one more thing, while you've been working with data up through October for your analysis, we just received November and December's as well, and I'd like to see how your model does with it.</p>
	<p>Could you give me the total number of bikes you'd expect for each day in this dataset? I'm not concerned with whether they are registered or casual at this point, just the total number for each hour of each day found here: <a href="https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/bikes_december.csv" download>bikes_december.csv</a>.</p>
	<p>Please make sure to submit both a .csv with these predictions and your executive summary.</p>
	</blockquote>
</div>


## More Tips from Johnny

!!!warning "keras vs tf.keras"
	As [mentioned in the reading](./keras.html), Keras used to be a standalone library, but as of September 2019, it is part of Google's TensorFlow library.

	Keep that in mind if you're looking at any tutorial that was written prior to that date. Most of the API and functions will be the same, but your import statements will likely be different. 

	For more information, [see this article on the change](https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/).

!!!note "Data Dictionary"
	Use this [data dictionary](./bikes-dictionary.txt) to help explain the values and sources of different columns in the dataset.

!!!note "Feature Scaling"
	If you're going to be comparing different numeric features, be sure they are using the same scale. You may find it useful to use min-max scaling to handle this problem. You could do this calculation manually, or use [Sci-Kit Learn's MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

!!!note "Keras & Sci-Kit Learn"
	Just because you're using keras and tensor flow to build the actual neural network, that doesn't mean you can't take advantage of some of the preprocessing and analysis modules in sci-kit learn. 

	Keras also provides [two wrappers](https://www.tensorflow.org/api_docs/python/tf/keras/wrappers/scikit_learn) that allow you to use sklearn pipeline style code with keras neural networks.

	For more information, see:
	
	* [How to insert Keras model into scikit-learn pipeline?](https://stackoverflow.com/questions/42415076/how-to-insert-keras-model-into-scikit-learn-pipeline)

	* [How to Grid Search Hyperparameters for Deep Learning Models in Python With Keras](https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/)

!!!note "Training Checkpoints"
	Neural networks can sometimes take a long time to train (especially once we move into using image data in future modules). If you find you can't let the model train for as long as is needed in a single run, you might want to look into [training checkpoints](https://www.tensorflow.org/guide/checkpoint).

	This [tutorial](https://machinelearningmastery.com/check-point-deep-learning-models-keras/) may be easier to follow, but remember to update the import statements as needed.

!!!note "Grid Search"
	There are a lot of hyperparameters to test out. You may want to use either a grid search or a random grid search. Here is an example in Google Colab. 

	[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_nn_grid_search.ipynb)

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, catches you after work:</h5>
	<blockquote><p>Hey, I know you're probably busy, I was going to put together some hints and sample code for you like I usually do, but the best example code I can provide is what you see in those <a href="./keras.html">keras tutorials from the reading assignment</a>. So, be sure to read over those.</p></blockquote>
</div>


[^1]: [CEO photo by Sung Wang on Unsplash](https://unsplash.com/photos/g4DgCF90EM4)

[^2]: [Investment Banker photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)