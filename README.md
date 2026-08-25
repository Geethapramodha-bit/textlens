Day 1 of my NLP Learning Journey — TextLens

I started a structured NLP mini-project series where I’ll build small projects to understand NLP concepts practically before moving toward a larger course-specific NLP system.

For Day 1, I built **TextLens**, a lightweight Python-based text analysis tool.

### What TextLens does

* Performs basic word tokenization
* Normalizes text through lowercasing and punctuation handling
* Counts sentences
* Calculates total and unique words
* Builds a word-frequency dictionary

### Concepts I learned

* Word and sentence tokenization
* Text normalization
* Stopwords
* Stemming vs. lemmatization
* Frequency analysis
* Basic rule-based sentence segmentation

One important takeaway was that NLP preprocessing is **task-dependent**. For example, removing punctuation or stopwords may help one NLP task but can remove useful information for another.

I also explored the limitations of simple rule-based sentence segmentation, such as incorrectly treating the period in abbreviations like “Dr.” as a sentence boundary.

This is just the beginning. I’ll continue building small NLP projects covering classical NLP, information retrieval, embeddings, text classification, and other concepts before combining them into a larger project.

**Tech:** Python | NLP | Text Processing

#NLP #NaturalLanguageProcessing #Python #MachineLearning #AI #LearningInPublic

Day-2 ## StemLab

A mini NLP project that compares different language normalization techniques.

### Features

- Tokenization
- Stemming
- Lemmatization
- POS tagging

### Example

| Word | Stemmed | Lemmatized |
| --- | --- | --- |
| studying | studi | study |
| techniques | techniqu | technique |
| models | model | model |

### Concepts Practiced

- Text normalization
- Porter Stemmer
- WordNet Lemmatizer
- POS tagging

- ## Day 3: RegexLab

A rule-based NLP project for extracting structured information from unstructured text using regular expressions.

### Features

- Email extraction
- Date extraction
- Phone number extraction
- Pattern matching

### Example Input

Contact Geetha at geetha.reddy@gmail.com before 20/08/2026.

Call 9876543210.

### Example Output

Emails:
['geetha.reddy@gmail.com']

Dates:
['20/08/2026']

Phone Numbers:
['9876543210']

### Concepts Practiced

- Regular expressions
- `re.findall()`
- Information extraction
- Pattern matching



## Day 4 – NERLab: Named Entity Recognition

Explored Named Entity Recognition using a pretrained spaCy English NLP pipeline.

### What I learned
- Named Entity Recognition (NER)
- Identifying important entities from text
- Entity labels such as PERSON, ORG, GPE, DATE, etc.
- Using a pretrained NLP model to detect entities automatically

### Example

Input:
"Sundar Pichai visited Hyderabad on 20 August 2026 for Google."

Output:
- Sundar Pichai → PERSON
- Hyderabad → GPE
- 20 August 2026 → DATE
- Google → ORG

### Technologies
- Python
- spaCy
- en_core_web_sm

## Day 5 – VectorLab: Word Embeddings

Explored Word2Vec and how words can be represented numerically as vectors.

### What I learned
- Converting words into numerical vectors
- Vector dimensions
- Training a Word2Vec model
- Finding similar words using `most_similar()`
- Understanding how word relationships can be represented in vector space

### Key Concept

Words appearing in similar contexts can develop similar vector representations.

### Technologies
- Python
- Gensim
- Word2Vec

## Day 6 – ContextLab: Contextual Embeddings

Explored contextual embeddings using a pretrained BERT model.

### What I learned
- BERT tokenization
- Token IDs and attention masks
- 768-dimensional contextual representations
- Same word can have different representations depending on context
- Comparing the word "bank" in different contexts
- Using cosine similarity to compare contextual representations

### Example

"I deposited money in the bank."
→ Financial context

"I sat beside the river bank."
→ Geographical context

### Technologies
- Python
- PyTorch
- Hugging Face Transformers
- BERT
