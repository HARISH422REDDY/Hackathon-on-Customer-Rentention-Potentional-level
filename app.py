import pickle
import streamlit as st 
import sklearn


pickle_in = open("C:/Users/user/OneDrive/Desktop/Streamlit/classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def    customer_retential_potential_prediction(OnlineCommunication,AutomaticRefill,DoorstepDelivery,
       Welcome_email_opened,No_of_customized_email,
       No_of_customized_email_opened,No_of_customized_email_clicked,
       TotalOrderQuantity,OrderFrequency,Average_Ordergap,
       no_of_BusinessDays,year_reg,month_reg,day_reg,PreferredDeliveryDay_num,City_CITY2,
       City_CITY3,City_CITY4):
    import numpy as np

    # convert input data to numpy array
    X = np.array([OnlineCommunication,AutomaticRefill,DoorstepDelivery,
       Welcome_email_opened,No_of_customized_email,
       No_of_customized_email_opened,No_of_customized_email_clicked,
       TotalOrderQuantity,OrderFrequency,Average_Ordergap,
       no_of_BusinessDays,year_reg,month_reg,day_reg,PreferredDeliveryDay_num,City_CITY2,
       City_CITY3,City_CITY4])

    # reshape the array to match the expected shape
    X = X.reshape(1, -1)

    # use the classifier to make a prediction
    prediction = classifier.predict(X)
    
    
    print(prediction)
    return prediction

def main():
    st.title("customer_Retention_Potential_Prediction")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">customer_RetentionPotential </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    OnlineCommunication=st.text_input("OnlineCommunication","Type Here")
    AutomaticRefill=st.text_input("AutomaticRefill","Type Here")
    DoorstepDelivery=st.text_input("DoorstepDelivery","Type Here")
    Welcome_email_opened=st.text_input("Welcome_email_opened","Type Here")
    No_of_customized_email=st.text_input("No_of_customized_email","Type Here")
    No_of_customized_email_opened=st.text_input("No_of_customized_email_opened","Type Here")
    No_of_customized_email_clicked=st.text_input("No_of_customized_email_clicked","Type Here")
    TotalOrderQuantity=st.text_input("TotalOrderQuantity","Type Here")
    OrderFrequency=st.text_input("OrderFrequency","Type Here")
    Average_Ordergap=st.text_input("Average_Ordergap","Type Here")
    no_of_BusinessDays=st.text_input("no_of_BusinessDays","Type Here")
    year_reg=st.text_input("year_reg","Type Here")
    month_reg=st.text_input("month_reg","Type Here")
    day_reg=st.text_input("day_reg","Type Here")
    PreferredDeliveryDay_num=st.text_input("PreferredDeliveryDay_num","Type Here")
    City_CITY2=st.text_input("City_CITY2","Type Here")
    City_CITY3=st.text_input("City_CITY3","Type Here")
    City_CITY4=st.text_input("City_CITY4","Type Here")
    
   
    result = ""
    if st.button("Predict"):
        result=customer_retential_potential_prediction(OnlineCommunication,AutomaticRefill,DoorstepDelivery,
       Welcome_email_opened,No_of_customized_email,
       No_of_customized_email_opened,No_of_customized_email_clicked,
       TotalOrderQuantity,OrderFrequency,Average_Ordergap,
       no_of_BusinessDays,year_reg,month_reg,day_reg,PreferredDeliveryDay_num,City_CITY2,
       City_CITY3,City_CITY4)
        
        
    #st.success('The customer_Retention_Potential level is {}'.format(result))
    st.success(f'The customer_Retention_Potential level is {"Low" if result == 0 else "High" if result == 1 else "Medium" if result == 2 else "Unknown"}')


    
    
    
    

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
