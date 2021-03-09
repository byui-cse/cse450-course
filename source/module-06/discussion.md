---
title: Module 06 — Content Creation, Case Study Discussion
body-class: index-page
---

## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

#### Network Architecture

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/thomas.jpg">
	<h5>Thomas, COO of HackPressIO</h5>
	<blockquote><p>Do you think we should be using LSTM layers or GRU layers in this network?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. One or more LSTM layers would be best.
2. One or more GRU layers would be best.
3. A combination of LSTM and GRU would work best.
4. They should work equally well for this type of problem.

#### Learning Strategy

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>I'm wondering what your views are on using a teacher forcing strategy compared to a curriculum learning strategy?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Teacher Forcing would be our best bet in this situation.
2. We would recommend Curriculum Learning here.
3. Either one should work just as well.
4. We're going to implement a custom strategy.

#### Model Evaluation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/monika.jpg">
	<h5>Monika, Senior Developer</h5>
	<blockquote><p>Our previous team used logits in the output layer and then used Sparse Categorical Cross Entropy as the loss function. Are you planning to use that approach as well?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Yes, Sparse Categorical Cross Entropy with logits is the best approach here.
2. It would be better to use SoftMax without logits.
3. We're thinking that we should use regular Categorical Cross Entropy and encode the data differently.

[^1]: [COO photo by Jonas Kakaroto on Unsplash](https://unsplash.com/photos/mjRwhvqEC0U)

[^2]: [Senior Developer photo by Mimi Thian on Unsplash](https://unsplash.com/photos/8kdA2IJsjcU)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)