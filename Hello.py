# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

def home_page():
    # Add the slide image at the top of the page
    # st.image("Slide1.PNG", use_column_width=True)

    # Add the title of the app
    st.title("- Mushtari Khan, Laila Arzuman Ara")
    st.write("This is the home page of the app.")
    st.markdown("""
Welcome to our interactive dashboard, a dynamic exploration of insights derived from a comprehensive analysis of the original environmental dataset. 
This dashboard serves as a visual gateway to the nuanced patterns and relationships discovered through extensive Exploratory Data Analysis (EDA).
    """)
  
def about_page():
    st.title("About")
    # Add links to datasets
    st.header("Initial Dataset")
    st.markdown("""
The initial dataset captures essential environmental parameters, providing a snapshot of conditions recorded over a series of days. 
The dataset includes information on the number of adult males, mean temperature, and relative humidity for each recorded date.
This raw data offers a foundation for exploring patterns and relationships between adult male presence and climatic factors such as temperature and humidity. 
Each row represents a distinct day, making it a valuable resource for understanding daily fluctuations in environmental conditions.
    """)
    
    # Load your data
    data = pd.read_csv('Project 1.csv')

    # Display the data using a DataFrame widget
    # st.write(data)

    # Add a slider to control the number of rows displayed
    num_rows = st.slider('Select the number of rows to display', min_value=1, max_value=len(data), value=50)
    st.write(data.head(num_rows))

    st.header("Transformed Dataset")
    st.markdown("""
Through a meticulous transformation process, the original dataset has been enriched with additional insights, making it more amenable for in-depth analysis. 
The transformation involves the extraction of meaningful temporal features such as day, month, year, and day of the week from the original date format. 
These extracted features enhance the dataset's interpretability and enable a more granular exploration of patterns over time.
The introduction of categorical features, such as the day of the week and season, further enriches the dataset. 
These additions facilitate a nuanced understanding of how environmental conditions vary across different days and seasons, potentially influencing the presence of adult males. 
Additionally, temperature and humidity have been categorized into levels, providing a structured framework for exploring their impact on adult male presence.

The resulting transformed dataset, with its augmented temporal and categorical features, sets the stage for a more comprehensive analysis. 
It not only retains the core information on adult male presence and climatic conditions but also empowers researchers to delve into nuanced patterns and correlations that may have 
otherwise been obscured in the original data.
    """) 

    # Load your data
    data2 = pd.read_csv('Final_BI_DS.csv')
    df = pd.read_csv('Final_BI_DS.csv')

    # Display the data using a DataFrame widget
    # st.write(data)

    # Add a slider to control the number of rows displayed
    num_rows = st.slider('Select the number of rows to display', min_value=1, max_value=len(data2), value=50)
    st.write(data2.head(num_rows))
    
def insights_page():
    #st.image("Slide3.PNG", use_column_width=True)
    st.title("Insights")
    st.write("This is the insights page of the app.")
      
def code_page():
   # st.image("Slide2.PNG", use_column_width=True)
    st.title("Code")
    st.write("This is the Visualizations page of the app.")

    # Create an interactive histogram with increased space between bins
    fig = px.histogram(df, x='temperature_mean', nbins=20, title='Distribution of Temperature',
                   labels={'temperature_mean': 'Temperature Mean'}, marginal='box')

    # Update the layout to set the gap between bins
    fig.update_layout(bargap=0.1)

    # Show the interactive chart
    fig.show()
    
    
# Create a function to switch pages based on user input
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About", "Insights", "Documentation", "Code"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()
    elif choice == "Insights":
        insights_page()
    elif choice == "Visualizations":
        code_page()

if __name__ == "__main__":
    main()