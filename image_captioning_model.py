# Image Captioning Model interface
#
# we use the BlipProcessor and BlipForConditionalGeneration 
# classes from the transformers q library to set up an image 
# captioning model. 
# This example demonstrates creating a web interface using Gradio, 
# where the input parameter specifies an image and the output is the 
# generated text caption. 
# The title and description parameters enhance the interface 
# by providing context and instructions for users.
import gradio as gr
from transformers import BlipForConditionalGeneration, BlipProcessor
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def generate_caption(image):
    # Directly using the PIL Image object
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs, max_length=30)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def caption_image(image):
    """ 
    Given an image, caption it
    """
    try: 
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"Error: {str(e)} with image: {image}"
    
    iface = gr.Interface(
        fn=caption_image, 
        inputs=gr.Image(type="pil"), 
        outputs=gr.Textbox(),
        title="Image Captioning",
        description="Upload an image and get a caption",
        )
    
    iface.launch()