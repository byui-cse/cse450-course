---
title: Preparation Reading 02: Descriptive Statistics
---

## Overview

In this reading we'll review some basic statistics you'll need for machine learning.

!!!time "Estimated Reading Time"
	Plan on around 60 to 90 minutes for this preparation reading, which contains a mix of online and textbook reading.

## Types of features

When analyzing a feature of our data, one of the first things we need to know is whether or not we are looking at a quantitative, categorical, or ordinal feature.

### Example

Imagine we conduct a survey of students and capture the following pieces of data:

* Their height in cm
* Their eye color
* Their year

Height would be a _quantitative_ feature, because it is a measured numeric value. It might be 178cm, 188.5cm, or anywhere in between.

!!!def "Quantitative Feature"
	
	A property of the data with a measured numeric value.


Eye color would be a _categorical_ feature, because it is a value that comes from a finite set of options. It might be "blue", "brown", "hazel", etc...

!!!def "Categorical Feature"

	A property of the data with a value that comes from a finite set of options.


Year could be a categorical feature, if we record it as "Freshman", "Sophomore", "Junior", or "Senior"; but what if we instead record it as 1, 2, 3, or 4? 

If we use numbers for our set of options, then we have an _ordinal_ feature.

!!!def "Ordinal Feature"

	A property of the data with a numeric value that comes from a finite set of options.


!!!warning "Features in Disguise"

	Beware of categorical features that *look* like quantitative or ordinal features. 

	If students in our survey example live in three different apartment complexes, we might ask "Which apartment complex do you live in, 1, 2, or 3?".

	Even though this is a numeric value, it's not an ordinal feature because there's no quantitative difference between the apartment complexes (living in building 2 isn't twice as important as living in building 1). 

	Later on, we'll see how to make sure our machine learning algorithms know that a feature really is a categorical feature, even when it uses numeric values.

## Textbook Reading

!!!note "Optional Statistics Review"

	If it's been a while since you've studied statistics, and are feeling a bit rusty, it would probably be a good idea to review these sections from appendix A first:

	* A.1 - Descriptive Statistics for Continuous Features
	* A.2 - Descriptive Statistics for Categorical Features
	* A.3 - Populations and Samples

* Read Chapter 3 (Data Exploration) in *Machine Learning and Predictive Data Analytics*.

