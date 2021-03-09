---
title: Module 06 — Self Driving Cars, Project
---

## Overview

After a few more meetings, your team has been assigned to address the following issues asked by the stakeholders:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/thomas.jpg">
	<h5>Thomas, COO of HackPressIO</h5>
	<blockquote><p>So the main thing we need at this point is a proof of concept model that shows we could, with enough work, generate full texts in the style and voice of a particular author.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/monika.jpg">
	<h5>Monika, Senior Developer</h5>
	<blockquote><p>I agree. The original team used Jane Austen as their training corpus, but you could use any author's work you find at <a href="https://www.gutenberg.org">Project Gutenberg</a>. Just be sure to clean up the data appropriately.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/thomas.jpg">
	<h5>Thomas, COO of HackPressIO</h5>
	<blockquote><p>I think that in order for me to feel good about whatever pipeline is being developed, I'd want to see works in the style of more than one author, at least two or three.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern</h5>
	<blockquote><p>Which means a separate network trained on each author's works...</p><p>It might be a good idea to define a network architecture used for all authors, and then save the trained model for each author, so you can load a given author's profile into the network whenever you wanted...but we'll leave the specifics up to you.</blockquote>
</div>

## More Tips from Johnny

!!!warning "keras vs tf.keras"
	Don't forget the warning from the last module, about how Keras used to be a standalone library, but as of September 2019, it is part of Google's TensorFlow 2.0 library.

	Keep that in mind if you're looking at any tutorial that was written prior to that date. Most of the API and functions will be the same, but your import statements will likely be different. 

	For more information, [see this article on the change](https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/).

!!!note "Starter Code"
	This [Colab notebook](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_publishing.ipynb) contains the starter code left by the previous team. 

	There may be better approaches than what that notebook is doing, but it will at least get you started.
	
!!!note "Saving Models"
	There are multiple ways to [save a Keras model](https://www.tensorflow.org/guide/keras/save_and_serialize). 

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, catches you after work:</h5>
	<blockquote><p>Hey, I know you're probably busy, so I put a bunch of comments and explanations in <a href="https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_publishing.ipynb">the code left behind by the previous team</a>, so make sure you read through those. Also, make sure you review <a href="./keras-rnn.html">the RNN tutorials from the reading assignment</a>.</p></blockquote>
</div>


[^1]: [COO photo by Jonas Kakaroto on Unsplash](https://unsplash.com/photos/mjRwhvqEC0U)

[^2]: [Senior Developer photo by Mimi Thian on Unsplash](https://unsplash.com/photos/8kdA2IJsjcU)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)