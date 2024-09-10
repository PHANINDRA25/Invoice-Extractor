
 #load all environment variables from .env

#import streamlit as st
import os
from PIL import Image #python imaging library - used to manipulate images
import google.generativeai as genai
#import Pillow
#configuring api key
genai.configure(api_key='AIzaSyADmO5bWRKb175B-6jeV2mkrL5qECdcT78')

def get_gemini_response(input_text,  prompt):
    try:
        # Assuming genai is a library and GenerativeModel can load models by name
        model = genai.GenerativeModel('gemini-pro')
        
        # Assuming generate_content can take a list with text and image data
        response = model.generate_content([input_text, prompt])
        
        # Return the textual part of the response if available
        return response.text
    except Exception as e:
        # Handle exceptions that might occur during model loading or content generation
        print(f"An error occurred: {e}")
        return None

def input_image_setup(uploaded_file):
    if uploaded_file is not None :

        #Read the file image into bytes
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                'mime_type':uploaded_file.type,
                'data':bytes_data
            }
        ]

    else:
        raise FileNotFoundError('No file uploaded')
    

text_input = "What is the capital of India?"
#



input_prompt="""
You are a Geography teacher . Answer the questions

"""

#image_data=input_image_setup(uploaded_file)
response=get_gemini_response(text_input,input_prompt)
print(response)
