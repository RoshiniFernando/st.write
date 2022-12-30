# This file shows some uses of st.write function
# Important libraries
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Add an image using URL 
st.image(
            "https://images.unsplash.com/photo-1615127717889-8945dba1f05a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2670&q=80",
            width=400, # Manually Adjust the width of the image as per requirement
        )

st.write('''
 _st.write is the Swiss Army knife of Streamlit commands_.
''')

# Example 1
st.write('''
### Display Text and Markdown-formatted text
''')
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.write('''
### Display Numbers
''')
st.write(1234)

# Example 3
st.write('''
### Display DataFrame
''')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4
st.write('''
### Pass multiple Arguments to st.write
''')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
st.write('''
### Display Charts
''')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)