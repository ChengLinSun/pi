from mpmath import mp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

with st.sidebar:
    number_digits = st.slider("Number of decimal digitals",
                              min_value=1000, max_value=10000,
                              step=1000)
mp.dps = number_digits + 2
pi_digits = mp.pi
pi_digits = str(pi_digits)[2:]
pi_digits_list = [int(x) for x in pi_digits]
pi_digits_array = np.array(pi_digits_list)
counts = np.bincount(pi_digits_array)
fig, ax = plt.subplots()
ax.bar(np.arange(10), counts, tick_label=np.arange(10))

# 添加标签和标题
ax.set_xlabel('value')
ax.set_ylabel('frequency')
ax.set_title('Frequency of occurrence of 0-9 ')
st.pyplot(fig)
