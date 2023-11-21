
Self Attention (Attention Map)
	• Illustrates attention weights between each word and every other word
		○ Here, the word "book" is strongly connected (pay attention) to "teacher" and "student"
	• The model can learn attention this way, significantly imp


The model works with numbers, not actual words, so for the input
	• First, tokenize the word (Converts words to number)
		○ Each number representing a position in a dictionary of all the possible words that the model can work with
		○ Must be same tokenizer for generating text as the tokenizer when training


Embedding Layer
	• It is a trainable vector embedding space, a high-dimensional space where each token is represented as a vector and occupies a unique location within that space.
	• The intuition is that these vectors learn to encode the meaning and context of individual tokens in the input sequence


Positional Encoding
	• As adding the token vectors to the base of Encoder and Decoder
		○ Add Positional Encoding (Model proccess the token vectors in parallel)
		○ It preserve the "word position in the sentence" info


Self-attention Layer
	• Model analyzes the relationships between the tokens in your input sequence
	• The self-attention weights that are learned during training and stored in these layers reflect the importance of each word in that input sequence to all other words in the sequence. 


Encoder and Decoder (fully-connected feed forward network)
	• All the attention weights are proccessed through fully-connected feed forward network
	• The output of this layer is a vector of logits proportional to the probability score for each and every token in the tokenizer dictionary.


Softmax Layer
	• These vector of logits are passed to a final SoftMax layer
		○ Normalized into a probability score for each word. 
		○ This output includes a probability for every single word in the vocabulary, so there's likely to be thousands of scores here. 
	• One single token will have a score higher than the rest. This is the most likely predicted token



Can choose different tokenization method
For example
	1. Token IDs matching complete words
	2. Token IDs represents parts of words

Each token is mapped to a vector
	• In the original transformer paper, the vector size is 512

For example, a vector size of 3
	• Plot the words in to 3D space, to see the relationships between words
	• Distance between words (angle) allows model to mathematically understand words



Multi-headed Self-attention
	• Multiple sets of self-attention weights or heads are learned in parallel independently
	• Number of attention heads varies in different model, commonly in range 12 -100
	• The intuition here is that each self-attention head will learn a different aspect of language
		○ For example, one head may see the relationship between the people entities in our sentence. Whilst another head may focus on the activity of the sentence. 
	• The weights of each head are randomly initialized and given sufficient training data and time, each will learn different aspects of language.



Autoencoding models build bidirectional representations of the input sequence
	• Model understand the full context of the token, not just the word comes before

Good use case 
(ideally tasks that benefit by bidirectional context)
	• Sentiment analysis
	• Named entity recognition (extract information from text)
	• Word classification
Example model
	• BERT
	• ROBERTA

token in the sequence is randomly masked

denoising objective

predicting the next token is sometimes called  full language modeling by researchers



In training
	• The model has no knowledge of the end of the sentence (unidirectional context)
	• It masks the input sequence and can only see the input tokens leading up to the token in question
	• It then iterates over the input sequence one by one to predict the following token.
	• It learns to predict the next token from a vast number of examples, the model builds up a statistical representation of language.

Good use case
	• Text generation
	• Other emergent behavior (unseen situation)
		○ Larger decoder-only models also show strong zero shot inference abilities

Example model
	• GPT
	• BLOOM
		

 base on previous sequence of tokens


Good use case
( generally useful in cases where you have a body of texts as both input and output)
	• Translation
	• Text summarization
	• Question answering

Example models
	• T5
	• BART

masks random sequences of input tokens

then replaced by unique sentinel token that don't correspond to any word
