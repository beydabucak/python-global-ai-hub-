# -*- coding: utf-8 -*-
"""global ai hub python for ml guided project 2.2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RaXnvM7TD7PZip4aqJULiJWdEwLSNqva

### Logistic
Let's continue with the next company from your brief.

Storage plays a crucial part in logistics, and the company wants to track the status of inventory space with software and be able to make changes in the system whenever it is needed.

Again, you need to create a class.

📌 Use the keyword "class" to create the class "Logistics" 

📌 Use the "__init__" method to initialze the object's attributes: self, company_name, foundation_year, founder_name,  company_slogan, and inventory_space.

#### Define the methods

Next, define the methods of the class:

1. print_report method: A method to print out information about the company. 

  📌 The report should have this structure: 

  "The company *name*, was founded in *year*. The founder of the company is *founder_name*. 

  Company slogan: *company_slogan*

  Inventory space of the company: *inventory_space*


2. update_inventory_space method: A method to update its inventory_space, and print a statement to describe the change.
It should consider the parameter "new_storage_space".
"""

#Define the "Logistics" class
class Logistics:
    #Initialize the object's attributes 
  def __init__ (self, company_name, foundation_year, founder_name, company_slogan,inventory_space)
    self.company_name=company_name
    self.foundation_year=foundation_year
    self.founder_name=founder_name
    self.company_slogan=company_slogan
    self.inventory_space=inventory_space
        
    #Define the print_report method
    def print_report(self):
      print(f"""the company name: {self.company_name}
            the founder name: {self.founder_name}
            foundation year: {self.foundation_year}
            company slogan: {self.company_slogan}
            inventory space: {self.inventory_space}""")

    #Define the update_inventory_space method
    def update_inventory_space(self):
      self.inventory_space=new_storage_space
      print("inventory space has been updated to {}".format(self.inventory_space))

"""#### Create the object 
Now that we created our class and initialized its attributes and methods, we can create the object “logistic_company1” with the attributes: 

* Company_name “LogCom”

* foundation_year “1990”

* founder_name “Laura McCartey”

* company_slogan “There is no place we cannot reach.” 

* inventory_space “2500”

"""

#Create the object "logistic_company1" with it's attributes
logistic_company1=Logistic("LogCom",1990,"Laura McCartey","There is no place we cannot reach.",2500)

"""
#### Let’s check if the methods work.
The logistics company plans to buy a new warehouse which will increase the inventory_space to 3000. 

📌 Call the update_inventory_space method to reflect this change in the system and then use the “print_report” method."""

#Update the inventory space
logistic_company1.update_inventory_space(3000)
#Call the print_report method for logistic_company1
logistic_company1.print_report()

"""### Trading
The last company you need to digitalize is the trading one.

You are expected to create a method to update the sales and expenses and calculate the revenue.

As with the previous companies, you need to create a class.

📌 Use the keyword "class" to create the class "Trading" 

📌 Use the "__init__" method to initialze the object's attributes: self, company_name, foundation_year, founder_name,  company_slogan, sales, expenses, and revenue.

#### Define the methods

Next, define the methods of the class:

1. print_report method: A method to print out information about the company. 

  📌 The report should have this structure: 

  "The company *name*, was founded in *year*. The founder of the company is *founder_name*. 

  Company slogan: *company_slogan*

  Total sales: *sales*

  Total expenses: *expenses*

  Total revenue: *revenue*


2. update_sales_and_expenses method: A method to update the sales and expenses.
It should consider the parameters "new_sales" and "new_expenses".

3. calculate_revenue method: A method  which computes the difference between sales and expenses and prints out the revenue.
"""

#Define the "Trading" class
class Trading:
    #Initialize the object's attributes 
    def __init__ (self, company_name, foundation_year, founder_name, company_slogan, sales, expenses, revenue)
      self.company_name=company_name
      self.foundation_year=foundation_year
      self.founder_name=founder_name
      self.company_slogan=company_slogan
      self.sales=sales
      self.expenses=expenses
      self.revenue=revenue

    #Define the print_report method
    def print_report(self):
      print(f"""the company name: {self.company_name}
            the founder name: {self.founder_name}
            foundation year: {self.foundation_year}
            company slogan: {self.company_slogan}
            sales: {self.sales}
            expenses:{self.expenses}
            revenur: {self.revenue}""")

    #Define the update_sales_and_expenses method
    def update_sales_and_expenses(self):
      self.sales+=new_sales
      self.expenses+=new_expenses
      print(f"sales and expenses has been updated to {self.sales} and {self.expenses}")
  

    #Define the calculate_revenue method
    def calculate_revenue(self):
      self.revenue=self.sales-self.expenses
      print(f"revenue of the company:: {self.revenue}")

"""#### Create the object 
Now that we created our class and initialized its attributes and methods, we can create the object “trading_company1” with the attributes: 

* Company_name “TraCom”

* foundation_year “2005”

* founder_name “Chong Wu”

* company_slogan “We revolutionize trading.” 

* sales "5000"

* expenses "2000"

* revenue "3000"
"""

#Create the object "trading_company1" with it's attributes
trading_company1=Trading("TraCom",2005,"Chong Wu", "We revolutionize trading.", 5000,2000,3000)

"""#### Let’s check if the methods work.
Update the sales and expenses. The sales went up by 100 and the expenses increased by 50.

📌 Use the update_sales_and_expenses method with this information.
"""

#Update the sales and expenses
trading_company1.update_sales_and_expenses(100,50)

"""After updating sale and expense informations, it is time to calculate the company revenue. 

📌 Use the calculate revenue method.
"""

#Calculate the revenue
trading_company1.calculate_revenue()

"""Finally, let’s check our company’s information."""

#Call the print_report method for trading_company1
trading_company1.print_report()