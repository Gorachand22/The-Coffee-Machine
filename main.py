# main.py
"""
This is the main file for the Streamlit app.
"""
import streamlit as st
import work
from db import MENU

if 'MONEY' not in st.session_state:
    st.session_state['MONEY'] = 0

if 'resources' not in st.session_state:
    st.session_state['resources'] = work.get_initial_resources()

def main():
    """This is the main function"""
    st.header("Welcome To The Coffee Machine")
    st.image("images/coffee.png",width=200)
    st.subheader("What do you want?")
    
    coffee_type = st.radio("Select Coffee Type:", options=["Espresso", "Latte", "Cappuccino"])

    paisa, paisa_type = work.payment_details(coffee_type)

    if st.button("Order"):
        water = st.session_state['resources']['water']
        milk = st.session_state['resources']['milk']
        coffee = st.session_state['resources']['coffee']
        if work.resources_available(coffee_type, water, milk, coffee):
            if work.verify_paisa(paisa, coffee_type, paisa_type):
                change,cost = work.process_money(coffee_type, paisa, paisa_type)
                st.session_state['MONEY'] += cost
                
                Type = coffee_type.lower()
                if coffee_type == 'Espresso':
                    
                    st.session_state['resources']['water'] -= MENU[Type]['ingredients']['water']
                    st.session_state['resources']['coffee'] -= MENU[Type]['ingredients']['coffee']
                elif coffee_type in ['Latte','Cappuccino']:
                    st.session_state['resources']['water'] -= MENU[Type]['ingredients']['water']
                    st.session_state['resources']['milk'] -= MENU[Type]['ingredients']['milk']
                    st.session_state['resources']['coffee'] -= MENU[Type]['ingredients']['coffee']
                
                st.success(f"Here is your {coffee_type} ☕️. Enjoy!")
                st.info(f"Your change is ${change} \n")
            
            else:
                st.warning("Not enough money \n")
        else:
            st.warning("Not enough resources \n")
            st.warning("Please try another coffee or add more resources")
    
    if st.button("Report"):
        work.report(st.session_state['MONEY'], st.session_state['resources'])

    if st.button("Add Resources"):
        work.add_resources(st.session_state['resources'])

st.sidebar.markdown(
        """
        1. **Select Coffee Type:**
           - Use the radio button to choose the type of coffee you want (Espresso, Latte, or Cappuccino).

        2. **Payment Method:**
           - Choose your payment method (Dollars or Rupees).
           - The cost of the selected coffee type will be displayed based on the chosen currency.

        3. **Place an Order:**
           - Click the "Order" button to place your coffee order.
           - If you don't have enough money or resources, the app will provide warnings.

        4. **View Resources:**
           - Click the "Report" button to view the current resources (water, milk, coffee) and money in your account.

        5. **Add Resources:**
           - Click the "Add Resources" button to add more water, milk, or coffee to the coffee machine.

        6. **Enjoy Your Coffee:**
           - After placing an order, the app will display your coffee and any change due.

        Note: Make sure to add sufficient resources and funds before placing an order.
        """
    )
if __name__ == "__main__":
    main()