---
title: Module 04 — Bike Rentals, Case Study Discussion
body-class: index-page
---

<style type="text/css">
    article ol { list-style-type: upper-alpha; }
    article ol li { list-style-type: upper-alpha; }
</style>

## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

#### Network Layers and Hyperparameters

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>My brother-in-law works for a big AI company in Hong Kong. We've chatted a bit about neural networks, and I was wondering how many layers you think the network should have.</p>
	<p>If you run your model on the data and the results seem lower than you expected, which of the following hyperparameters do you feel has the most potential for model improvement?
	</p></blockquote>
</div>

1. Number of neurons and number of hidden layers.
2. Learning rate and optimizer selection.
3. Batch size and number of epochs.
4. Activation functions of the layers and overall loss function.


#### Feature Engineering

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>Looking at the features we have, how do you think we should handle the temperature features?</p></blockquote>
</div>

#### Learning Rate

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>My brother-in-law told me that I should be careful with how I handle learning rate in my network.</p><p>What approach do you think you're going to take to find the optimal learning rate?</p></blockquote>
</div>

#### Loss Function

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>How will we know if our model has strong predictive power?</p><p>What are you planning to use for the loss function?</p></blockquote>
</div>

#### Predictive Risk Model

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/william.jpg">
	<h5>William, Investment Banker</h5>
	<blockquote><p>We would like use AI to predict the likelihood of damage based on user profile data, such as name, birthday, sex, or address, so that we can add an insurance premium to the rental cost. We are concerned that there may be ethical/legal implications here, what would you recommend?</p></blockquote>
</div>

#### Pandemic and Health Concerns

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/zhao.jpg">
	<h5>Zhao, CEO of WelcomeBike</h5>
	<blockquote><p>Coming out of the pandemic has put a strain on resources. Our customers are much more concerned about health and safety of sharing bikes.</p><p>In your executive summary, would you add your recommendations for when we could pull bikes out of rotation to clean and disinfect them? For example, what days and times we should bring them in?</p><p>We also need to know if we have any lasting problems now that we are a few years past COVID-19. What can we expect for forcasts into the future? Are we back on track or still recovering?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. We can do this, as long as the users have provided that profile data and we have kept record of previous damages.
2. Using any profile data in this way would be inappropriate.
3. As long as we only use name and address, that would be fine.
4. Instead of using their profile data, we could track their usage via GPS and feed those live statistics (speed, angle, direction) into the model and deactivate the bike if the model predicts they will damage the bike. (For example, if they were going extremely fast down a crowded sidewalk.)



[^1]: [CEO photo by Sung Wang on Unsplash](https://unsplash.com/photos/g4DgCF90EM4)

[^2]: [Investment Banker photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)
