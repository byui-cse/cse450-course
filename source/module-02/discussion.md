---
title: Module 02 — Targeted Marketing, Case Study Discussion
body-class: index-page
---

## Questions
You're at dinner with the President of the bank, VP of Marketing, and the Senior Data Scientist. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

### Data Science Methods

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/miguel.jpg">
	<h5>Miguel Ferreira, Bank President asks:</h5>
	<blockquote><p>The core task we're interested in is identifying those customers most likely to subscribe to a term deposit.</p><p>A <em>term deposit</em> is a fixed-term investment that includes the deposit of money into an account at a financial institution. In this case, our financial institution.</p>
	<p>I don't know a lot about data science, but I've been trying to get up to speed. Do you think a supervised or unsupervised approach would work best for this situation?</p>
	</blockquote>
</div>

### Train Test Split

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/beatriz.jpg">
	<h5>Beatriz, Senior Data Scientist asks:</h5>
	<blockquote><p>Miguel, that is a great question.</p>
	<p>While we are asking detailed questions, the dataset has approximately 37,000 records. How much of that data will you use to train your model?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. A simple 80/20 split will provide us with enough to accurately train and test our model.
2. A 50/50 split so that we have the same amount of training data as testing.
3. We will pull out 1,000 records for our test dataset and use the other 36,000 for training. This gives our model more to train on and will produce better results.
4. We will use all 37,000 for training and use cross-validation to evaluate the model.


### Additional Insights

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/francisco.jpg">
	<h5>Francisco, VP of Marketing asks:</h5>
	<blockquote><p>Aside from the core marketing question Miguel mentioned, I'm wondering if there are other insights we could gain from our data.</p>
	<p>I can look at the data and tell that some days of the week or some months produce better results than others.</p><p>I'm wondering if it's possible for us to see if those results are true for all customers, or if some types of customers respond better on certain days than others?</p></blockquote>
</div>

### Data Privacy Laws

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/beatriz.jpg">
	<h5>Beatriz, Senior Data Scientist asks:</h5>
	<blockquote><p>Since we're operating in the European Union, we're subject to GDPR compliance requirements.</p>
	<p>What do you think we might need to do for this project in order to be compliant with GDPR regulations?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. This is historic data, so we should be just fine.
2. This is anonymous data, so we should be just fine.
3. The GDPR doesn't apply in this situation, since we're just building a model, not selling data.
4. In order to use this data under GDPR, we'll need to get consent from the customers in the dataset.


[^1]: [Chairman of the Board photo by Portuguese Gravity on Unsplash](https://unsplash.com/photos/oMF2q4tlhDg)

[^2]: [President photo by Roland Samuel on Unsplash](https://unsplash.com/photos/MZ5A24H1JqU)

[^3]: [VP of Marketing photo by Mehrad Vosoughi on Unsplash](https://unsplash.com/photos/iUQmEFtfdLw)

[^4]: [Head of Data Science photo by Mateus Campos Felipe ](https://unsplash.com/photos/WnPJft0DJpk)
