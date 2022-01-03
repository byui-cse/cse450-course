---
title: Module 03 — Housing Estimates, Class Discussion Questions
---

<style type="text/css">
    article ol { list-style-type: upper-alpha; }
    article ol li { list-style-type: upper-alpha; }
</style>

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
	<blockquote><p>Our insurance customers are particularly interested in making sure that homes in… unsavory neighborhoods, aren't estimated high.</p>
<p>Is there a way we can easily identify properties in low income areas and have the model lower those estimates to protect our insurance customers' interests?
</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We can lower the predicted price for specific neighborhoods before training the model.
2. We can add average income or other demographic information for the area as features.
3. For specific zip codes we could add a step to our pipeline that reduces the predicted price by a specific percentage prior to outputting the final price result to ensure the properties aren’t being overvalued.
4. Taking this kind of action would be a violation of federal laws and/or ethics.



### Data Analysis

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern asks:</h5>
	<blockquote><p>The head of data science says we should use gradient boosted trees for this analysis.</p><p>I've noticed that a lot of the features use pretty different ranges.</p>
	<p>For example, how should we handle square footage?</p></blockquote>
</div>


[^1]: [CEO photo by Oz Seyrek on Unsplash ](https://unsplash.com/photos/-Ir03_pgpMU)

[^2]: [VP of Customer Support photo by Christina @ wocintechchat.com](https://unsplash.com/photos/SJvDxw0azqw)

[^3]: [VP of Finance photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^4]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)