---
title: Exploration 01: Netflix Movies
---

## Overview

In this data exploration, you will:

* Create a Kaggle account to gain access to the datasets and development environment we'll use in this course.
* Stage the dataset you'll use in this exploration.
* Learn how to load, explore, and filter data with the Pandas library.
* Perform some basic data visualization with the Seaborn graphing library.

Througout this exploration, when you're asked to use a new function or library, we'll usually provide a link to that function's documentation, or a tutorial related to it. "

## Introduction

Throughout the course, we'll be using [Kaggle](https://kaggle.com) for most of our data exploration and modeling. 

This assignment will teach you how Kaggle works and give you some practice using it. You'll also get some practice using the Python language, as well as some of the most popular libraries used by professional data scientists.

!!!note "Learning Python and Friends"

	The assignments in this course require a fair amount of Python coding as well as the use of a few popular Python-based data science tools. We don't spend much time in this class explicitly learning Python or these tools, for a few reasons:

	* In industry, you'll often be asked to complete a task or project that requires quickly coming up to speed on a new technology or software library that you've never used before.

	* By the time you start your first job in data science, many of the tools and libraries will be different anyway, so we try to focus on teaching principles and helping you "learn how to learn" on your own so you can keep up with this rapidly changing field.

	* As a 400-level student, we expect that at this point you have enough diligence and experience reading technical documentation and tutorials that you can handle this largely on your own.

	However, we have put together [a guide containing some good references and tutorials]({{URLROOT}}/course/tools.html), as well as tips for reading technical documentation.

## Introduction to Kaggle

Kaggle is a data repository, data science competiton site, and cloud-based data science development environment. It includes support for the most widely used libraries and tools in data science, as well as providing access to optimized hardware for data analysis.

Kaggle uses "Jupyter Notebooks" for data exploration and analysis. If you've never heard of those before, Jupyter Notebooks are interactive documents that contain a mix of text and python code "cells".

!!!note "Local Development vs Kaggle"

	While it's possible to use Jupyter notebooks locally, Kaggle provides a lot of great datasets, and access to cloud-based instances that have all the standard data science libraries pre-installed and configured for use.

	You *can* opt to do your development locally, but keep in mind that you'll still have to submit via Kaggle, which means you'll have to upload your Jupyter notebooks to that site, and if you run into problems with your local configuration, you'll be largely on your own to sort that out.

The following video will walk you through how to complete this first assignment, demonstrating how to use Kaggle, some things to watch out for when using it, and the different ways you can submit a Kaggle notebook assignment.

[!embed](https://www.youtube.com/watch?v=PJzijKS7sOo)

## Assignment

A consumer watchdog group wants to see if Netflix has more movies for adults or children. 

Using a dataset containing metadata for all of the movies Netflix had available on their platform in 2019, determine if they are correct.


### Stage the data

First, we'll load the dataset into our development environment. Since this is a Kaggle dataset, we can load it directly from their data repository:


1. If the right sidebar isn't visible, click on the `|<` button in the top right-hand corner of the window.

2. In the right sidebar, click the `+ Add data` button.

3. In the window that appears, search for `Netflix`, then change `Sort By` to `Most votes`.

4. The topmost dataset should be `Netflix Movies and TV Shows`. Click the `Add` button next to it.

5. Once you see a little message that the data is read to use, click the `⌄` button next to `+ Add data` to view the files available to your notebook. Expand the arrow next to `netflix-shows` so you can see the `netflix_titles.csv` file.

6. Hover over that file and click the button on the right to `Copy file path`. Make sure you copy the path to the `netflix_titles.csv` file, not the `netflix-shows` folder.
