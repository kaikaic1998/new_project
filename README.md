New on-going project

Content
	1. Initialize FLAN-T5 model
	2. Load dataset
	3. Inference without prompt
	4. Zero shot inference
	5. Zero shot inference (different prompt)
	6. One shot inference
	7. Few shot inference
	8. Try with different LLM config

Goal: Test out FLAN-T5's ability to summarize dialogues

Install library


Import Hugging Face LLM libraries


Load the DialogSum
	• Dialogues dataset from the DialogSum Hugging face dataset
	• This dataset contains 10000+ dialogues with corresponding manually labeled summaries and topics


Print a couple of dialogues with their baseline summaries


Load the FLAN-T5 model, creating an instance of the AutoModelForSeqLM class with the .from_pretrained() method
	• It is a good generalized model that can perform many tasks


Initialize the tokenizer for the FLAN-T5 
	• Parameter use_fast switches on the fast tokenizer
	• Tokenizer converts words into vector space that can be processed by the model


Take a look at the tokenizer's encoding and decoding


Test the base LLM to summarize a dialogue without any prompting 
(feed the dialogue without any instruction)
	• The model is not sure what task is supposed to accomplish


Next, try Zero Shot Inference with an instruction prompt
	• To instruct the model to do a task, this case --> summarize a dialogue
		○ Can convert the dialogue to an instruction prompt, wrapping the dialogue in a descriptive instruction



Label vs Generation
--> Very different

It is better
but still did not pick up the nuance of the conversation
