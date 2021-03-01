---
title: Module 05 — Self Driving Cars, Project
---

## Overview

After a few more meetings, your team has been assigned to address the following issues asked by the stakeholders:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/emma.jpg">
	<h5>Emma, CEO of GehirnWagen</h5>
	<blockquote><p>I think everyone is agreed on what we need — a neural network that can recognize street signs here in Germany.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/karl.jpg">
	<h5>Karl, Head of AI</h5>
	<blockquote><p>Yes, and just as a technical note, our other smart car products integrate tightly with Apple's CarKit.</p><p>So whenever you feel like you have a decent model, please save it in a format that we can import into Apple's MLKit framework.</blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the data science intern</h5>
	<blockquote><p>Given how many variables there are in building convolutional neural networks, and how long it takes to train and test them, we probably need everyone on the team working on building and testing convolutional neural networks.</p><p>I'd suggest that you coordinate how to tackle that in a smart way.</blockquote>
</div>

## More Tips from Johnny

!!!warning "keras vs tf.keras"
	Don't forget the warning from the last module, about how Keras used to be a standalone library, but as of September 2019, it is part of Google's TensorFlow 2.0 library.

	Keep that in mind if you're looking at any tutorial that was written prior to that date. Most of the API and functions will be the same, but your import statements will likely be different. 

	For more information, [see this article on the change](https://www.pyimagesearch.com/2019/10/21/keras-vs-tf-keras-whats-the-difference-in-tensorflow-2-0/).


!!!note "Data Dictionary"
	Use this [data dictionary](./signs-dictionary.txt) to help explain how the data set is structured.

!!!note "Starter Code"
	Loading image data can be tricky, but this [Colab notebook](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_signs.ipynb) should be helpful. 

	There may be better ways to handle the data than what that notebook is doing, but it will at least get you started.
	
!!!note "Saving Models"
	There are multiple ways to [save a Keras model](https://www.tensorflow.org/guide/keras/save_and_serialize). 

	Since the AI team is planting to integrate this model into a techstack based on Apple's frameworks, be sure to see what Apple's requirements are for [user defined machine learning models](https://coremltools.readme.io/docs/tensorflow-2#conversion-from-user-defined-models).

	Note that you don't have to actually convert the model using Apple's tools, just save it in a format that the AI team can use to convert it later.

!!!note "Preexisting Architectures"
	If you want to try using a pre-existing CNN architecture instead of building your own, you can see [a list of options here](https://www.tensorflow.org/api_docs/python/tf/keras/applications).

	Note that with each of these, there are two options:

	1. You can load just the architecture and train it from scratch using the road sign training data. (By setting the `weights` parameter to `None`).

	2. You can load the pretrained model and use *Transfer Learning* techniques (see below) to adapt it to the road sign training data. (By setting the `weights` parameter to `imagenet`).

!!!note "Transfer Learning with Pretrained Models"
	If you're going to try and use a pretrained model to try and solve this problem, you might want to read through [this guide](https://www.tensorflow.org/guide/keras/transfer_learning) to see how you can fine tune a pre-existing model for a new problem.

!!!note "TensorBoard"
	If you're looking for a good individual above and beyond topic, you might want to check out [TensorBoard](https://www.tensorflow.org/tensorboard/get_started), a tool created by Google to make it easier to see a visual representation of what's happening in your network.

	Note that just throwing TensorBoard into a notebook doesn't count as going above and beyond. You need to dive into that documentation and really understand what it's doing and how it can help you.

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, the Data Science Intern, catches you after work:</h5>
	<blockquote><p>Hey, I know you're probably busy, I was going to put together some hints and sample code for you like I usually do, but the best example code I can provide is what you see in those <a href="./keras-cnn.html">CNN tutorials from the reading assignment</a>. So, be sure to read over those.</p></blockquote>
</div>


[^1]: [CEO photo by Amy Hirschi on Unsplash](https://unsplash.com/photos/b3AYk8HKCl0)

[^2]: [Head of AI photo by Ameer Basheer on Unsplash](https://unsplash.com/photos/ABuzWPku1Ug)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)