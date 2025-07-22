import pymysql # type: ignore

# This module provides functions to interact with a MySQL database for an e-commerce application.

# Function to connect to the MySQL database
def connect_to_db():
    conn = pymysql.connect(
        host='localhost',
        user='qa_user',
        password='qa_pass',
        db='ecommerce'
    )
    return conn  # Return the connection object for further use

# to insert a new user into the users table in the database
def insert_user(username, password):
    
    # Connect to the MYSQL database
    conn = connect_to_db()

    with conn.cursor() as cursor:
        # Insert a new user into the users table
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        conn.commit() #saves the changes to the database. without this, the changes won't be saved
        conn.close() #ensure the connection is closed


#retrive product information by product name
def get_product_info(product_name):
    
    # Connect to the MYSQL database
    conn = connect_to_db()
   
    with conn.cursor() as cursor:
        # Retrieve product information by product name
        sql = "SELECT id, name , price FROM products WHERE name = %s"
        cursor.execute(sql, (product_name,))
        result = cursor.fetchone()  # Fetch one record
        conn.close()  # Ensure the connection is closed
        return result  # Return the product information

#verify a product has been added to the cart
def verify_product_in_cart(user_email, product_name):
    
    # Connect to the MYSQL database
    conn = connect_to_db()
    
    with conn.cursor() as cursor:
        # Verify if a product has been added to the cart

        #This SQL query checks if a product with the specified name is in the cart 
        # of a user with the specified email.

        # join cart and product on product_id
        # join cart and users on user_id
        
        sql = """
        SELECT cart.id, cart.user_id, cart.product_id, products.name 
        FROM cart 
        JOIN products ON cart.product_id = products.id  //
        JOIN users ON cart.user_id = users.id 
        WHERE users.email = %s AND products.name = %s
        """
        cursor.execute(sql, (user_email, product_name))
        result = cursor.fetchone()

        conn.close()  # Ensure the connection is closed
        return result is not None  # Return True if product is in cart, else False