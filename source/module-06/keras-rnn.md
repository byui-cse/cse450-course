---
title: Module 06 — Recurrent Neural Networks, Keras
body-class: index-page
---

## Recurrent Neural Networks with Keras

We'll be using Keras for creating recurrent neural networks. Much of what you learned in Module's 04 and 05 will be applicable to this module. 

Before class on Monday, read [through the Colab notebook](https://colab.research.google.com/github/byui-cse/cse450-course/blob/master/notebooks/starter_publishing.ipynb) that contains the starter code for this module and make sure you have a pretty decent understanding of all of the steps involved. 

You don't have to fully understand every line of code, but you should read the comments and most of the linked articles carefully enough to be able to discuss it with your team. 

There's a lot of new TensorFlow code being used in the starter code. You may find it useful to look up what those functions do in the TensorFlow documentation.

The starter code is based on an updated and simplified version of [this TensorFlow tutorial](https://www.tensorflow.org/tutorials/text/text_generation), which is also worth reviewing.

### Above and Beyond / Advanced RNN Tutorials

If you feel like you fully understand the starter code and have your RNN in a place where you're getting good results, you might be interested in some of these more advanced RNN techniques.

* You could modify the model to use [Curriculum Learning](https://www.tensorflow.org/tutorials/text/text_generation#advanced_customized_training).

* The current model uses a character-based model rather than a word-based model. You could try to implement [Word Embedding](https://www.tensorflow.org/tutorials/text/word_embeddings) using [Word2Vec](https://www.tensorflow.org/tutorials/text/word2vec).

* You could also attempt to incorporate [a weighted attention mechanism](https://www.tensorflow.org/tutorials/text/nmt_with_attention) to cause the model to pay more attention to certain parts of the text. More details [can be found here](https://github.com/tensorflow/nmt#background-on-the-attention-mechanism).
