

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
