import gradio as gr



# Define a simple function to be used in the interface
def greet(name):
    return f"Hello, {name}!"

# Create the Gradio interface
iface = gr.Interface(
    fn=greet, 
    inputs="text", 
    outputs="text",
    title="Greeting App",
    description="A simple app that greets the user."
)

# Launch the interface
if __name__ == "__main__":
    iface.launch()
