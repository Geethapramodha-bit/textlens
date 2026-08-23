from gensim.models import Word2Vec

sentences = [
    ["dog", "is", "a", "pet"],
    ["cat", "is", "a", "pet"],
    ["dog", "likes", "food"],
    ["cat", "likes", "food"],
    ["puppy", "is", "a", "dog"]
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1
)

print(model.wv["dog"])
print(model.wv.most_similar("dog"))