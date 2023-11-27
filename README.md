





3 main classes of PEFT




Not enough memory

PEFT is less prone to catastrophic forgetting

With PEFT, you train only a small number of weights, which results in a much smaller footprint overall, as small as megabytes depending on the task. 

Same size

Different PEFT method
	• each has  trade-offs

train only certain components of the model or specific layers, or even individual parameter types. 

Researchers have found that the performance of these methods is mixed and there are significant trade-offs between parameter efficiency and compute efficiency. 

work with the original LLM parameters, but reduce the number of parameters to train by creating new low rank transformations of the original network weights.

 keep all of the original LLM weights frozen and introduce new trainable components.

2 methods
	• Adapter
		○ Add new trainable layers to the architecture of the model
		○ Typically inside the encoder or decoder components after the attention or feed-forward layers
	• Soft Prompts
		○ Keep the model architecture fixed and frozen
		○ Focus on manipulating the input to achieve better performance. This can be done by adding trainable parameters to the prompt embeddings or keeping the input fixed and retraining the embedding weights.
		
QLoRA:
	• Combine LoRA with the quantization techniques














There are 2 types of Neural Networks (Learn when train)
	• Self-attention (majority of the learnable weights)
	• Feed forward network

inject a pair of rank decomposition matrices alongside the original weights
	• The products has the same dimensions as the original weights
	
	
	

Because this model has the same number of parameters as the original, there is little to no impact on inference latency. 

Researchers have found that applying LoRA to just the self-attention layers of the model is often enough to fine-tune for a task and achieve performance gains. 
However, in principle, you can also use LoRA on other components like the feed-forward layers. But since most of the parameters of LLMs are in the attention layers, you get the biggest savings in trainable parameters by applying LoRA to these weights matrices. 

Example

	1. take the LoRA matrices you trained for this task
	2. calculate their product
	3. then add this matrix to the original weights and update the model

still an active area of research

The takeaway here is that ranks in the range of 4-32 can provide you with a good trade-off between reducing trainable parameters and preserving performance.














Soft Prompts are not fixed
	• Can think of them as virtual tokens
	• Through supervised learning, the model learns the values for these virtual tokens that maximize performance for a given task


Natural language tokens have fixed location in vector space

	1. Train a set of soft prompts for one task and a different set for another
	2. Prepend your input prompt with the learned tokens
	3. To another task, you simply change the soft prompt

One potential issue to consider
is the interpretability of learned virtual tokens

because the soft prompt tokens can take any value within the continuous embedding vector space. 
The trained tokens don't correspond to any known token, word, or phrase in the vocabulary of the LLM. 


However, an analysis of the nearest neighbor tokens to the soft prompt location shows that they form tight semantic clusters. 

In other words, the words closest to the soft prompt tokens have similar meanings. 

The words identified usually have some meaning related to the task, suggesting that the prompts are learning word like representations. 
