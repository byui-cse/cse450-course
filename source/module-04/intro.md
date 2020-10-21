---
title: Module 04 — Hit Songs, Case Study Introduction
---

![Meeting]({{URLROOT}}/shared/img/song.jpg)
*[Photo by Austin Neill on Unsplash](https://unsplash.com/photos/hgO1wFPXl3I)*

## Introduction
You've been hired by a major record label, MMC Entertainment, to help them build a model that can predict whether or not a song will be a hit.

## Stakeholders

These are the individuals your team will be helping during the case study:

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/ezra.jpg">
	<h5>Ezra, Lead Singer of the Wasps</h5>
	<blockquote><p>I don't need some computer telling me how to make my art.</p><p>But, it could be interesting to incorporate some synthetic components into one of my songs...just as an experiment.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/tom.jpg">
	<h5>Tom Jones, Head of marketing and brand development</h5>
	<blockquote><p>While we all celebrate the art behind your music Ezra, our research over the years tells us that there are several factors that go into predicting whether or not a song will be a hit.</p><p>Some of that comes down to timing, but we think there may be other aspects that we can quantify.</p></blockquote>
</div>

<div class="dialogue">
	<img src="{{URLROOT}}/shared/img/johnny.jpg">
	<h5>Johnny, Data Science Intern</h5>
	<blockquote><p>Hey! You're here too! I just started working here last week.</p>
		<p>The record company has a ton of information on old songs, including how popular they were. I suggest we start there.</p></blockquote>
</div>

!!!note "Stakeholder Focus Areas"
	The stakeholders are particularly interested in the following areas:

	1.	Building a model that can predict how popular a song is.
	2.  Understanding how tastes have changed over time, and if there are cycles in those tastes.

You've been invited to a strategy meeting tomorrow. They're planning to discuss the marketing campaign and would like your input on a few key points.

## Data
Spend some time with your team evaluating the data. Be sure to look at data types, ranges, and meanings of each feature from the [data dictionary](./bank-dictionary.txt).

### Datasets
* [Spotify Data](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/spotify/data.csv)
* [Spotify Data (by Artist)](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/spotify/data_by_artist.csv)
* [Spotify Data (by Artist with genres)](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/spotify/data_by_artist_w_genres.csv)
* [Spotify Data (by Genre)](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/spotify/data_by_genres.csv)
* [Spotify Data (by Year)](https://raw.githubusercontent.com/byui-cse/cse450-course/master/data/spotify/data_by_year.csv)

You can use the following Google Colab notebook to assist you:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/Module_04.ipynb)

[^1]: [Lead Singer photo by Brian Lundquist on Unsplash](https://unsplash.com/photos/3Uf-aRahKcc)

[^2]: [Head of Marketing photo by LinkedIn Sales Navigator on Unsplash](https://unsplash.com/photos/pAtA8xe_iVM)

[^3]: [Data Science Intern photo by Fábio Lucas on Unsplash](https://unsplash.com/photos/iczrMDNuvzkml-pxK0Ovmw)