from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")
result = sentiment_pipeline("I love how simple and effective Hugging Face pipelines are!")

print(result)
