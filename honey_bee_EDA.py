#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# load the data
PATH = 'C:/Users/COMMANDCENTER/Desktop/coding/Datasets/Bees/'
df = pd.read_csv(os.path.join(PATH,f'save_the_bees.csv'))

# Create a usable time feature
df['year'] = df['year'].astype(str)
df['quarter'] = df['quarter'].astype(str)
df['time'] = df['year'] + '-' + df['quarter']

# Rename a column
df.rename(columns={'other_pests_and_parasites': 'other_pests'}, inplace=True)

print("Data loaded...")


# In[3]:


# Dropdown widget
dropdown_widget = widgets.Dropdown(
    options=[col for col in df.columns if col not in ['time', 'state', 'state_code', 'year', 'quarter']], 
    description='Select Data:')

# TimeSelector widget
timeselector_widget = widgets.SelectionSlider(
        options=df['time'].unique().tolist(),
        value=df['time'].min(),
        description='Select Time:',
        style={'description_width': 'initial'}, 
        layout={'width': '80%'})

def update_plot(selected_data, selected_time):
    filtered_df = df[df['time'] == selected_time]
    fig = px.choropleth(
        filtered_df,
        locations='state_code',
        locationmode="USA-states",
        color=selected_data,
        color_continuous_scale="Viridis_r",
        scope="usa",
        animation_frame='time')
    fig.show() 

# Put it all together
interactive_widget = widgets.interactive(
    update_plot,
    selected_data=dropdown_widget,
    selected_time=timeselector_widget)

display(interactive_widget)

