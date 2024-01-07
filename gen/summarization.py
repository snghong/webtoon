# abstractive text summarization module to generate descriptions for panels


# Import necessary modules
import transformers
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

def get_summary(text, length=10):
    # Preprocess the text and encode it as input for the model
    input_text = "summarize: " + text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate a summary
    summary = model.generate(input_ids, max_length=length)
    # Decode the summary
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
    return summary_text


# get emotion
def get_mood(text):
    # Preprocess the text and encode it as input for the model
    input_text = "emotion: " + text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Generate a summary
    summary = model.generate(input_ids, max_length=1)
    # Decode the summary
    summary_text = tokenizer.decode(summary[0], skip_special_tokens=True)
    return summary_text

