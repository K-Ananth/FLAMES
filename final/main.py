import streamlit as st
import pandas as pd
from PIL import Image

hide_st_style="""
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>"""
st.markdown(hide_st_style,unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    image = Image.open("C:\\Users\\91944\\inwallet.png")
    st.image(image)
with col3:
    st.write(' ')

file_name = st.sidebar.file_uploader("Upload File", type={"csv", "txt","xlsx"})

col1, col2, col3= st.columns(3)

if file_name is not None:

    xl = pd.ExcelFile(file_name)
    sheet_selector = st.sidebar.selectbox("Select sheet:",xl.sheet_names)
    df = pd.read_excel(file_name,sheet_selector)
    st.markdown(f"### Currently Selected: `{sheet_selector}`")
    df6 = df.copy()
    col1.text("Shape of the input data : ")
    col2.text(df.shape)

    if sheet_selector=="PINCODE":

       options_Pin = df6['PINCODE'].unique().tolist()
       col1.text("No of Pincode           : ")
       col2.text(len([*set(options_Pin)]))

       options_Ban = df6['BANK'].unique().tolist()
       col1.text("No of Bank              : ")
       col2.text(len([*set(options_Ban)]))

       selected_Pin = st.sidebar.multiselect('Pincode', options_Pin)

       selected_Ban = st.sidebar.multiselect('Bank Name', options_Ban)

       if selected_Pin:
           df6 = df6[df6["PINCODE"].isin(selected_Pin)]
           st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
           )

       elif selected_Ban:
           df6 = df6[df6["BANK"].isin(selected_Ban)]
           st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
           )
       else:
           st.markdown(
               f'<p class="header_title"> {str(df6.shape[0])} </p>',
               unsafe_allow_html=True,
           )
       if selected_Pin or selected_Ban:
           st.dataframe(df6.reset_index(drop=True))
       else:
           st.dataframe(df)
    else:

        options_PL = df6['PL'].tolist()
        options_BL = df6['BL'].tolist()
        options_HL = df6['HL'].tolist()
        options_LAP = df6['LAP'].tolist()
        options_GL = df6['GL'].tolist()

        col1.text("No of PL                : ")
        col2.text(options_PL.count('YES'))

        col1.text("No of BL                : ")
        col2.text(options_BL.count('YES'))

        col1.text("No of HL                : ")
        col2.text(options_HL.count('YES'))

        col1.text("No of LAP               : ")
        col2.text(options_LAP.count('YES'))

        col1.text("No of GL                : ")
        col2.text(options_GL.count('YES'))

        options_Name = df6['NAME'].unique().tolist()
        selected_Name = st.sidebar.multiselect('Name',options_Name)

        col1.text("No of Names             : ")
        col2.text(len([*set(options_Name)]))

        options_phone = df6['Phone Number'].unique().tolist()
        selected_phone = st.sidebar.multiselect('Phone Number',options_phone)

        options_bank = df6['BANK/NBFC'].unique().tolist()
        selected_bank = st.sidebar.multiselect('Bank',options_bank)

        col1.text("No of Banks             : ")
        col2.text(len([*set(options_bank)]))

        options_district = df6['District'].unique().tolist()
        selected_district = st.sidebar.multiselect('District',options_district)
        col1.text("No of District          : ")
        col2.text(len([*set(options_district)]))

        options_location = df6['Location'].unique().tolist()
        selected_location = st.sidebar.multiselect('Location',options_location)
        col1.text("No of Locations         : ")
        col2.text(len([*set(options_location)]))

        if selected_Name:
            df6 = df6[df6["NAME"].isin(selected_Name)]
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        elif selected_phone:
            df6 = df6[df6["Phone Number"].isin(selected_phone)]
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        elif selected_bank:
            df6 = df6[df6["BANK/NBFC"].isin(selected_bank)]
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        elif selected_district:
            df6 = df6[df6["District"].isin(selected_district)]
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        elif selected_location:
            df6 = df6[df6["Location"].isin(selected_location)]
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        else:
            st.markdown(
                       f'<p class="header_title"> {str(df6.shape[0])} </p>',
                       unsafe_allow_html=True,
                       )

        if selected_Name or selected_phone or selected_bank or selected_district or selected_location:
            st.dataframe(df6.reset_index(drop = True))
        else:
            st.dataframe(df)
