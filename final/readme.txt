# Online wearable and Accessories e-commerce website
1.Basic e-commerce website using technologies HTML, CSS, JQuery, JavaScript for the frontend and Python, SQLite database for the backend.

2.This website basically shows a dashboard of items to the customer when they login to website and after purchasing desired products the inventory is updated

3.The database is automatically updated with the SQL queries and filter by function to get only desired items in the list.

#Contents of the file
Final_Project/
-README.md
-readme.txt

-requirements.txt

-data.db

-application.py
-wsgi.py

./templates
 -adminbase.html
 -adminlogin.html
 -base.html
 -cart.html
 -contactquery.html
 -contactus.html
 -history.html
 -index.html
 -inventory.html
 -login.html
 -new.html
 -payment.html
 -product_id_missing.html
 -product_not_found.html
 -signin.html
 -thankyou.html
 -update_product.html

 ./static
 -css
 --custom.css
 --footer.css
 --style.css
 --styles.css
 -img
 -js
 --myscripts.js
 --validate.js

#VIRTUAL ENVIRONMENT SETUP

 1.Open a new terminal in vscode, open the folder directory.
 2.Create virtual enviornment using following commands.
    For windows:
    python -m venv env
    env\Scripts\activate

    For MAC:
    python -m venv env
    source env\bin\activate

 3.Inorder to downlaod the requirements.txt file
    pip install -r requirements.txt   


#Executing the code
python wsgi.py
1.calling the main function to run the application.py


To check admin functionalities, use the following credentials:
username - ritish
password - ritish123