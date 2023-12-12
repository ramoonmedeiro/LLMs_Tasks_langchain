import streamlit as st
import openai
from wrapper import ModelWrapper

st.set_page_config(page_title='Youtube Script Generator', page_icon='📜')
st.title("Generate Script for Youtube Video")

with st.sidebar:
    openai_api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai_api_key.startswith('sk-') and len(openai_api_key) == 51):
        st.warning('Please enter your OPENAI API KEY!', icon='⚠️')
    else:
        st.success('OPENAI API KEY provided', icon='🎉')

    temperature = st.slider(
        label='Temperature',
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )


topic = st.text_input('Enter a topic:', value='')
if st.button("Search") and topic != "":
    #try:
    model = ModelWrapper(
        openai_api_key=openai_api_key,
        temperature=temperature,
        topic=topic
    )

    st.write(model.wrapper())
    #except openai.RateLimitError:
    #    st.error('Error: Rate limit exceeded. Please try again later.', icon='⚠️')
    #except Exception as e:
    #    st.error(f'Error: {e}', icon='⚠️')
