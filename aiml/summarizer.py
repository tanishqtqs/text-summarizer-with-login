from transformers import pipeline
import torch

# Check if CUDA is available
device = 0 if torch.cuda.is_available() else -1

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

def summarize_text(text: str) -> str:
    """
    Summarizes the input text and returns the summary.
    :param text: Original content to summarize
    :return: Summarized text
    """
    # Summarize the content
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
