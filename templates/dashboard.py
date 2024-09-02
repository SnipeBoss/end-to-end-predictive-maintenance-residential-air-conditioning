import streamlit as st
import pandas as pd
import streamlit_option_menu
from streamlit_option_menu import option_menu
# https://github.com/ksoderholm22/similo_beta2
# https://github.com/iamontheinet/snowpark-python-anaconda/blob/main/streamlit_app.py

# Custom CSS for Blue Tone
st.markdown("""
    <style type="text/css">
    blockquote {
        margin: 1em 0px 1em -1px;
        padding: 0px 0px 0px 1.2em;
        font-size: 20px;
        border-left: 5px solid rgb(230, 234, 241);
        # background-color: rgb(129, 164, 182);
    }
    blockquote p {
        font-size: 30px;
        color: #FFFFFF;
    }
    [data-testid=stSidebar] {
        background-color: rgb(129, 164, 182);
        color: #FFFFFF;
    }
    [aria-selected="true"] {
         color: #000000;
    }
    </style>
""", unsafe_allow_html=True)



with st.sidebar:
  selected = option_menu(
    menu_title = "Predictive Maintenance",
    # https://icons.getbootstrap.com/
    options = ["Home","Evaporator","Compressor", "Condensor"],
    icons = ["house","thermometer-snow","fan", "gear"],
    menu_icon = "thermometer-snow",
    default_index = 0,
  )
  

#   if selected == "Home":
#     st.title(f"You Have selected {selected}")
#     st.header('Snowflake Healthcare App')
#     my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#     my_cur = my_cnx.cursor()
#     # run a snowflake query and put it all in a var called my_catalog
#     my_cur.execute("select * from SWEATSUITS")
#     my_catalog = my_cur.fetchall()
#     st.dataframe(my_catalog)
#     q1 = st.text_input('Write your query','')
#     st.button('Run Query')
#     if not q1:
#       st.error('Please write a query')
#     else:
#       my_cur.execute(q1)
#       my_catalog = my_cur.fetchall()
#       st.dataframe(my_catalog)
#   if selected == "Projects":
#     st.title(f"You Have selected {selected}")
#   if selected == "Contact":
#     st.title(f"You Have selected {selected}")