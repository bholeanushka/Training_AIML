# from transformers import pipeline
#
# classifier = pipeline("sentiment-analysis")
#
# text = "I really love this movie! It was fantastic."
# result = classifier(text)
#
# print(result)
# ------------------------------------------
# Aesthetic Sentiment Analysis Web App
# Using Hugging Face + Gradio
# ------------------------------------------

from transformers import pipeline
import gradio as gr

# Load pre-trained sentiment model
classifier = pipeline("sentiment-analysis")

# Define prediction function
def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text.", None

    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    # Make the result more aesthetic and readable
    emoji = "😊" if label == "POSITIVE" else "😞"
    styled_label = f"{emoji} {label} ({score:.2%} confidence)"
    return styled_label, f"The model is {score:.2%} confident this text is {label.lower()}."

# Create custom CSS for aesthetics
custom_css = """
body {
    background-color: #f7f8fc;
}
.gradio-container {
    font-family: 'Poppins', sans-serif;
    color: #333;
}
h1 {
    text-align: center;
    color: #222;
    font-weight: 600;
    margin-bottom: 10px;
}
"""

# Build Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Type your sentence here...",
        label="Enter text to analyze sentiment"
    ),
    outputs=[
        gr.Textbox(label="Predicted Sentiment", show_label=True),
        gr.Textbox(label="Model Confidence", show_label=False)
    ],
    title="🧠 Sentiment Analyzer",
    description="Enter any sentence below to find out if it's positive or negative using a Hugging Face Transformer model.",
    theme="soft",
    css=custom_css,
    examples=[
        ["I absolutely loved this movie!"],
        ["The food was cold and tasteless."],
        ["It’s an average product, not too bad."],
    ]
)

# Launch the web app
demo.launch()

