from transformers import pipeline

# Initialize the Hugging Face summarization model
summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    """
    Summarizes the input text and returns the summary.
    :param text: Original content to summarize
    :return: Summarized text
    """
    # Summarize the content
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
