import streamlit as st
from streamlit_drawable_canvas import st_canvas

import numpy as np
import pandas as pd

from PIL import Image

st.set_page_config(page_title="Handwriting converter",
                   page_icon="✍️",
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items={"Get help": "mailto:jana.wilbert@posteo.de",
                               "Report a bug": "mailto:jana.wilbert@posteo.de",
                               "About": "HI!"})

st.markdown("""# Handwriting converter
    """)

st.markdown("""
Draw on the canvas and convert your handwriting !
""")

# Set a default background color = #eee
bg_color = '#eee'

# Allow refreshing of canvas by change of background color
if st.button("Refresh"):
   bg_color = '#ddd'

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=20,
    #stroke_color=stroke_color,
    background_color=bg_color,
    #background_image=Image.open(bg_image) if bg_image else None,
    #update_streamlit=realtime_update,
    height=250,
    width=250,
    #drawing_mode=drawing_mode,
    #point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    display_toolbar=False,
    key="canvas",
)

# Send canvas image array
st.button("Convert")

# if st.button("Convert"):
    # if canvas_result.image_data is not None:
    # st.image(canvas_result.image_data)

st.text_input("", "placeholder output")
