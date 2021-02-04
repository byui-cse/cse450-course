---
title: Module 04 — Neural Networks, Activation Functions
---

## Activation Functions

The videos mention the _Sigmoid_ activation function. There are lots of different activation functions used in neural networks, and it's an area of active research. 

There are three key things to know about activation functions in the context of neural networks:

### Functions Convert Inputs to Outputs
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

### Activation Functions in Neural Networks

Activation functions are used to determine what the output of a [perceptron](https://developers.google.com/machine-learning/glossary#perceptron) should be.

Different activation functions have different behaviors and side-effects. Some types are better suited to certain problems than others. 

The videos you watched mention the [Sigmoid activation function](https://developers.google.com/machine-learning/glossary#sigmoid_function), which was popular in neural networks for many years.

Currently, the [Rectified Linear Unit (ReLU) activation function](https://developers.google.com/machine-learning/glossary#ReLU) is the most commonly used.[^2]

As with most things in machine learning, the general strategy for choosing the best activation function is to try different variations and measure the results.[^3]


[^1]: Mathematicians like to say that functions "map a domain to a range". See [this article](https://www.mathsisfun.com/sets/domain-range-codomain.html) for details.

[^2]: [This article](https://missinglink.ai/guides/neural-network-concepts/7-types-neural-network-activation-functions-right/) has a good overview of some of the most common activation functions and their pros and cons. However, most of the pros and cons people associate with activation functions are math-centric, which may not be easily translatable to "is this a good function to use for my data?" 

[^3]: Activation functions are an active area of research, and people are always exploring new functions to use in neural networks. [This Wikipedia article](https://en.wikipedia.org/wiki/Activation_function#Comparison_of_activation_functions) has a good overview of some recent and popular activation functions.