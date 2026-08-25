from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sentence1 = "I deposited money in the bank."
sentence2 = "I sat beside the river bank."

tokens1 = tokenizer(sentence1, return_tensors="pt")
tokens2 = tokenizer(sentence2, return_tensors="pt")

with torch.no_grad():
    output1 = model(**tokens1)
    output2 = model(**tokens2)

print(output1.last_hidden_state.shape)
print(output2.last_hidden_state.shape)
tokens1_list = tokenizer.convert_ids_to_tokens(tokens1["input_ids"][0])
tokens2_list = tokenizer.convert_ids_to_tokens(tokens2["input_ids"][0])

print(tokens1_list)
print(tokens2_list)
bank_vector1 = output1.last_hidden_state[0, 6, :]
bank_vector2 = output2.last_hidden_state[0, 6, :]
print(bank_vector1)
print(bank_vector2)
import torch.nn.functional as F

similarity = F.cosine_similarity(
    bank_vector1.unsqueeze(0),
    bank_vector2.unsqueeze(0)
)

print("Cosine Similarity:", similarity.item())