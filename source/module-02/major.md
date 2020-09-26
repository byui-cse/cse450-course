---
title: Module 02 — Workplace Makeover, Major Case Study Assignment
---

## Overview

After a few more meetings with the executive team, the head of the data science division has assigned your team to address the following issues:

1. Is there a pay gap based on gender and/or race for similar positions and experience levels?

2. If we put employees into groups based on months of service and the results of the latest satisfaction survey, can we identify what the members of each group have in common? 

	In the case of terminated employees, their months of service would be the time between their start date and their termination date. For active employees, it would be the time between their start date and today.

3. Are we doing a good job on diversity? What's the current makeup of our workforce, and what recruiting efforts are helping us the most in this area?

4. The company spent a lot of money on hiring an outside partner to our Employee Engagement survey (`EngagementSurvey`). William, the VP of Finance thinks that the Employee Engagement survey was worthwhile, but the partner company is owned by his cousin. 

	Cecil, the VP of HR, conducted her own survey as part of an internal HR initiative (`EmpSatisfaction2`), and thinks this was not only cheaper, but better. The CEO wants to know what you think.

## Tips

!!!note "Salary Scale"
	Remember that the `PayRate` column is using two different scales. Hourly employees (production technicians) have their hourly rates listed. Salaried employees (everyone else) have their annual salaries listed. 

	If you're doing any kind of comparison of pay rates, you'll need to convert annual salaries to hourly rates, remembering that salaried employees work 40 hours a week, 52 weeks a year.

!!!note "Feature Scaling"
	If you're going to be comparing different numeric features, be sure they are using the same scale. You may find it useful to use min-max scaling to handle this problem. You could do this calculation manually, or use [Sci-Kit Learn's MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

!!!note "Binning"
	Just as you did with the Titanic dataset when you reduced the number of titles, you may find it useful to "bin" categorical features into discrete groups in order to address some of the questions above. There are multiple ways to do this, but previously we used the [`map()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html).

!!!note "Dealing with Dates" 
	In order to do calculations on dates, you will first need to convert the feature from a string to a DateTime object. The [`to_datetime()` function](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/09_timeseries.html) can help with this.

	Once the feature is a datetime, you can [calculate the number of months between two dates](https://medium.com/@bramtunggala/a-simple-way-to-finding-the-difference-between-two-dates-in-pandas-179d2714b6c).

!!!note "K-Means Clustering"
	Remember, K-Means doesn't work on categorical data. According to the question above, you'll be clustering based on months of service and the results of the most recent Employee Satisfaction survey (`EmpSatisfaction2`).

	The head of the data science reminds you that you'll need to tackle this part in two steps. First, find the optimal number of clusters using the elbow method. Then, cluster the data into that many clusters and try to figure out what the members of each cluster have in common with one another.

!!!note "Visualizations"
	Aside from the visualizations you'll make for the other questions, you will probably want to visualize your clusters in two different ways:

	1. A scatter plot visualization where each point is colored according to its cluster label.
	2. One or more scatter plots where each point is colored according to some feature you think is important to the clustering.

	Alternatively, you could do a single chart where the color is based on cluster label, and the size of the point is based on the feature you think is important to the clustering.

If you need more hints, you might want to [look at this page](hints.html).

## Submission

This case study has two submissions:

1. Your team will work together to create a brief executive summary of your results, showing visualizations and key statistics. You'll use [this template](./summary.docx) for this.

	Your team will have 5 - 7 minutes to present your results to the class. You may use your executive summary for this, or you may prefer to pull out key points and put them in a separate slide show.

2. Following the presentation, each member of your team will also complete and submit a Case Study reflection using [this template]({{URLROOT}}/course/reflection.docx).
