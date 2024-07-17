import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import mysql.connector
from datetime import  time

with st.sidebar:
        selected = option_menu(
        menu_title= "Redbus Booking",
        options = ["Home","Bus Booking"],
        icons = ["house","bus-front"],
        menu_icon="cast",
        default_index=0
        )
db_connection = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "12345",
        database = "MDE92"
)

# Fetch options from database for dropdown
cursor = db_connection.cursor()


if selected=="Home":
        st.title("Welcome To Bus-Ticket Analyser Application")
if selected == "Bus Booking":
        st.write("You Can select the preferred options and analyse the bus availablity!")

        col1, col2,col3 = st.columns(3)

        with col1:
                cursor.execute("SELECT bus_routes_name FROM bus_routes")
                options = [row[0] for row in cursor.fetchall()]
                bus_routes =[]
                options = set(options)
                for i in options:
                        bus_routes.append(i)

                selected_option = st.selectbox(
                        'Select the Bus Route',
                        bus_routes
                )

        if selected_option:
                # Execute SQL query with selected_option as parameter
                query1 = f"SELECT * FROM bus_routes WHERE bus_routes_name = '{selected_option}'"


        with col2:
                option1 = st.selectbox(
                        'Select the Seat Type ',
                        ('Sleeper','Seater','Semi Sleeper','Super Luxury')
                )
                if option1 == "Sleeper":
                        query1 += "and  bus_type LIKE '%Sleeper%' AND bus_type NOT LIKE '%Semi Sleeper%'"

                elif option1 == "Seater":
                        query1 += "and  bus_type LIKE '%Seater%'"
                elif option1 == "Super Luxury":
                        query1 += "and  bus_type LIKE '%SUPER LUXURY%'"
                else:
                        query1 += "and  bus_type LIKE '%Semi Sleeper%'"

        with col3:
                option2 = st.selectbox(
                        'Select the Ac Type ',
                        ('A/C','Non A/C')
                )
                if  option2 == 'A/C':
                        # Execute SQL query with selected_option as parameter
                        query1 += """and (bus_type LIKE '%A/C%' OR bus_type LIKE '%A.C%' OR bus_type LIKE '%AC%') AND 
                                      NOT (LOWER(bus_type) LIKE '%non a/c%' OR LOWER(bus_type) LIKE '%non-ac%' OR 
                                      LOWER(bus_type) LIKE '%non ac%')"""
                else:
                        query1 += "AND (LOWER(bus_type) LIKE '%non a/c%' OR LOWER(bus_type) LIKE '%non-ac%' OR LOWER(bus_type) LIKE '%non ac%')"



        with col1:
                option3 = st.selectbox(
                        'Select the Ratings',
                        ('Below 1','1 to 2','2 to 3','3 to 4','4 to 5')
                )
                if option3 == "Below 1":
                        query1 += "and star_rating < 1"
                elif option3 == "1 to 2":
                        query1 += "and star_rating BETWEEN 1 AND 2"
                elif option3 == "2 to 3":
                        query1 += "and star_rating BETWEEN 2 AND 3"
                elif option3 == "3 to 4":
                        query1 += "and star_rating BETWEEN 3 AND 4"
                elif option3 == "4 to 5":
                        query1 += "and star_rating BETWEEN 4 AND 5"
        with col2:
                option4 = st.selectbox(
                        'Select the Starting Time',
                        ('00:00 - 01:00', '01:00 - 02:00', '02:00 - 03:00', '03:00 - 04:00', '04:00 - 05:00', '05:00 - 06:00',
                         '06:00 - 07:00', '07:00 - 08:00', '08:00 - 09:00','09:00 - 10:00', '10:00 - 11:00', '11:00 - 12:00',
                         '12:00 - 13:00', '13:00 - 14:00', '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00', '17:00 - 18:00',
                         '18:00 - 19:00', '19:00 - 20:00', '20:00 - 21:00', '21:00 - 22:00', '22:00 - 23:00', '23:00 - 24:00')
                )
                if option4:
                        time_range_str = option4
                        times = time_range_str.split(' - ')
                        start_time = times[0]
                        end_time = times[1]
                        query1 += f" and time(departing_time) >='{start_time}' and time(departing_time) <'{end_time}'"
        with col3:

                option5 = st.selectbox(
                        'Select the Bus fare',
                        ('Less than 500','Less than 1000','Less than 1500','Less than 2000','Less than 5000')
                )
                if option5:
                        if 'Less than' in option5:
                                number_part = option5.split('Less than ')[1]
                                number = int(number_part.replace(',', ''))
                                query1 += f"and price < {number}"

        cursor.execute(query1)
        results = cursor.fetchall()
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        st.dataframe(df)


# Close database connection
cursor.close()
db_connection.close()
