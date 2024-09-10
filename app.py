# #invoice extractor



import os
from dotenv import load_dotenv

load_dotenv() # will search for .env file in local folder and load variables 

KEY_VAR = os.getenv('GOOGLE_API_KEY')
print(KEY_VAR)

import streamlit as st
import os
from PIL import Image #python imaging library - used to manipulate images
import google.generativeai as genai

#configuring api key
#os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=KEY_VAR)

#genai.configure(api_key='AIzaSyAKDFHnioTr_OpX9jyuqbdDOc1X6Tw6nvk')

#Function to load gemini pro vision model and get response

def get_gemini_response(input,image,prompt):
    # loading the model
    try:
        model=genai.GenerativeModel('gemini-1.5-flash')
        response=model.generate_content([input,image[0],prompt])  #images are laoded as list
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
        return image_parts

    else:
        raise FileNotFoundError('No file uploaded')

#initilize our streamlit app

#st.set_config(page_title='Invoice Extractor')
st.header('Gemini Application')
input=st.text_input('Input prompt: ',key='input')
uploaded_file=st.file_uploader('choose an image...',type=['jpeg','jpg','png'])
image=''
if uploaded_file is not None :
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded image.',use_column_width=True)  #display the file here

submit=st.button('Tell me about the invoice')

input_prompt="""
You are an expert in understanding invoices. you will receive input images as invoices
 and you will have to answer questions based on the input image

"""

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input,image_data,input_prompt)

    st.subheader('The response is ')
    st.write(response)






