---
title: Module 05 — Self Driving Cars, Case Study Discussion
body-class: index-page
---
<style type="text/css">
    article ol { list-style-type: upper-alpha; }
    article ol li { list-style-type: upper-alpha; }
</style>


## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

#### Transfer learning for from scratch

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/karl.jpg">
	<h5>Karl, Head of AI</h5>
	<blockquote><p>Obviously you'll be using a convolutional neural network to build your model, but will you be using an existing architecture as a starting point, or do you think it'll be better to design your own?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. VGG-16 would be a good architecture to use on this data.
2. ResNet would be a good architecture to use on this data.
3. Inception would be a good architecture to use on this data.
4. For best results, we should design a custom architecture.

#### Preprocessing

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>The training and test images have three color channels, (Red, Green, and Blue), with pixel values for each channel ranging from 0 to 255.</p><p>Do you think we need to do any preprocessing before using the data to train the model?</p></blockquote>
</div>

#### Data Augmentation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/emma.jpg">
	<h5>Emma, CEO of GehirnWagen</h5>
	<blockquote><p>I'm concerned that the model will only be able to recognize signs that look exactly like the ones we have images for.</p><p>I understand from Johnny that <a href="https://www.tensorflow.org/guide/keras/preprocessing_layers#preprocessing_data_before_the_model_or_inside_the_model">data augmentation</a> can help with this problem. What strategy would you suggest?</p></blockquote>
</div>

#### Model Evaluation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>This seems like one of those cases where straight accuracy might not be the best metric for model evaluation, but what do you think?</p></blockquote>
</div>

#### Confidence

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/karl.jpg">
	<h5>Karl, Head of AI</h5>
	<blockquote><p>We'd like you to actually ride in the car for a test drive, based on automation built on your sign recognition model. What performance would you require before you’d ride in the car?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Only an F1 score of 1.00 on all signs would be appropriate.
2. A recall score of 1.00 for all stop signs.
3. An accuracy of 95% would be good enough.
4. An accuracy of 85% or above for all warning/information signs, and 98% or above for all other prohibition and traffic signs.



[^1]: [CEO photo by Amy Hirschi on Unsplash](https://unsplash.com/photos/b3AYk8HKCl0)

[^2]: [Head of AI photo by Ameer Basheer on Unsplash](https://unsplash.com/photos/ABuzWPku1Ug)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)