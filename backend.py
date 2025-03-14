import mysql.connector
import datetime
import streamlit as st

mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="An4ka6422?", database="CMS")
st.session_state.eid = st.session_state.firstname = None

def login_checker(email, password):
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Customers")
    for row in c:
        if row[3] == email and row[4] == password:
            st.session_state.firstname = row[1]
            st.session_state.cid = row[0]
            st.session_state.row = row
            return True, True
        elif (row[3] == email and row[4] != password) or (row[3] != email and row[4] == password):
            return True, False
    c.close()
    return False, False

def admin_checker(email, password):
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Admin")
    for row in c:
        if row[1] == email and row[2] == password:
            return True
    c.close()
    return False

def add_details(first_name, last_name, email, co_password, number, address):
    c = mydb.cursor(buffered=True)
    c.execute('''INSERT INTO Customers (FirstName, LastName, Email, Password, Phone, Address)
              VALUES (%s, %s, %s, %s, %s, %s)''', (first_name, last_name, email, co_password, number, address))
    mydb.commit()
    c.close()
    return None

def get_customers():
    customers = []
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Customers;")
    for row in c:
        customers.append(row)
    c.close()
    return customers

def delete_customer(x):
    c = mydb.cursor(buffered=True)
    c.execute("DELETE FROM Customers WHERE CustomerID = %s", (x, ))
    mydb.commit()
    c.close()
    return None

def edit_details(cid, first_name, last_name, email, number, address):
    c = mydb.cursor(buffered=True)
    c.execute(''' UPDATE Customers SET FirstName = %s, LastName = %s, Email = %s, Phone = %s, Address = %s
               WHERE CustomerID = %s''', (first_name, last_name, email, number, address, cid))
    mydb.commit()
    c.close()
    return None

def get_products():
    products = []
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Products;")
    for row in c:
        products.append(row)
    c.close()
    return products

def edit_product_details(pid, product_name, description, price, stock, image):
    c = mydb.cursor(buffered=True)
    c.execute(''' UPDATE Products SET Name = %s, Description = %s, Price = %s, StockQuantity = %s, ProductImage  = %s
               WHERE ProductID = %s''', (product_name, description, price, stock, image, pid))
    mydb.commit()
    c.close()
    return None

def delete_product(x):
    c = mydb.cursor(buffered=True)
    c.execute("DELETE FROM Products WHERE ProductID = %s", (x, ))
    mydb.commit()
    c.close()
    return None

def add_product(product_name, description, price, stock, image):
    c = mydb.cursor(buffered=True)
    c.execute('''INSERT INTO Products (Name, Description, Price, StockQuantity, ProductImage)
              VALUES (%s, %s, %s, %s, %s)''', (product_name, description, price, stock, image))
    mydb.commit()
    c.close()
    return None

def get_orders():
    orders = []
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Orders;")
    for row in c:
        orders.append(row)
    c.close()
    return orders

def get_customer_firstname(x):
    c = mydb.cursor(buffered=True)
    c.execute("SELECT Customers.FirstName From Orders Join Customers ON Orders.CustomerID = Customers.CustomerID WHERE Customers.CustomerID = %s;", (x, ))
    for row in c:
        name = row[0]
    return name

def get_order_details(x):
    details = ""
    c = mydb.cursor(buffered=True)
    c.execute('''SELECT 
    Products.Name,
    OrderDetails.Quantity
    FROM 
        OrderDetails
    JOIN 
        Products
    ON 
        OrderDetails.ProductID = Products.ProductID
    JOIN 
        Orders
    ON 
        OrderDetails.OrderID = Orders.OrderID
    WHERE Orders.OrderID = %s;
    ''', (x, ))
    for row in c:
        details += f"{row[0]}  -----  {row[1]} units \n\n"
    return details

def modify_status(status, oid):
    c = mydb.cursor(buffered=True)
    c.execute(''' UPDATE Orders SET OrderStatus = %s
               WHERE OrderID = %s;''', (status, oid))
    mydb.commit()
    c.close()
    return None

def add_to_basket(pid, units):
    c = mydb.cursor(buffered=True)
    c.execute("SHOW tables;")
    tables = ""
    for row in c:
        tables += row[0]
    if "Basket" not in tables:
        c.execute('''CREATE TABLE Basket (
                    BasketID INT AUTO_INCREMENT PRIMARY KEY,
                    ProductID INT NOT NULL,
                    CustomerID INT NOT NULL,
                    Quantity INT NOT NULL,
                    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
                    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
                );
                ''')
    c.execute('''INSERT INTO Basket (ProductID, CustomerID, Quantity)
                VALUES (%s, %s, %s)''', (pid, st.session_state.cid, units)
            )
    mydb.commit()
    c.close()
    return None

def get_total_price():
    price = 0
    c = mydb.cursor(buffered=True)
    c.execute('''SELECT SUM(b.Quantity * p.Price) AS TotalPrice
                FROM Basket b
                JOIN Products p ON b.ProductID = p.ProductID
                WHERE b.CustomerID = %s;
                ''', (st.session_state.cid, ))
    for row in c:
        price = row[0]
    return price

def get_basket():
    items = []
    c = mydb.cursor(buffered=True)
    c.execute('''SELECT 
                    p.ProductImage,
                    p.Name, 
                    p.Price, 
                    b.Quantity,
                    b.BasketID
                FROM 
                    Basket b
                JOIN 
                    Products p ON b.ProductID = p.ProductID
                WHERE 
                    b.CustomerID = %s;
                ''', (st.session_state.cid, ))
    for row in c:
        items.append(row)
    c.close()
    return items

def delete_item(x):
    c = mydb.cursor(buffered=True)
    c.execute("DELETE FROM Basket WHERE BasketID = %s", (x, ))
    mydb.commit()
    c.close()
    return None

def checkout_basket():
    c = mydb.cursor(buffered=True)
    insert_order_query = '''
        INSERT INTO Orders (CustomerID, TotalAmount)
        SELECT CustomerID, SUM(b.Quantity * p.Price)
        FROM Basket b
        JOIN Products p ON b.ProductID = p.ProductID
        WHERE b.CustomerID = %s
        GROUP BY b.CustomerID;
    '''
    c.execute(insert_order_query, (st.session_state.cid,))
    
    c.execute('SELECT LAST_INSERT_ID() AS LastOrderID;')
    order_id = c.fetchone()[0]
    
    insert_order_details_query = '''
        INSERT INTO OrderDetails (OrderID, ProductID, Quantity)
        SELECT %s, b.ProductID, b.Quantity
        FROM Basket b
        WHERE b.CustomerID = %s;
    '''
    c.execute(insert_order_details_query, (order_id, st.session_state.cid))
    
    delete_basket_query = 'DELETE FROM Basket WHERE CustomerID = %s;'
    c.execute(delete_basket_query, (st.session_state.cid,))
    mydb.commit()
    return None

def get_customer_order():
    orders = []
    c = mydb.cursor(buffered=True)
    c.execute("SELECT * from Orders WHERE CustomerID = %s;", (st.session_state.cid, ))
    for row in c:
        orders.append(row)
    c.close()
    return orders