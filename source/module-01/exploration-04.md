---
title: Exploration 04: US Honey Production
---

![Jar of Honey]({{URLROOT}}/shared/img/honey.jpg)
*[Photo by Alexander Mils on Unsplash](https://unsplash.com/photos/nesUgwNX3u4)*

## Overview

In this data exploration, you will:

* Perform some probability calculations.

Throughout this exploration, when you're asked to use a new function or library, we'll usually provide a link to that function's documentation, or a tutorial related to it.

## Introduction

As with our previous data explorations, this assignment uses [Google Colab](http://colab.research.google.com). For more information on using Google Colab, including how to submit assignments with it, please see the information in [Data Exploration 01](./exploration-01.html) 

## Assignment

A local farmer's cooperative has expressed concern about the effect the use of Neonic pesticides has on honeybee populations.

They've asked you to analyze the data and identify any trends that might suggest a link between the increased use of pesticides and a decrease in honeybee health.


### Notes about the data

This dataset merges two different datasets. One on honey production, the other by pesticide use.

From USDA data:

* `numcol`: Number of honey producing colonies. Honey producing colonies are the maximum number of colonies from which honey was taken during the year. It is possible to take honey from colonies which did not survive the entire year

* `yieldpercol`: Honey yield per colony. Unit is pounds

* `totalprod`: Total production (numcol x yieldpercol). Unit is pounds

* `stocks`: Refers to stocks held by producers. Unit is pounds

* `priceperlb`: Refers to average price per pound based on expanded sales. Unit is dollars.

* `prodvalue`: Value of production (totalprod x priceperlb). Unit is dollars.

From USGS Data:

* `nCLOTHIANIDIN`: The amount in kg of CLOTHIANIDIN applied

* `nIMIDACLOPRID`: The amount in kg of IMIDACLOPRID applied

* `nTHIAMETHOXAM`: The amount in kg of THIAMETHOXAM applied

* `nACETAMIPRID`: The amount in kg of ACETAMIPRID applied

* `nTHIACLOPRID`: The amount in kg of THIACLOPRID applied

* `nAllNeonic`: The amount in kg of all Neonics applied = (nCLOTHIANIDIN + nIMIDACLOPRID + nTHIAMETHOXAM + nACETAMIPRID + nTHIACLOPRID)


### Colab Link

Click on the `Open In Colab` button below to open a Google Colab notebook with the template for this assignment. Once you've completed the assignment, don't forget to take the corresponding quiz in Canvas. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Exploration_04.ipynb)

## Teacher's Solution

Once you have absolutely exhausted all of your best efforts in solving the data exploration problems, and you are stuck on where to go next, you can [view the teacher's solution here](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Exploration_04_Solved.ipynb).
