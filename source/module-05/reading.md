---
title: Module 05 — Neural Networks
---

![Clustering]({{URLROOT}}/shared/img/network.jpg)
*[Photo by Akshay Nanavati on Unsplash](https://unsplash.com/photos/Zq6HerrBPEs)*

## Overview

!!!time "Estimated Reading Time"
	Plan on around 120 - 240 minutes for this preparation reading, which consists of online reading and videos. 

The objective of this module is to provide a real-world scenario in which you can practice using Neural Networks.

## Preparation Reading

!!!def "Lots of Vocabulary"
	You will likely come across _a lot_ of new vocabulary as you study neural networks.

	[This resource from Google](https://developers.google.com/machine-learning/glossary) provides
	a nice reference.

This module's reading has the following components:

* An introduction to neural networks
* An overview of activation functions
* A discussion of hyperparameters
* A set of tutorials for the Keras framework you'll be using to create neural networks
* Some optional extended reading for going further

### Neural Networks Intro

Watch the first three videos on [this playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), which introduce neural networks, gradient descent, and backpropagation. The fourth video is optional:

[!embed](https://www.youtube.com/watch?v=aircAruvnKk)

[!embed](https://www.youtube.com/watch?v=IHZwWFHWa-w)

[!embed](https://www.youtube.com/watch?v=Ilg3gGewQ5U)

### Activation Functions

The videos mention the _Sigmoid_ activation function. There are lots of different activation functions used in neural networks, and it's an area of active research. 

There are three key things to know about activation functions in the context of neural networks:

#### Functions Convert Inputs to Outputs
Like all mathematical functions, activation functions take an input and convert it to an output.[^1]

!!!note "Function Syntax"
	You might be used to seeing functions written like this: $y = mx + b$, which we might read as:

	*Y is equal to m times x plus b.*

	But, often functions are written using this syntax: $f(x) = mx + b$, which results in the same answer, but is read as:

	*The output of the function is m times the input, plus b.*

	Activation functions (and most higher math in machine learning) use the second syntax.

Here's a really simple activation function:

$$f(x) = x$$

This function just says, whatever $x$ is (the input), $f(x)$ (the output) will be the same thing.

Many activation functions are [piecewise functions](https://www.mathsisfun.com/sets functions-piecewise.html). 

For example:

$$f(x) = \begin{cases} 
						0, &\text{if } x \leq 0 \\\\
						x, &\text{if } x \gt 0 
					\end{cases} $$

This function says that if $x$ (the input) is less than or equal to 0, $f(x)$ (the output) will be 0. If $x$ is greater than 0, then the output will just be $x$.

#### Activation Functions in Neural Networks

Activation functions are used to determine what the output of a [perceptron](https://developers.google.com/machine-learning/glossary#perceptron) should be.

Different activation functions have different behaviors and side-effects. Some types are better suited to certain problems than others. 

The videos you watched mention the [Sigmoid activation function](https://developers.google.com/machine-learning/glossary#sigmoid_function), which was popular in neural networks for many years.

Currently, the [Rectified Linear Unit (ReLU) activation function](https://developers.google.com/machine-learning/glossary#ReLU) is the most commonly used.[^2]

As with most things in machine learning, the general strategy for choosing the best activation function is to try different variations and measure the results.[^3]

### Hyperparameters

In the context of neural networks, hyperparameters are the settings you adjust that control the structure of the network, as well as how it learns.

[This article](https://missinglink.ai/guides/neural-network-concepts/hyperparameters-optimization-methods-and-real-world-model-management/) gives a good overview of the different hyperparameters in a neural network, what they control, and strategies for finding optimum values.

### Keras

We'll be using Keras for creating neural networks. Keras is a library like SciKit-Learn, but designed specifically for neural networks. 

Note that Keras used to be a standalone library, but is now part of Google's TensorFlow library.

On the [TensorFlow Tutorials Page](https://www.tensorflow.org/tutorials), in the left sidebar, you'll see a section called "Beginner". Under that section you'll see a "ML Basics with Keras" section and a "Load and preprocess data" section.

You'll want to review the following examples in ML Basics:

* [Image Classification with Keras](https://www.tensorflow.org/tutorials/keras/classification)
* [Regression with Keras](https://www.tensorflow.org/tutorials/keras/regression)
* [Overfit and Underfit](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit)
* [Save and Load](https://www.tensorflow.org/tutorials/keras/save_and_load)
* [Tune Hyperparameters with the Keras tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner)

And at least the following under "Load and preprocess data":

* [pandas.DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)
* [CSV](https://www.tensorflow.org/tutorials/load_data/csv)
* [Images](https://www.tensorflow.org/tutorials/load_data/images)

You might also want to keep this [Keras API reference page](https://keras.io/api/) handy.

### Additional Reading

As mentioned, there is a lot of information on neural networks. It's an extremely popular area of research right now. Here are some good resources for going further:

* [Setting the learning rate of your neural network](https://www.jeremyjordan.me/nn-learning-rate/)
* [Why Momentum Really Works](https://distill.pub/2017/momentum/)
* [The Neural Networks and Deep Learning online eBook](http://neuralnetworksanddeeplearning.com)
* [MIT's Intro to Deep Learning Course](http://introtodeeplearning.com)


[^1]: Mathematicians like to say that functions "map a domain to a range". See [this article](https://www.mathsisfun.com/sets/domain-range-codomain.html) for details.

[^2]: [This article](https://missinglink.ai/guides/neural-network-concepts/7-types-neural-network-activation-functions-right/) has a good overview of some of the most common activation functions and their pros and cons. However, most of the pros and cons people associate with activation functions are math-centric, which may not be easily translatable to "is this a good function to use for my data?" 

[^3]: Activation functions are an active area of research, and people are always exploring new functions to use in neural networks. [This Wikipedia article](https://en.wikipedia.org/wiki/Activation_function#Comparison_of_activation_functions) has a good overview of some recent and popular activation functions.

