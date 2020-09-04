---
title: Preparation Reading 03: Visualizing Feature Relationships
---

## Overview

In this reading we'll review some of the most common ways to visualize relationships between features in dataset.

!!!time "Estimated Reading Time"
	Plan on around 60 to 90 minutes for this preparation reading, which contains a mix of online and textbook reading.

## Introduction

Looking at descriptive statistics can be a great way to understand a particular feature. But often what we're most interested in is the relationships between features. 

There are some quantitative ways to look at those relationships that we'll learn about later in the semester, but often looking at feature relationships visually can help you decide what direction to take on the rest of the analysis.

## Reading

* Read section 3.5.1 (pages 77 - 86) of *Machine Learning and Predictive Data Analytics*
* Seaborn's [Visualizing Statistical Relationships Tutorial](https://seaborn.pydata.org/tutorial/relational.html)
* Seaborn's [Plotting with Categorical Data Tutorial](https://seaborn.pydata.org/tutorial/categorical.html)
* Seaborn's [Pairwise Relationships Tutorial](https://seaborn.pydata.org/tutorial/distributions.html#visualizing-pairwise-relationships-in-a-dataset)

You may have read parts of some of the Seaborn tutorials for previous assignments. If so, be sure to read through the rest just to have a good idea of what your options are.

!!!warning "Plot Function Return Types"

	Most of Seaborn's plot functions return a [matplotlib axes object](https://matplotlib.org/3.3.1/api/axes_api.html), which you can further customize using the techniques shown in the teacher's solution of [Data Exploration 02](./exploration-02.html).

	However, some of the wrapper functions like [catplot()](https://seaborn.pydata.org/generated/seaborn.catplot.html#seaborn.catplot) return a Seaborn [Facet Grid object](https://seaborn.pydata.org/generated/seaborn.FacetGrid.html#seaborn.FacetGrid), which has different functions for modifying the final output.

