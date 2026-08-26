from transformers import AutoTokenizer, AutoModel
import torch

# Load pretrained BERT tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "The animal did not cross the street because it was tired."

# Convert sentence into tokens
tokens = tokenizer(sentence, return_tensors="pt")

# Get BERT representations
with torch.no_grad():
    outputs = model(**tokens)

# Get the final hidden states
embeddings = outputs.last_hidden_state

# Display tokens
token_list = tokenizer.convert_ids_to_tokens(tokens["input_ids"][0])

print("Tokens:")
print(token_list)

print("\nEmbedding Shape:")
print(embeddings.shape)

# Show the contextual representation of each token
print("\nToken Embeddings:")

for i, token in enumerate(token_list):
    print(token, "->", embeddings[0, i, :5].numpy())

# Calculate similarity between two token representations
token1 = embeddings[0, 2, :]
token2 = embeddings[0, 3, :]

similarity = torch.nn.functional.cosine_similarity(
    token1.unsqueeze(0),
    token2.unsqueeze(0)
)

print("\nCosine Similarity:")
print(similarity.item())