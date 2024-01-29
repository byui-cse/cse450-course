---
title: Module 03 — More Hints
body-class: index-page
---

!!!warning "Don't Sell Yourself Short"

	Coding and Data Science is hard. Most of what I'm going to put here, you could look up on your own from official docs, tutorials, and Stack Overflow questions. 

	As we proceed throughout the semester, you'll get fewer hints and be expected to look more stuff up on your own.

	If you haven't tried independent research yet, you might want to try that for a few hours, then come back here.


## Using a Function to Transform a Feature

Sometimes you want to do a complex transformation where you create a new feature based on the data in one or more existing features, or where you need to use boolean logic in your transformation. 

One way to accomplish this is with `apply()` plus a function or lambda, as shown in the following colab notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_functions.ipynb)


## Scaling a Feature
Sometimes it is necessary to transform a feature to use a normalized scale.

Min-max scaling (aka range scaling) will make the values span the range 0.0 - 1.0, as shown in the following colab notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_scaling.ipynb)

Standardization, (aka z-score normalization), scales the values so they have a mean of 0 and a standard deviation of 1, as shown in the following colab notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_normalization.ipynb)


## Dealing with Dates
Sometimes we need to calculate the span between two dates using different units. Or, we might need to to do more complex calculations on a date using boolean logic. The following colab notebook shows some examples of that:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_dates.ipynb)


## One-Hot-Encoding Problems
Oftentimes when using categorical data that has been one-hot encoded, you'll run into problems with a holdout or test dataset that doesn't have the same categorical data (normally missing values). This colab notebook shows how to align your X_train features and your X_test or holdout features:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_one_hot_encode_align.ipynb)


## Using XGBoost
If you've read through the official documentation and tutorials about XGBoost on the [project page](./project.html) and still aren't sure how to use it, this colab notebook might help:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/hint_xgboost.ipynb)

## Choosing the Right Metric

Figuring out which metric to use can be tough. Here is a [quick introduction to different metrics](https://towardsdatascience.com/metrics-to-understand-regression-models-in-plain-english-part-1-c902b2f4156f) you may want to try. 

