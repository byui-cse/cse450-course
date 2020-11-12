---
title: Module 06 — Self Driving Cars, Case Study Discussion
body-class: index-page
---

## Questions
You're at a strategy meeting with the stakeholders. They want to make sure you have the data required to answer the questions they're most interested in.

Be prepared to answer the following questions:

#### Network Architecture

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/karl.jpg">
	<h5>Karl, Head of AI</h5>
	<blockquote><p>Obviously you'll be using a convolutional neural network to build your model, but will you be using a traditional architecture as a starting point, or do you think it'll be better to design your own?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. VGG-16 would be a good architecture to use on this data.
2. ResNet would be a good architecture to use on this data.
3. Inception would be a good architecture to use on this data.
4. We'll need to build a custom architecture for best results.

#### Preprocessing

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>The training and test images have three color channels, (Red, Green, and Blue), with pixel values for each channel ranging from 0 to 255.</p><p>Do you think we need to do any preprocessing before using the data to train the model?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. The RGB pixel values should be fine with that scale, since they're all the same.
2. We should use a Rescaling layer to rescale the pixel values down to the range of 0 to 1.
3. We should use a Rescaling layer to rescale the pixel values down to the range of -1 to 1.
4. We should convert the image to gray scale by taking the average value of the three channels, giving us a single gray scale channel to work with.

#### Data Augmentation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/emma.jpg">
	<h5>Emma, CEO of GehirnWagen</h5>
	<blockquote><p>I'm concerned that the model will only be able to recognize signs that look exactly like the ones we have images for.</p><p>I understand from Johnny that <a href="https://www.tensorflow.org/guide/keras/preprocessing_layers#preprocessing_data_before_the_model_or_inside_the_model">data augmentation</a> can help with this problem. What strategy would you suggest?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Data augmentation is not necessary due to the number of different training images.
2. We should use a data augmentation strategy on the data prior to loading it into the model.
3. We should use a data augmentation strategy that is based on model preprocessing layers.

#### Model Evaluation

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>This seems like one of those cases where straight accuracy might not be the best metric for model evaluation, but what do you think?</p></blockquote>
</div>

Based on your initial analysis of the data, your team feels:

1. Accuracy is still the best metric here.
2. The $F_1$ score is the best option for this problem.
3. We should probably use logarithmic loss, to be safe.


[^1]: [CEO photo by Sung Wang on Unsplash](https://unsplash.com/photos/g4DgCF90EM4)

[^2]: [Investment Banker photo by steffen Wienberg on Unsplash](https://unsplash.com/photos/ml-pxK0Ovmw)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)
