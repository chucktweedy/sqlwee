import tkinter as tk
from tkinter import ttk
from peewee import *

db = SqliteDatabase('my_database.db')


# Assume you have a Peewee model defined
class YourModel(Model):
    name = CharField()

    # ... other fields

    class Meta:
        database = db  # Your database connection


# Create the Tkinter window and Combobox
root = tk.Tk()
combo = ttk.Combobox(root)


# Function to populate the Combobox
def populate_combobox():
    # Execute Peewee select query
    query = YourModel.select(YourModel.name)

    # Extract names from the query results
    names = [model.name for model in query]

    # Set the Combobox values
    combo['values'] = names

def on_combobox_select(event):
    selected_name = combo.get()
    # Perform actions with the selected name, e.g., query the database



# Call the function to populate the Combobox
populate_combobox()

combo.pack()
combo.bind('<<ComboboxSelected>>', on_combobox_select)
root.mainloop()




