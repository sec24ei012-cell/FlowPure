import streamlit as st
import tensorflow as tf
import numpy as np

# 1. Load your trained AI brain
# Make sure the filename matches exactly what you downloaded from Colab
model = tf.keras.models.load_model('flowpure_brain.h5')

# 2. Design the Website Header
st.set_page_config(page_title="FlowPure AI", layout="centered")
st.title("🌊 FlowPure: STP Efficiency Predictor")
st.write("College Project: Real-time AI Monitoring for Sewage Treatment")

# 3. Create Input Fields for the User
st.sidebar.header("Sensor Inputs")
inlet_cod = st.sidebar.number_input("Inlet COD (mg/L)", min_value=0, value=500)
ph_level = st.sidebar.slider("pH Level", 0.0, 14.0, 7.0)

# 4. The Prediction Logic
if st.button("Run AI Analysis"):
    # Prepare the data for the model (Array format)
    input_data = np.array([[inlet_cod, ph_level]])
    
    # Get the prediction
    prediction = model.predict(input_data)
    efficiency = prediction[0][0]
    
    # 5. Show Results with Color Logic
    st.subheader(f"Predicted Efficiency: {efficiency:.2f}%") 
    
    if efficiency > 80:
        st.success("Status: High Efficiency - System Optimal")
    elif efficiency > 50:
        st.warning("Status: Moderate Efficiency - Check Aeration")
    else:
        st.error("Status: Low Efficiency - Immediate Maintenance Required")
