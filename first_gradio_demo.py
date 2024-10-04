import gradio as gr
def greet(name, intensity):
  return "Hello, " + name + "!" * int(intensity)

# To make the first demo, we create an instance of the gr.Interface class. 
# The Interface class is designed to create demos for machine learning models 
# that accept one or more inputs and return one or more outputs.
#
# Gradio output is shown in http://localhost:7860/
#
# The Interface class has three core arguments:

# - fn: The function to wrap a user interface (UI) around
# - inputs: The Gradio component(s) to use for the input. 
#   The number of components should match the number of arguments in the function.
# - outputs: The Gradio component(s) to use for the output. 
#   The number of components should match the number of return values from the function.
#
# The fn argument is flexible — we can pass any Python function we want to wrap with a UI. 
#
# The input and output arguments take one or more Gradio components.
demo = gr.Interface(
  fn=greet,
  inputs=["text", "slider"],
  outputs=["text"],
)
demo.launch()