from app.models.order import *

order1 = Order("John Smith", "20.1.21", 1, "Fender", "Telecaster")
order2 = Order("Anne Jones", "19.1.21", 1, "Gibson", "Les Paul")
order3 = Order("Ken Davidson", "18.1.21", 2, "Fender", "Stratocaster")
order4 = Order("Jane Olsen", "17.1.21", 3, "Yamaha", "Pacifica")
orders = [order1, order2, order3, order4]