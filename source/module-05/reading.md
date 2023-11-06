---
title: Module 05 — Convolutional Neural Networks
---

![Eyeball]({{URLROOT}}/shared/img/eye.jpg)
*[Photo by Amanda Dalbjörn on Unsplash](https://unsplash.com/photos/UbJMy92p8wk)*

## Overview

The objective of this module is to provide a real-world scenario in which you can practice using Convolutional Neural Networks.

!!!time "Estimated Reading Time"
	Plan on around 120 - 240 minutes for this preparation reading, which consists of online reading and videos.

## Preparation Reading

!!!note "Theory vs Practice"
	There is a lot of content to read this week. For the sake of the preparation quiz and Friday's discussion, you should go through everything in the *Theory* section below.

	The items in the *Practical* section are things you'll want to go through before you start in on the actual case study work on Monday.

### Theory

Please go through this content before the reading quiz and class discussion on Friday:

#### Convolutional Neural Networks

First, read the following article that introduces how Convolutional Neural Networks work. But, ignore the code examples, because the article uses an older version of TensorFlow:

* [CNN Explainer](https://poloclub.github.io/cnn-explainer/)

* [Deep Learning and Convolutional Neural Networks](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721)

Next, watch this video from MIT, which dives a little deeper into the concepts of how convolutional neural networks work, and how they can be used to solve machine learning problems.

<iframe width="560" height="315" src="https://www.youtube.com/embed/iaSUYvmCekI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#### Data Augmentation

Next, read through this article on [data augmentation](https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/). Don't worry too much about the code, just make sure you understand the main ideas.


#### Network Architecture

At this point, you might be wondering how to decide what network architecture is best? How do you decide how many convolutional layers to use? How do you pick a filter size? How do you determine how many filters and dense layers to use?

The most common approach is to experiment — adjust parameters one at a time and see how those adjustments affect your outcome. 

Another approach is to start with one of the many [well known CNN network architecture designs](https://www.jeremyjordan.me/convnet-architectures/) and adjust those as needed for your particular problem.

CNN architecture is a [very active](https://www.aismartz.com/blog/cnn-architectures/) field of development. As with most things in machine learning, there is no "one size fits all" answer.


### Practical

Please go through this content before class on Monday:

* Read [this collection of tutorials on the Keras library](./keras-cnn.html)







