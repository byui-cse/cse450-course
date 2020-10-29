---
title: Module 05 — Bike Rentals, Case Study Discussion
body-class: index-page
---

## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

#### Network Layers

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>My brother-in-law works for a big AI company in Hong Kong. We've chatted a bit about neural networks, and I was wondering how many layers you think the network should have.</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. A single input layer and single output layer should do it.
2. An input layer, a hidden layer, and an output layer would be best.
3. An input layer, two hidden layers, and an output layer would be best.
4. An input layer, three hidden layers, and an output layer would be best.

#### Feature Engineering

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>Looking at the features we have, how do you think we should handle the temperature features?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. They should be fine the way they are.
2. They should be standardized using min-max scaling.
3. They should be normalized using a z-score transformation.
4. They should be binned, then one-hot encoded.

#### Learning Rate

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>My brother-in-law told me that I should be careful with how I handle learning rate in my network.</p><p>What approach do you think you're going to take to find the optimal learning rate?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Choosing different learning rates manually based on model performance would be best.
2. Performing a grid search on learning rate would be best. 
3. Using an adaptive learning rate would be best.
4. Using a scheduled learning rate would be best.

#### Loss Function

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>How will we know if our model has strong predictive power?</p><p>What are you planning to use for the loss function?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We'll use root mean squared error (RMSE).
2. We'll use mean squared error (MSE).
3. We'll use mean absolute error (MAE).
4. We'll use Huber loss.

#### Predictive Risk Model

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/william.jpg">
	<h5>William, Investment Banker</h5>
	<blockquote><p>Can we use AI and the GPS tracker in the bikes to keep track of where the customers are going?</p><p>This way, we can charge them a premium if they're biking through sections of the city that our models predict are more likely to result in bike theft.</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Yes, we'd need to build a neural network that approaches that as a classification problem.
2. Yes, we'd need to build a neural network that approaches that as a regression problem.
3. Yes, but not with a neural network.
4. Answering this question would be a violation of ethics and/or privacy laws.


[^1]: [CEO photo by Sung Wang on Unsplash](https://unsplash.com/photos/g4DgCF90EM4)

[^2]: [Investment Banker photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)
