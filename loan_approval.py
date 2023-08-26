# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 20:26:16 2022

@author: USER
"""
import sklearn
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading saves model

loan_status=pickle.load(open(r"K:\My Drive\My Work\Working Data\AI\Python Files\Loan Approval Prediction Dataset\loan_approval_prediction_xgb.sav",'rb'))

#diabetes_model=pickle.load(open(r"K:\My Drive\My Work\Working Data\AI\Python Files\Multiple Disease Prediction\diabetes_model.sav",'rb'))

#heart_model=pickle.load(open(r"K:\My Drive\My Work\Working Data\AI\Python Files\Multiple Disease Prediction\heart_disease_model.sav",'rb'))

#parkinsons_model=pickle.load(open(r"K:\My Drive\My Work\Working Data\AI\Python Files\Multiple Disease Prediction\parkinsons_model.sav",'rb'))



#side bar for navigations

with st.sidebar:
    selected=option_menu('Loan Prediction System',
                          ['Loan Status Prediction'
                           ],
                          
                          icons=['heart'],
                          
                            default_index=0)
    
    
    #Diabetes prediction page
if(selected=='Loan Status Prediction'):

    #page title
    st.title('Loan Status Prediction Using Machine Learnig')
    
    
    #getting the input data from user
    #colum for input fields
    
    col1,col2,col3= st.columns(3)
    
    with col1:
        loanid = st.text_input('Loan ID')
        
    with col2:
        noofdeper = st.text_input('No Of Deper')
        
    with col3:
        education = st.text_input('Education')
        
        
    with col1:
        selfemployed = st.text_input('Self Employed')
    
    with col2:
        incomeannum = st.text_input('Income Annual')
        
    with col3:
        loanamount = st.text_input('Loan Amount')
        
    with col1:
        loanterm = st.text_input('Loan Term')

    with col2:
        cibilscore = st.text_input('Cibil Score')
        
    with col3:
         residantialasset = st.text_input('Residantial Asset')
         
    with col1:
         commercialasset = st.text_input('Commercial Asset')

    with col2:
         luxuryasset = st.text_input('Luxury Asset')
         
    with col3:
        bankasset = st.text_input('Bank Asset')
        
        
        
    
    
    #code for prediction
    
    loan_diagnosis= ''
    
    #creating button for predictions
    
    if st.button('Loan Status Result'):
        loan_prediction= loan_status.predict([[ loanid, noofdeper, education, selfemployed, incomeannum, loanamount, loanterm, cibilscore, residantialasset, commercialasset, luxuryasset, bankasset]])
        if(loan_prediction[0]==1):
            loan_diagnosis='Loan Approved!'
        else:
            loan_diagnosis='Loan is not Approved!'
            
    st.success(loan_diagnosis)  





