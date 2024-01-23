import streamlit as st
from db import MENU

def get_initial_resources():
    """This function returns the initial resources."""
    return {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

def payment_details(coffee_type):
    """This function will return paisa based on the payment method."""
    coffee_type = coffee_type.lower()
    paisa_type = st.radio("Choose Your Payment Method:", options=['Dollars', 'Rupees'])
    if paisa_type == 'Dollars':
        st.write(f"The Cost of {coffee_type} is: ${MENU[coffee_type]['cost']}")
    elif paisa_type == 'Rupees':
        st.write(f"The Cost of {coffee_type} is: ₹{MENU[coffee_type]['cost'] * 80}")
    
    paisa = st.number_input("Enter Your Amount", min_value=1)
    return paisa, paisa_type


def resources_available(coffee_type, water, milk, coffee):
    """This function will check if the resources are available or not."""
    coffee_type = coffee_type.lower()
    if coffee_type.lower() == 'espresso':
        if MENU[coffee_type]['ingredients']['water'] <= water and MENU[coffee_type]['ingredients']['coffee'] <= coffee:
            return True
    elif MENU[coffee_type]['ingredients']['water'] <= water and MENU[coffee_type]['ingredients']['milk'] <= milk and MENU[coffee_type]['ingredients']['coffee'] <= coffee:
        return True
    else:
        return False

def verify_paisa(paisa, coffee_type, paisa_type):
    """This function will verify the paisa."""
    coffee_type = coffee_type.lower()
    if paisa_type == 'Dollars':
        if paisa >= MENU[coffee_type]['cost']:
            return True
        else:
            return False
    elif paisa_type == 'Rupees':
        if paisa >= MENU[coffee_type]['cost'] * 80:
            return True
        else:
            return False
    

def process_money(coffee_type, paisa, paisa_type):
    """This function will process the paisa."""
    coffee_type = coffee_type.lower()
    cost = None
    change = None
    if paisa_type == 'Dollars':
        change = paisa - MENU[coffee_type]['cost']
    elif paisa_type == 'Rupees':
        change= (paisa - (MENU[coffee_type]['cost'] * 80)) / 80
    cost = MENU[coffee_type]['cost']
    return change, cost

def add_resources(resources):
    """This function will add resources"""
    water = st.number_input("Enter the amount of water in ml:", min_value=1, max_value=500)
    milk = st.number_input("Enter the amount of milk in ml:", min_value=1, max_value=500)
    coffee = st.number_input("Enter the amount of coffee in g:", min_value=1, max_value=200)

    resources['water'] += water
    resources['milk'] += milk
    resources['coffee'] += coffee



def report(paisa, resources):
    """This function will print report of resources."""
    st.write(f"Water: {resources['water']}ml")
    st.write(f"Milk: {resources['milk']}ml")
    st.write(f"Coffee: {resources['coffee']}g")
    st.write(f"Money in account: ${paisa:.2f}")