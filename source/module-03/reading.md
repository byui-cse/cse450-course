---
title: Module 03 — Gradient Boosted Trees
body-class: index-page
---

![Stacked Rocks]({{URLROOT}}/shared/img/stackedrocks.jpg)
*[Photo by Samrat Khadka on Unsplash](https://unsplash.com/photos/yFOjHnFu8jI)*

## Overview

!!!time "Estimated Reading Time"
	Plan on around 90 - 120 minutes for this preparation reading, which consists of a mix of textbook and online reading. 

The objective of this module is to provide a real-world scenario in which you can practice the following data science / machine learning skills:

* Gradient Boosted Trees and the XGBoost Library
* Evaluating how well a model carries out regression

## Preparation Reading

### Model Ensembles

First, read this section from your textbook:

* Read Section 8.4.5 of your text (Performance Measures: Continuous Targets)
* Read section 4.4.5 of your text (Model Ensembles)

### Gradient Boosted Trees

Four videos are listed below.

The first video explains the concepts of gradient boosted trees within the context of regression tasks. The second explains the mathematics behind those concepts. 

The third video explains the concepts of gradient boosted trees within the context of classification tasks. The fourth explains the mathematics behind those concepts. 

It's not essential that you master the mathematics, though you should try your best to follow along as they do a really good job of explaining what some of the stickier bits of notation represent.

(Don't let the corny music at the start dissuade you, they're really good videos)

<iframe width="560" height="315" src="https://www.youtube.com/embed/3CC4N4z3GJc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/2xudPOBz-vs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/jxuNLH5dXCs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Optional Video ####

The following video completes the series. It's very good and does an excellent job walking through the derivation of the math used in the classification example, but it is deeper than what is required for this course.

You might consider watching it with the intent to understand the approach at a high level rather than worrying about the details of every expression.

<iframe width="560" height="315" src="https://www.youtube.com/embed/StWY5QWMXCw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

!!!note "XGBoost"
	You can find documentation on how to use xgboost to be useful, particularly the sections on the sklearn wrapper:

	* [User Guide for XGBoost](https://xgboost.readthedocs.io/en/latest/)
	* [API Reference for the SKLearn Wrapper](https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=sklearn#module-xgboost.sklearn)
	* [An XGBoost tutorial that uses the sklearn wrapper](https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/)
	* [A more in-depth tutorial on xgboost](https://www.kaggle.com/stuarthallows/using-xgboost-with-scikit-learn)
	* [An XGBoost tutorial that does not use the sklearn wrapper](https://medium.com/low-code-for-advanced-data-science/xgboost-explained-a-beginners-guide-095464ad418f)

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, drops by your hotel room around midnight:</h5>
	<blockquote><p>Okay, just one last thing, if you need any more help at all, I put together <a href='./hints.html'>this collection of Google Colab notebooks</a> that might be useful.</p></blockquote>
</div>

[^1]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)