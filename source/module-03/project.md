---
title: Module 02 — Housing Estimates, Project
---

## Overview

After a few more meetings with the executive team, the head of the data science division has assigned your team to address the following issues asked by the stakeholders:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/cecil.jpg">
	<h5>Cecil, the VP of Customer Relations says:</h5>
	<blockquote><p>The biggest thing I want to see is quantifiable evidence that the predictions we come up with are reliable.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/william.jpg">
	<h5>William, the VP of Finance asks:</h5>
	<blockquote><p>I'd like to know which property types are weighing most heavily in the house prices predicted by your model. My excel spreadsheets can tell me that information for our current methodology...can your so-called artificial intelligence do the same?</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/devon.jpg">
	<h5>Devon, the CEO adds:</h5>
	<blockquote><p>Yes...thank you William. These are all great questions.</p><p>One other question the board was wondering about, is if there are additional factors about these areas that might be affecting prices, which we aren't taking into account.</p><p>That may be a little above and beyond what you're team is planning, since it would require finding more data from an external source and correlating it with the data we already have, but if you have the time, I know they'd appreciate it.</p>
	<p>If you could send us <a href='./summary.docx'>your team's write up on this by Saturday night</a>, that would be great.</p></blockquote>
</div>

!!!note "Team Project Expectations"
	Be sure to read over the [Team Project Expectations](../course/projects.html) guide to know what the expectations are for this and future projects.


## Tips from Johnny

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern, whispers to you after the meeting:</h5>
	<blockquote><p>Hey, I put together a list of tips and ideas that might help us out:</p></blockquote>
</div>

!!!note "Data Dictionary"
	Our database analyst put together this [data dictionary](./housing-dictionary.txt) to help explain the values and sources of different columns in the [housing dataset](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/housing.csv), so be sure to review that.

!!!note "Feature Scaling"
	If you're going to be comparing different numeric features, be sure they are using the same scale. You may find it useful to use min-max scaling to handle this problem. You could do this calculation manually, or use [Sci-Kit Learn's MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

!!!note "Binning"
	Just as you did with the Titanic dataset when you reduced the number of titles, you may find it useful to "bin" certain features into discrete groups in order to address some of the questions above. There are multiple ways to do this, but previously we used the [`map()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html).

!!!note "Adding External Data"
	If you do decide to add additional data from another source, such as data you find related to a particular zip code, you might find [this Pandas tutorial on combining tables](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html) to be useful.

!!!note "XGBoost"
	You can find documentation on how to use xgboost to be useful, particularly the sections on the sklearn wrapper:

	* [User Guide for XGBoost](https://xgboost.readthedocs.io/en/latest/)
	* [API Reference for the SKLearn Wrapper](https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=sklearn#module-xgboost.sklearn)
	* [An XGBoost tutorial that uses the sklearn wrapper](https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/)
	* [A more in-depth tutorial on xgboost](https://www.kaggle.com/stuarthallows/using-xgboost-with-scikit-learn)
	* [An XGBoost tutorial that does not use the sklearn wrapper](https://towardsdatascience.com/a-beginners-guide-to-xgboost-87f5d4c30ed7)

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, drops by your hotel room around midnight:</h5>
	<blockquote><p>Okay, just one last thing, if you need any more help at all, I put together <a href='./hints.html'>this collection of Google Colab notebooks</a> that might be useful.</p></blockquote>
</div>


[^1]: [CEO photo by Oz Seyrek on Unsplash ](https://unsplash.com/photos/-Ir03_pgpMU)

[^2]: [VP of HR photo by Christina @ wocintechchat.com](https://unsplash.com/photos/SJvDxw0azqw)

[^3]: [VP of Finance photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^4]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)