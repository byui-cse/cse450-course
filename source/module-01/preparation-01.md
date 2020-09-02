---
title: Preparation Reading 01: Introduction
---

## Objectives

In this reading, we'll discuss the definition of terms like "artificial intelligence" and "machine learning". We'll also explore the three main areas of machine learning, and the two most common machine learning tasks.

## Introduction

In the 1980′s, Hans Moravec made the following observation, which came to be known as Moravec’s Paradox:

> ...as the number of demonstrations has mounted, it has become clear that it is comparatively easy to make computers exhibit adult-level performance in solving problems on intelligence tests or playing checkers, and difficult or impossible to give them the skills of a one-year-old when it comes to perception and mobility. [^1]

So, while AI and machine learning algorithms can accomplish many tasks much better than humans can, any toddler can outperform even the most machine learning algorithm in picking out photos of their parents or pet cat. As this XKCD Cartoon illustrates: [^2]

![XKCD Cartoon](https://imgs.xkcd.com/comics/tasks.png)
*[XKCD 1425: Tasks](https://xkcd.com/1425/)*

Even though Moravec wrote about this over thirty years ago, the same sentiment persists in AI research today. In a 2016 interview, Dr. Sean Holden, an AI researcher at Cambridge University, discussed the differences between human intelligence and artificial intelligence:

> Most AI researchers don’t try to solve the whole problem because it’s too hard. They take some specific problem and do it better. That’s not to say that the way humans think isn’t useful to AI, but working out how brains do things is hard. And there’s a difference in scale. Brains are doing things that are in some senses quite different from what AI researchers are currently attacking – I’d be ecstatic, for example, if I could build a robot that could put on a duvet cover. [^3]

Dr. Fumiya Iida, from the Machine Intelligence Lab at Cambridge, adds:

> We have hundreds of thousands of muscles in our body, so how can the brain control this? A computer can’t. Every fraction of a second you have to co-ordinate hundreds of muscles just to grab a cup, for example. [^4]

## Artificial Intelligence vs Machine Learning vs Data Science

There are many different ways the terms *Artificial Intelligence*, *Machine Learning*, and *Data Science* are used in the media.

Scan through a couple of the following articles and look at the definitions provided for these terms. Consider where they agree and disagree. How might the backgrounds and experiences of the authors affect their perceptions?

(There's no need to take notes or memorize these opinions, we'll come up with our own definitions later.)

- [Michael Copeland writing for NVidia](https://blogs.nvidia.com/blog/2016/07/29/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/)
- [Bernard Marr writing for Forbes](https://www.forbes.com/sites/bernardmarr/2016/12/08/what-is-the-difference-between-deep-learning-machine-learning-and-ai/#78654ee526cf)
- [Vincent Granville writing for Data Science Central](http://www.datasciencecentral.com/profiles/blogs/difference-between-machine-learning-data-science-ai-deep-learning)
- [Simply Statistics Blog - The key word in “Data Science” is not Data, it is Science](http://simplystatistics.org/2013/12/12/the-key-word-in-data-science-is-not-data-it-is-science/)

Of particular note is this quote from the Granville article:

> Earlier in my career (circa 1990) I worked on image remote sensing technology, among other things to identify patterns (or shapes or features, for instance lakes) in satellite images and to perform image segmentation: at that time my research was labeled as *computational statistics*, but the people doing the exact same thing in the computer science department next door in my home university, called their research *artificial intelligence*. Today, it would be called *data science* or *artificial intelligence*, the sub-domains being *signal processing*, *computer vision* or *IoT*.

Notice how there's a lot of overlap between these commonly used terms. You might just as easily call this type of work "machine learning". 

There is often a wide gap between how the media, government, and business sectors view a particular technology compared to how it’s viewed by the engineers and scientists using that technology.

### Our Definitions

For this course, we’ll define these terms as follows:

!!! def "Artificial Intelligence"
	The study of man-made “agents” that perceive their environment and take actions that maximize their chances of success at some goal. [^5]

!!! def "Machine Learning"
	A subfield within Artificial Intelligence that gives “computers the ability to learn without being explicitly programmed.” [^6]

!!! def "Data Science"
	The study and use of the techniques, statistics, algorithms, and tools need to extract knowledge and insights from data. [^7]

## The Three Main Areas of Machine Learning

The three main areas of machine learning are *supervised learning*, *unsupervised learning*, and *reinforcement learning*. 

The focus of this course will be supervised learning, which is the most common type of machine learning used in industry. We'll have a little exposure to unsupervised learning, but talk only briefly about reinforcement learning.

### Supervised Learning

![Credit Card Transaction]({{URLROOT}}/shared/img/cc.jpg)
*[Photo by Clay Banks on Unsplash](https://unsplash.com/photos/E2HgkL3LaFE)*

Many credit card companies use supervised learning to develop models that can predict if a particular transaction looks fraudulent. 

They start with a large set of transactions that they've already analyzed for fraud. This is called the *training data*. Each individual transaction in this set is referred to as a *sample* or *instance* of the data.

These transactions will each have a set of interesting attributes, such as the time the transaction occurred, the amount, the location of the purchase, whether or not it was an online or in-person transaction, etc... 

These attributes are referred to by statisticians as *predictors*. Data scientists usually refer to them as *features*.

!!! warning "Synonym Madness"
	
	As we noted in the reading earlier, the concepts and techniques used in machine learning have been around for a long time, and have been developed and refined through work in many different fields. 

	Because of this, there are many terms like "predictors" and "features" that came from different fields, but which mean the same thing and are sometimes used interchangeably.

Since these are historic transactions, one of the attributes will be whether or not the credit card company determined they were fraudulent. Since this is the attribute we're trying to predict in future transactions, it is referred to as the *response variable* (by statisticians) or as the *target* (by data scientists).

With that background, we can now define supervised learning this way:

!!! def "Supervised Learning"

	Supervised learning algorithms use *labeled* training data, (data that starts with known values for the target variable) to generate models that relate the features to the target. 

	The purpose of these models is to accurately predict the response for future observations (prediction) or to help us better understand the relationship between the response and the predictors (inference). 

As you'll see throughout this course, the accuracy and usefulness of these models will depend on a number of factors.

### Unsupervised Learning
![Grocery Shopping]({{URLROOT}}/shared/img/grocery.jpg)
*[Photo by nrd on Unsplash](https://unsplash.com/photos/D6Tu_L3chLE)*

A grocery store chain might wish to decide which customers to target for a particular sales promotion. Historic shopping data can be analyzed using a technique known as *cluster analysis* to determine which groups of customers would be most likely to respond to a particular ad campaign.

A geneticist tracking measuring how a plant cell responds to drought conditions might take measurements of tens of thousands of proteins every few seconds. With that many features to analyze, it can be difficult to find any kind of useful pattern. A technique known as *dimensional reduction* can aggregate the features into groups based on their response patterns, reducing the number of features that need to be analyzed.

Cluster analysis and dimensional reduction are examples of unsupervised learning.

!!! def "Unsupervised Learning"
	Unsupervised learning algorithms generate models that allow us to identify patterns in unlabeled training data, make inferences about those patterns, and predict where future data might fall within those patterns. 

### Reinforcement Learning
![Robot]({{URLROOT}}/shared/img/robot.jpg)
*[Photo by Lenin Estrada on Unsplash](https://unsplash.com/photos/OI1ToozsKBw)*

Reinforcement learning is what most people think of when they think of artificial intelligence. 

!!! def "Reinforcement Learning"
	Reinforcement learning is an iterative process where an algorithm seeks to maximize some value based on rewards received for being right. [^8]

Reinforcement learning is used in robotics development to train robots to respond to varying environmental factors in order to achieve a goal. 

## Supervised Machine Learning Tasks

Most problems addressed by supervised machine learning can be divided into two groups, regression and classification.

!!! def "Regression"

	The process of generating a model that can be used to predict a numerical value along a continuous range.

Examples of regression problems are predicting the likelihood that someone will contract a disease based on epidemiological data, calculating the value of a house based on its features and current market trends, or predicting a student's most likely GPA based on their ACT scores.

!!! def "Classification"

	The process of generating a model that can be used to predict a particular value from a set of discrete choices.

Examples of classification problems include facial recognition software, systems that decide whether a customer should be given a loan, tests to determine if someone has a particular illness, and optical character recognition systems.

!!! warning "Regression vs Classification"

	While there are some algorithms that are designed to be used in regression or classification scenarios, most can be used in either one. In addition, with a few modifications to the problem statement, many classification problems can be restated as regression problems and vice versa.

	Depending on how the final model is going to be used, one approach might make more sense than another. As you'll soon realize is the case for many aspects of machine learning, the right approach will depend on many factors.

[^1]: [Mind Children, by Hans Moravec (Harvard University Press, 1988)](http://www.hup.harvard.edu/catalog.php?isbn=9780674576186&content=reviews)

[^2]: [XKCD 1425: Tasks](https://xkcd.com/1425/)

[^3]: [Cambridge Alumni Magazine, Issue 79, pg 19](https://www.alumni.cam.ac.uk/magazine/cam-79)

[^4]: [Cambridge Alumni Magazine, Issue 79, pg 19](https://www.alumni.cam.ac.uk/magazine/cam-79)

[^5]: [Artificial Intelligence: A Modern Approach by Russell and Norvig (Prentice Hall, 2009)](http://aima.cs.berkeley.edu/)

[^6]: [Some Studies in Machine Learning Using the Game of Checkers, by Arthur L. Samuel (IBM Journal, Vol 3, No 3, 1959)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.368.2254&rep=rep1&type=pdf)

[^7]: [Wikipedia article on Data Science](https://en.wikipedia.org/wiki/Data_science)

[^8]: [Reinforcement Learning](https://www.sciencedirect.com/topics/neuroscience/reinforcement-learning)
