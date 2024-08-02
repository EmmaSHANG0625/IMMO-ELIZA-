import streamlit as st
import joblib
import numpy as np

# Load trained model 
model_path = 'Random_Forest_model.joblib'
model = joblib.load(model_path)

# Define the function to make predictions
def predict_price(input_features):
    # Make sure the input_features are in the correct shape
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

# Streamlit app layout
st.title("IMMO ELIZA - BELGIUM")
st.header("House Price Prediction App")

# Collecting user inputs for the features
#district selection 
#district selection 
districts = ['Aalst', 'Antwerp', 'Arlon', 'Ath', 'Bastogne',   
             'Bruge', 'Brugge', 'Brussels', 'Charleroi', 'Dendermonde',  
             'Diksmuide', 'Dinant', 'Eeklo', 'Gent', 'Halle-Vilvoorde',    
             'Hasselt', 'Huy', 'Ieper', 'Kortrijk', 'Leuven',    
             'Liège', 'Maaseik', 'Marche-en-Famenne', 'Mechelen', 'Mons',     
             'Mouscron', 'Namur', 'Neufchâteau', 'Nivelles', 'Oostend',    
             'Oudenaarde', 'Philippeville', 'Roeselare', 'Sint-Niklaas', 'Soignies', 
             'Thuin', 'Tielt','Tongeren',  'Tournai', 
             'Turnhout', 'Verviers', 'Veurne', 'Virton', 'Waremme']
selected_district = st.selectbox("District", districts)

# One-hot encode the selected district
district_one_hot = [1 if district == selected_district else 0 for district in districts]
#Property type selection
property_types = ["House", "Apartment"]
property_type = st.selectbox("Type of Property", property_types)

# One-hot encode the property type
if property_type == "House":
    type_of_property_house = 1
    type_of_property_appartment = 0
else:
    type_of_property_house = 0
    type_of_property_appartment = 1



bedroom_count = st.number_input("Number of Bedrooms", min_value=1, max_value=50)
bathroom_count = st.number_input("Number of Bathroom", min_value=1, max_value=10)
room_count = st.number_input("Number of Rooms", min_value=1, max_value=100)
construction_year = st.number_input("Construction Year", min_value=1850, max_value=2035)

living_area = st.number_input("Living Area (m2)", min_value=0.00)
surface_of_plot = st.number_input("Plot Area (m2)", min_value=0.00)

number_of_facades = st.slider("Number of Facades", 1, 4)
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(number_of_facades))

#PEB
select_values = [1,2,3,4,5,6,7,8,9]
select_strings = ["G", "F", "E", "D", "C", "B", "A", "A+", "A++"]

def stringify(i: int) -> str:
    if i > 0 and i <= len(select_strings):
        return select_strings[i-1]
    return "Invalid Selection"

PEB_grade = st.selectbox(
    "PEB Grade",
    options=select_values,
    index=5,  # Use `index` instead of `value` for default selection
    format_func=stringify)

#building state
select_values_2 = [1,2,3,4,5,6]
select_strings_2 = ["TO RESTORE", "TO RENOVATE", "TO BE DONE UP", "GOOD", "JUST RENOVATED", "AS NEW"]

def stringify(i: int) -> str:
    if i > 0 and i <= len(select_strings_2):
        return select_strings_2[i-1]
    return "Invalid Selection"

Building_state_grade = st.selectbox(
    "State of Building",
    options=select_values_2,
    index=3,  
    format_func=stringify)

#garden
select_values_3 = [0, 1]
select_strings_3 = ["No", "Yes"]

def stringify(i: int) -> str:
    if i == 0 or i <= len(select_strings_3):
        return select_strings_3[i]
    
garden = st.selectbox(
    "Garden",
    options=select_values_3,
    index=0,  
    format_func=stringify)

#swimming pool
select_values_4 = [0, 1]
select_strings_4 = ["No", "Yes"]

def stringify(i: int) -> str:
    if i == 0 or i <= len(select_strings_4):
        return select_strings_4[i]
    
swimming_pool = st.selectbox(
    "Swimming Pool",
    options=select_values_4,
    index=0,  
    format_func=stringify)



# Store the inputs in a list
user_inputs = [bathroom_count, bedroom_count, construction_year, garden, living_area, number_of_facades, room_count,
                surface_of_plot, swimming_pool, PEB_grade, Building_state_grade, type_of_property_appartment, type_of_property_house]+ district_one_hot

# Predict button
if st.button("Predict House Price"):
    predicted_price = predict_price(user_inputs)
    st.write(f"The predicted price of the house is: €{predicted_price:,.2f}")



