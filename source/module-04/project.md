---
title: Module 04 — Hit Song, Project
---

## Overview

After a few more meetings, your team has been assigned to address the following issues asked by the stakeholders:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/tom.jpg">
	<h5>Tom Jones, Head of marketing and brand development</h5>
	<blockquote><p>After our discussion yesterday, I went back to corporate, and they want it all.</p><p>They want to know if a song is going to be popular, they want to know why it's popular, and they want to know if we can quantify how tastes have changed over the decades.</blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/ezra.jpg">
	<h5>Ezra, Lead Singer of the Wasps</h5>
	<blockquote><p>I want to know one more thing, sort of the opposite of Tom's questions. Obviously, everyone wants to top the charts, but I know a lot of guys that are living large just based on royalty from midlister songs — songs that aren't super popular, but that also aren't horrible.</p><p>So if popularity has a big timing component to it, can you also build a model or something that says "whatever you do, don't make a song like this, regardless of when it comes out?</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/tom.jpg">
	<h5>Tom Jones, Head of marketing and brand development</h5>
	<blockquote><p>In other words, I want a model that predicts hits.</p><p>Ezra wants to know if there's a way to predict flops.</p><p>Wouldn't that be the same model, but in reverse?</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/ezra.jpg">
	<h5>Ezra, Lead Singer of the Wasps</h5>
	<blockquote><p>Maybe?</p></blockquote>
</div>


<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/tom.jpg">
	<h5>Tom Jones, Head of marketing and brand development</h5>
	<blockquote><p>Either way, please have a summary of your research ready by Saturday.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern</h5>
	<blockquote><p>Hey, I put together some tips for us to use, just like old times!</p></blockquote>
</div>

!!!warning "Executive Summary"
	By now you know what level of quality we expect from you in terms of analysis summaries. From this point on, you will not be provided with an executive summary template.

	While you now have some leeway in the styling of this report, please ensure that what you turn in has the same level of quality and professionalism as previous templates.

## Tips from Johnny

!!!note "Data Dictionary"
	Our database analyst put together this [data dictionary](./spotify-dictionary.txt) to help explain the values and sources of different columns in the datasets.

!!!note "Different Views of the Data"
	There are several different views of the historic song data. One that gives just the raw data for each track. Another grouped by year, where all the hit songs for that year are aggregated based on the mean or mode values for each attribute, another by artist, another by genre, etc...

	Some of those may be more useful than others in your analysis. You might also want to generate your own summaries of the data using something other than mean and mode.

!!!note "k-Nearest Neighbors"
	You can find documentation on how to use kNN with sci-kit learn on these pages:

	* [User Guide Entry for Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)
	* [API Docs for Nearest Neighbors Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
	* [API Docs for Nearest Neighbors Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html)
	
!!!note "Hyper Parameters"
	When you build a model, you specify some settings for how the model should work. Which algorithm to use, the value of different constraints, etc... In machine learning, these values are collectively called "Hyper Parameters".

	These settings will have a large effect on how well your model performs. You could test different combinations manually, or you could use an automated method such as [Grid Search](https://scikit-learn.org/stable/modules/grid_search.html).


<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, catches you after work:</h5>
	<blockquote><p>Hey, I know you're probably busy, but in case you need it, I put together <a href='./hints.html'>this collection of Google Colab notebooks</a> that might be useful for this project.</p></blockquote>
</div>


[^1]: [Lead Singer photo by Brian Lundquist on Unsplash](https://unsplash.com/photos/3Uf-aRahKcc)

[^2]: [Head of Marketing photo by LinkedIn Sales Navigator on Unsplash](https://unsplash.com/photos/pAtA8xe_iVM)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)