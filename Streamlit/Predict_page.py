import streamlit as st
import numpy as np
import pickle

def load_model():
    file_name = r"C:\Users\shounak lohokare\Desktop\Python Basics\Credit_Card_Fraud\Flask_API\model_XGBC.p"
    with open(file_name, "rb") as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model
def Load_Dictionary():
    with open('Dicts\Cities.pkl', 'rb') as f:
        cities = pickle.load(f)

    with open('Dicts\States.pkl', 'rb') as f:
        states = pickle.load(f)
        
    with open('Dicts\Merchants.pkl', 'rb') as f:
        merchants = pickle.load(f)

    with open('Dicts\Jobs.pkl', 'rb') as f:
        jobs = pickle.load(f)
        
    with open('Dicts\Days.pkl', 'rb') as f:
        days = pickle.load(f)

    with open('Dicts\Category.pkl', 'rb') as f:
        category = pickle.load(f)
    return cities, states, merchants, jobs, days, category

cities, states, merchants, jobs, days, categories = Load_Dictionary()

def Predict_Page():

    
    st.title("Predict Fraud Transaction")

    st.write("""
            ### We Need Some Information to Predict the Fraud
            """)
    

    state = st.selectbox("State", tuple(states.keys()))

    city = st.selectbox("City", tuple(cities.keys()))

    merchant = st.selectbox("Merchant", tuple(merchants.keys()))

    job = st.selectbox("Job", tuple(jobs.keys()))

    day = st.selectbox("Day", tuple(days.keys()))

    category = st.selectbox("Category", tuple(categories.keys()))

    city = cities[city]

    state = states[state]

    day = days[day]

    job = jobs[job]

    merchant = merchants[merchant]

    category = categories[category]

    Age = int(st.text_input("Age", value = "0"))

    Hour = int(st.text_input("Hour of Transaction Time",value = "0"))

    Distance = float(st.text_input("Distance Between Merchant and Buyer", value = "0"))

    Fraud_amt = float(st.text_input("Enter Fraud Amount", value = "-1"))

    Legit_amt = float(st.text_input("Enter Non Fraud Amount", value = "-1"))


    if Age > 0 and Hour >= 0 and Distance >= 0 and Fraud_amt > -1 and Legit_amt > -1:
        model = load_model()

        Data = np.array([int(Hour) ,state ,merchant, int(Age), day
                        , job, category, float(Fraud_amt) + float(Legit_amt), float(Distance), float(Fraud_amt), float(Legit_amt), float(Fraud_amt)]).reshape(-1, 1).astype(np.float).transpose()


        preds = model.predict(Data).tolist()

        if preds[0] == 1:
            st.write("""
                    ### Transaction is Fraud :((
                    """)
        else:
            st.write("""
                    ### Transaction is Legit :D
                    """)