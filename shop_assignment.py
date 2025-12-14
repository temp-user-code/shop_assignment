import streamlit as st
import time

shop = [
    
    {'prod_name':'soap'      , 'price':150},
    {'prod_name':'sugar'     , 'price':200},
    {'prod_name':'oil'       , 'price':550},
    {'prod_name':'floor'     , 'price':150},
    {'prod_name':'milk'      , 'price':250},
    {'prod_name':'shampo'    , 'price':450},
    {'prod_name':'toothpaste', 'price':250},
    {'prod_name':'anday'     , 'price':35 },
    {'prod_name':'lays'      , 'price':100},
    {'prod_name':'biscuit'   , 'price':50 },
]

assignment_description_markdown = """
# Note: Desktop Only

⚠️ **This app is designed to run on desktop screens only and is not responsive for mobile devices. For the best experience, please use a desktop or laptop.**

---

# Online Shop System

## Project Overview
Welcome to the **Online Shop System**! This application simulates an online shopping experience, allowing users to browse products, add them to a shopping cart, view the cart, remove items, calculate the total bill, and proceed to checkout. The system is designed using basic Python functions and is powered by Streamlit for an interactive user interface.

## Features
- **Browse Products:** View a list of available products with their names and prices.
- **Add to Cart:** Add your favorite products to the shopping cart.
- **View Cart:** Check the items you have added to your cart at any time.
- **Remove from Cart:** Remove unwanted items from your cart.
- **Total Bill Calculation:** Calculate the total cost of the items in your cart.
- **Checkout:** Finalize your purchase and clear the cart.

## Requirements Fulfilled
This project fulfills all the following requirements of the assignment:
1. **Product List:** A list of products is created with details such as name and price. 
2. **Functions:**
    - `show_products()`: Displays available products with name and price.
    - `add_to_cart(cart, product_id)`: Adds selected products to the cart.
    - `view_cart(cart)`: Allows the user to view products added to the cart.
    - `remove_from_cart(cart, product_id)`: Removes a product from the cart.
    - `calculate_total(cart)`: Computes the total amount for the cart.
    - `checkout(cart)`: Finalizes the purchase, clears the cart, and displays the total bill.
3. **Streamlit Interface:** The application is fully interactive with buttons for adding/removing products, viewing the cart, and checking out.

## How to Use
1. **View Products:** Browse the available products.
2. **Add to Cart:** Add any products you'd like to buy by clicking the "Buy It" button next to each product.
3. **View Cart:** At any time, you can view the products you’ve added to your cart.
4. **Remove Items:** If you change your mind, you can remove products from your cart.
5. **Checkout:** Once you are done shopping, click "Checkout" to finalize the purchase and view your total bill.

## Streamlit UI
The interface is built using Streamlit, allowing for an interactive and user-friendly shopping experience.

---

Enjoy shopping and thank you for using our Online Shop System!

"""

# Session States
if "shop" not in st.session_state:
    st.session_state.shop = shop

if "cart" not in st.session_state:
    st.session_state.cart = []

if "show_cart" not in st.session_state:
    st.session_state.show_cart=False

if "checkout" not in st.session_state:
    st.session_state.checkout = False

if "entered" not in st.session_state:
    st.session_state.entered = False

# Required Functions
def show_products():
    st.header("Available Products")
    products_in_cart = [prod["prod_name"] for prod in st.session_state.cart]
    c1,c1a, c2 ,c3= st.columns([2,2 ,1,1])
    c1.header("Products")
    c1a.header("Price")
    for i, product in enumerate(st.session_state.shop):
        if product["prod_name"] in products_in_cart:
            continue
        c1,c1a, c2 ,c3= st.columns([2,2,1,1])
        c1.write(product["prod_name"])
        c1a.write(product["price"])
        if c2.button("Buy It", key=i):
            add_to_cart(st.session_state.cart, i)
            c3.success("Added")
            time.sleep(1.5)
            st.rerun()

def add_to_cart(cart, product_id):
    selected_product = st.session_state.shop[product_id]
    cart.append(
        {
            "prod_id": product_id,
            "prod_name": selected_product["prod_name"],
            "price": selected_product["price"],
        }
    )

    

def view_cart(cart):
    st.header("Products in Cart")
    if cart != []:
            c1,c1a, c2 ,c3= st.columns([2,2 ,1,1])
            c1.header("Products")
            c1a.header("Price")
            for product in st.session_state.cart:
                c1,c1a, c2 ,c3= st.columns([2,2,1,1])
                c1.write(product["prod_name"])
                c1a.write(product["price"])
                if c2.button("Delete It", key=f"c{product['prod_id']}", type="primary"):
                    remove_from_cart(st.session_state.cart, product["prod_id"])
                    c3.success("Deleted")
                    time.sleep(1.5)
                    st.rerun()
    else:
        st.error("Cart is Empty")

def remove_from_cart(cart, product_id):
    for i, item in enumerate(cart):
        if item["prod_id"] == product_id:
            del cart[i]
    
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total

def checkout(cart):
    st.title(f"Your total bill is {calculate_total(cart)}")
    cart.clear()

def main_menu():
    if not st.session_state.entered:
        st.title("Shop Assignment")
        st.markdown(assignment_description_markdown)

        if st.button("Enter into Shop"):
            st.session_state.entered = True
            st.rerun()

    if st.session_state.entered:
        if not st.session_state.checkout:
            col1, col2 = st.columns([1,1])
            if st.session_state.show_cart:
                if col1.button("Show Available Projects"):
                    st.session_state.show_cart=False
                    st.rerun()
                
                view_cart(st.session_state.cart)

            if not st.session_state.show_cart: 
                if col2.button("Show Cart"):
                    st.session_state.show_cart = True
                    st.rerun()
                show_products()
            
            if st.session_state.show_cart:
                if st.button("Checkout"):
                    st.session_state.checkout = True
                    st.rerun()
                
        elif st.session_state.checkout:
            checkout(st.session_state.cart)
            if st.button("Exit from Shop", type="primary"):
                st.session_state.clear()
                st.rerun()
        
        


main_menu()
