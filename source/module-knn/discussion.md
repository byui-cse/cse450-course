---
title: Module 04 — Hit Songs, Case Study Discussion
body-class: index-page
---

## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

### Data Science Methods

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>I guess the first thing we need to decide is if this is a classification problem or a regression problem.</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. This is a classification problem.
2. This is a regression problem.

### Additional Insights

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/tom.jpg">
	<h5>Tom Jones, Head of marketing and brand development</h5>
	<blockquote><p>I don't want to know just whether or not a particular song is going to be a hit or not, I want to know what goes into making it a hit. What are the most important factors and which factors don't matter at all.</p><p>Is there an algorithm that can tell me that?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Yes, k Nearest Neighbors can answer that question.
2. Yes, decision trees would do a good job here.
3. Yes, clustering is the way to answer that question.
4. No, all we can give you is a predictive model, not tell you why how it works.

### Timing

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/ezra.jpg">
	<h5>Ezra, Lead Singer of the Wasps</h5>
	<blockquote><p>But if we're like, using a bunch of old data, won't your model just predict what would have been a popular song twenty years ago?</p><p>How can we make sure that what the model predicts for today would actually be popular today?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels that the best way to handle this is:

1. To stratify the training and test data by decade to figure this out using some kind of model ensemble.
2. To look for features that persist across the decades and appear to be timeless.
3. To filter the dataset to include only the songs that were popular in the last ten years or so.
4. There's no way to guarantee this.

### Model Evaluation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>How will we know if our model has strong predictive power?</p><p>Which evaluation metric will we use?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We'll use the accuracy of test set predictions.
2. We'll use the $F_1$ score.
3. We'll use the root mean squared error (RMSE).
4. We'll use the $R^2$ value.


[^1]: [Lead Singer photo by Brian Lundquist on Unsplash](https://unsplash.com/photos/3Uf-aRahKcc)

[^2]: [Head of Marketing photo by LinkedIn Sales Navigator on Unsplash](https://unsplash.com/photos/pAtA8xe_iVM)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)
