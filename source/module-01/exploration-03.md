---
title: Exploration 03: Class Distinctions
---

![Iceberg]({{URLROOT}}/shared/img/iceberg.jpg)
*[Photo by Derek Oyen on Unsplash](https://unsplash.com/photos/4ReskwNsh68)*

## Overview

In this data exploration, you will:

* Analyze feature relationships using visualizations.
* Perform feature engineering.

Throughout this exploration, when you're asked to use a new function or library, we'll usually provide a link to that function's documentation, or a tutorial related to it.

## Introduction

As with our previous data explorations, this assignment uses [Google Colab](http://colab.research.google.com). For more information on using Google Colab, including how to submit assignments with it, please see the information in [Data Exploration 01](./exploration-01.html) 

## Assignment

You're working on an exhibit for a local museum called "The Titanic Disaster". They've asked you to analyze the passenger manifests and see if you can find any interesting information for the exhibit. 

The museum curator is particularly interested in why some people might have been more likely to survive than others.

!!!note "Seaborn Version"
	If you're trying to use a visualization in this assignment that you read about in the Seaborn documentation, but which gives you an error about being unavailable, it might be because that function was added in a more recent version than the one Google Colab uses by default.

	You can see what version of seaborn you have installed in your Colab runtime with this commands:

		import seaborn as sns
		sns.__version__

	The [What's New in Each Version Page](https://seaborn.pydata.org/whatsnew.html) tells you what has been added with each version, so you can see if what you're trying to use is too recent.

	If you want to upgrade the version of seaborn used by your runtime, which will give you access to the latest features, you can issue a command using the `!` prefix:

		!pip install seaborn --upgrade

	Once this command finishes, the runtime will likely tell you that you need to restart the runtime for that change to take affect. This will also require you to re-run all of your code cells, which can result in reimporting an older version of seaborn again. 

	To get around this issue, put the upgrade command in your very first cell, restart the runtime, then run all your cells. 

	If you don't need or want to use the latest version of seaborn, you can ignore this information.

### Notes about the data

Column Information:

* Survived: Did the passenger survive? (0 = no, 1 = yes)
* Pclass: The passenger's ticket class. (1 = 1st, 2 = 2nd, 3 = 3rd)
* Name: The passenger's name
* Sex: The passenger's gender
* Age: The passenger's age in years
* SibSp: Count of the passenger's siblings and spouse also aboard.
* Parch: Count of the passenger's parents and children also aboard.
* Ticket: The passenger's ticket number
* Fare: The amount the passenger paid for their ticket.
* Cabin: The passenger's cabin id.
* Embarked: Where the passenger embarked from (C = Cherbourg, S = Southampton, Q = Queenstown)

Click on the `Open In Colab` button below to open a Google Colab notebook with the template for this assignment. Once you've completed the assignment, don't forget to take the corresponding quiz in Canvas. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Exploration_03.ipynb)

## Teacher's Solution

Once you have absolutely exhausted all of your best efforts in solving the data exploration problems, and you are stuck on where to go next, you can [view the teacher's solution here](https://github.com/byui-cse/cse450-course/blob/master/notebooks/Exploration_03_Solved.ipynb).
