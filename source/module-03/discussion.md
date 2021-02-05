---
title: Module 03 — Housing Estimates, Class Discussion Questions
---

![Meeting]({{URLROOT}}/shared/img/meeting.jpg)
*[Photo by Campaign Creators on Unsplash](https://unsplash.com/photos/gMsnXqILjp4)*

## Questions
You're about to go into a strategy meeting with the CEO, Vice President of Human Resources, and Vice President of Finance. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

### Problem Type

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/devon.jpg">
	<h5>Devon, the CEO says:</h5>
	<blockquote><p>I just sat through four hours of machine learning training with the board of directors this past week, so I'm curious to get your take on this.</p> 
	<p>Looking at the data and our business model, what kind of machine learning problem do you think we're looking at here?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. This is a supervised regression problem
2. This is a supervised classification problem
3. This is an unsupervised learning problem
4. This is a semi-supervised learning problem

### Model Confidence

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/cecil.jpg">
	<h5>Cecil, the VP of Customer Relations asks:</h5>
	<blockquote><p>My biggest concern right now is making sure that whatever method we come up with to predict housing prices, we can also attach some kind of empirical confidence metric.</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels you can best show confidence in your model by using:

1. The sum of squares error (SSE).
2. The mean squared error (MSE).
3. The root mean squared error (RMSE).
4. The $R^2$ value.

### Insurance Question

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/william.jpg">
	<h5>William, the VP of Finance asks:</h5>
	<blockquote><p>Our insurance division is particularly interested in making sure our investment portfolio avoids certain — uh — less savory property types.</p><p>Is there a way we can easily identify properties in low income areas and have the model lower those estimates to protect our investors' interests?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We have the necessary data in the correct form to answer this question.
2. The data we have cannot answer that question, we need to collect more data.
3. We could use the data we have, but we'll have to normalize some of the features, and/or encode some of them differently.
4. Answering this question would be a violation of ethics and/or privacy laws.


### Data Analysis

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern asks:</h5>
	<blockquote><p>The head of data science says we should use gradient boosted trees for this analysis.</p><p>I've noticed that a lot of the features use pretty different ranges.</p>
	<p>For example, how should we handle square footage?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We should normalize square footage values using range normalization (aka min-max scaling).
2. We should standardize square footage values using z-score normalization.
3. We should use binning to group square footage values into discrete categories.
4. We should be fine sticking with the raw values.


[^1]: [CEO photo by Oz Seyrek on Unsplash ](https://unsplash.com/photos/-Ir03_pgpMU)

[^2]: [VP of Customer Support photo by Christina @ wocintechchat.com](https://unsplash.com/photos/SJvDxw0azqw)

[^3]: [VP of Finance photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^4]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)