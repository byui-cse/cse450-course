---
title: Exploration 02: Cereal Marketing
---

![Cereal]({{URLROOT}}/shared/img/cereal.jpg)
*[Photo by Haley Owens on Unsplash](https://unsplash.com/photos/QdwrSyJV3_4)*

## Overview

In this data exploration, you will practice the following:

* Data exploration and visualization.
* Calculating summary statistics.
* Feature engineering.

Throughout this exploration, when you're asked to use a new function or library, we'll usually provide a link to that function's documentation, or a tutorial related to it.

## Introduction

As with our previous data explorations, this assignment uses [Google Colab](http://colab.research.google.com). For more information on using Google Colab, including how to submit assignments with it, please see the information in [Data Exploration 01](./exploration-01.html) 

## Assignment

You're working as a data analyst at a cereal marketing company in New York. 

In a strategy meeting, the marketing director tells you that in 2018, the US weight loss industry was worth over $72 Billion dollars, growing 4% compared to the previous year. [^1] 

In contrast, sales of cold cereal fell 6% to $8.5 billion during the same time period. [^2]

Cereal executives have approached the marketing company asking how they can somehow tap into the weight loss market growth to boost the sales of their cereal brands.

Your assignment is to analyze a dataset of nutritional information for major US cereals, and calculate some metrics that can be used by the marketing team.

Click on the `Open In Colab` button below to open a Google Colab notebook with the template for this assignment. Once you've completed the assignment, don't forget to take the corresponding quiz in Canvas. 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Exploration_02.ipynb)

## Data Dictionary

Fields in the dataset:

    Name: Name of cereal
    mfr: Manufacturer of cereal
        A = American Home Food Products;
        G = General Mills
        K = Kelloggs
        N = Nabisco
        P = Post
        Q = Quaker Oats
        R = Ralston Purina 
    type:
        cold
        hot 
    calories: calories per serving
    protein: grams of protein
    fat: grams of fat
    sodium: milligrams of sodium
    fiber: grams of dietary fiber
    carbo: grams of complex carbohydrates
    sugars: grams of sugars
    potass: milligrams of potassium
    vitamins: vitamins and minerals - 0, 25, or 100, indicating the typical percentage of FDA recommended
    shelf: display shelf (1, 2, or 3, counting from the floor)
    weight: weight in ounces of one serving
    cups: number of cups in one serving
    rating: a rating of the cereals (Possibly from Consumer Reports?)


## Teacher's Solution

Once you have absolutely exhausted all of your best efforts in solving the data exploration problems, and you are stuck on where to go next, you can [view the teacher's solution here](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Exploration_02_Solved.ipynb).


[^1]: [Business Wire — Feb 25, 2019](https://www.businesswire.com/news/home/20190225005455/en/72-Billion-Weight-Loss-Diet-Control-Market)

[^2]: [Wall Street Journal — Aug 20, 2019](https://www.wsj.com/articles/cereal-makers-try-again-to-jump-start-stale-sales-11566293404)