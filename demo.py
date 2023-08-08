import streamlit as st
import time
import warnings

st.write("Hello ,let's learn how to build a streamlit app together")
st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
# st.image("kid.jpg")
# st.audio("Audio.mp3")
# st.video("video.mp4")
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
st.balloons()
st.progress(10)
# with st.spinner('Wait for it...'):
#     time.sleep(10)
st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
st.sidebar.title("Hello i am sidebar")
container = st.container()
container.write("write here i am container")

import matplotlib.pyplot as plt
import numpy as np
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

import pandas as pd
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)


df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)

df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)

# import altair as alt
# df = pd.DataFrame(np.random.randn(500, 3),   columns=['x','y','z'])​
# c = alt.Chart(df).mark_circle().encode(   x='x' , 'y'=y , size='z', color='z', tooltip=['x', 'y', 'z'])
# st.altair_chart(c, use_container_width=True)

import graphviz as graphviz
st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)

# cimport streamlit as stimport pandas as pdimport numpy as npimport pickle  #to load a saved modelimport base64  #to open .gif files in streamlit app

@st.cache(suppress_st_warning=True)
def get_fvalue(val):    
    feature_dict = {"No":1,"Yes":2}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
               return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

# if app_mode=='Home':    
#     st.title('LOAN PREDICTION :')      
#     st.image('loan_image.jpg')    
#     st.markdown('Dataset :')    
#     data=pd.read_csv('loan_dataset.csv')    
#     st.write(data.head())    
#     st.markdown('Applicant Income VS Loan Amount ')    
#     st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))

# elif app_mode == 'Prediction':    
#     st.image('slider-short-3.jpg')    
#     st.subheader('Sir/Mme , YOU need to fill all necessary informations in order    to get a reply to your loan request !')    
#     st.sidebar.header("Informations about the client :")    
#     gender_dict = {"Male":1,"Female":2}    
#     feature_dict = {"No":1,"Yes":2}    
#     edu={'Graduate':1,'Not Graduate':2}   
#     prop={'Rural':1,'Urban':2,'Semiurban':3}    
#     ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)    
#     CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)   
#     LoanAmount=st.sidebar.slider('LoanAmount in K$',9.0,700.0,200.0)    
#     Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))    
#     Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))    
#     Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))    
#     Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))    
#     Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))    
#     Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])    
#     Education=st.sidebar.radio('Education',tuple(edu.keys()))    
#     Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))    
#     class_0 , class_3 , class_1,class_2 = 0,0,0,0    
# if Dependents == '0':        
#     class_0 = 1    
# elif Dependents == '1':        
#     class_1 = 1    
# elif Dependents == '2' :        
#     class_2 = 1    
# else:        
#     class_3= 1    
# Rural,Urban,Semiurban=0,0,0    
# if Property_Area == 'Urban' :        
#     Urban = 1    
# elif Property_Area == 'Semiurban' :        
#     Semiurban = 1    
# else :        
#     Rural=1

# data1={    'Gender':Gender,    'Married':Married,    'Dependents':[class_0,class_1,class_2,class_3],    'Education':Education,    'ApplicantIncome':ApplicantIncome,    'CoapplicantIncome':CoapplicantIncome,    'Self Employed':Self_Employed,    'LoanAmount':LoanAmount,    'Loan_Amount_Term':Loan_Amount_Term,    'Credit_History':Credit_History,    'Property_Area':[Rural,Urban,Semiurban],    }    
# feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,
#               get_value(Gender,gender_dict),get_fvalue(Married),
#               data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],
#               data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),
#               data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]
#               ]    
# single_sample = np.array(feature_list).reshape(1,-1)