import streamlit as st
#from streamlit_option_menu import option_menu
import json
import pickle
import numpy as np

# Function to load JSON data from a file

with open("columns.json", 'r') as f:
    data=json.load(f)

# Set title page
st.set_page_config(page_title="My App", layout="wide")

st.image("header.jpg", use_column_width=True )
st.title("Welcome to My Web")
 
selected_location = st.selectbox(
    'Select desired location:',
    data['data_columns'][3:],
)



def predict_price(location,sqft,bath,bhk):
    loc_index=np.where(np.array(data["data_columns"])==selected_location)[0][0]

    x=np.zeros(len(data['data_columns']))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    print(x)

    return model.predict([x])[0]

area=st.text_input("Enter the area of the house (in square feet)", value="2000")
bedrooms_bhk=st.text_input("Enter the number of BHK/ bedrooms", value="3")
bathrooms=st.text_input("Enter the numbers of bathrooms", value="2")

# Load Pre-Trained Model
with open('home_prices_model.pickle', 'rb') as f:
    model=pickle.load(f)


# Value picker function

if st.button("Start Prediction", type="secondary"):
    
    try:
        area=float(area)
    except ValueError:
        st.warning("Please enter valid numbers for area inputs")

    try:
        bedrooms=int(bedrooms_bhk)
    except ValueError:
        st.warning("Please enter valid numbers for bedrooms inputs")
    
    try:
        bathrooms=int(bathrooms)
    except ValueError:
        st.warning("Please enter valid numbers for bathrooms inputs")


    # For Model try and execpt check

    try:
        predicted_price=predict_price(selected_location, area, bathrooms, bedrooms_bhk)
        st.title(selected_location)
        st.success(str(round(predicted_price,3))+" (IND Lakh)")
    except Exception as e:
        st.warning("Problem in Model")
        st.write(e)
    