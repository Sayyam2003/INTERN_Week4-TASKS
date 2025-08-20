#Text analyzer character  count app using gradio.
import gradio as gr

# Function to analyze text
def analyze_text(text):
    char_count = len(text)
    word_count = len(text.split())
    return f"Characters: {char_count}\nWords: {word_count}"

# Gradio interface
iface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(lines=5, placeholder="Enter your text here..."),
    outputs="text",
    title="📝 Text Analyzer - Character & Word Count",
    description="This app counts the number of characters and words in the given text input."
)

# Launch the app
iface.launch()
