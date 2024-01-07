from typing import List
import spacy

nlp = spacy.load("en_core_web_sm")
# semantic segmentation: https://spacy.io/usage/linguistic-features#vectors-similarity

def split_sentences(text: str) -> List[str]:
  doc = nlp(text)
  sentences = [sentence.text for sentence in doc.sents]
  return sentences

def group_sentences_semantically(sentences: List[str], threshold: int) -> List[str]:
    docs = [nlp(sentence) for sentence in sentences] 
    # each doc is a tokenization of a sentence
    # we can compare similarity across docs to group them
    assert(len(docs) == len(sentences))
    segments = []

    start_idx = 0
    end_idx = 1

    while end_idx < len(sentences):
        if docs[start_idx].similarity(docs[end_idx]) < threshold:
            segments.append(sentences[start_idx: end_idx])
            start_idx = end_idx
        end_idx += 1
    
    # parse each segment as one text block
    return [" ".join(segment) for segment in segments]

def split_text(text: str) -> List[str]:
  sentences = split_sentences(text)
  similarity_threshold = 0.33
  return group_sentences_semantically(sentences, similarity_threshold)

def create_segments(text):
    semantic_segments = split_text(text)
    return semantic_segments