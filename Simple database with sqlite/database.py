from tkinter import *
import sqlite3
root = Tk()
root.geometry("400x600")


#create a table
'''connect = sqlite3.connect('address_book.db')
c = connect.cursor()
c.execute(""" CREATE TABLE addresses( 

			first_name text,
			last_name text,
			address text,
			city text,
			state text,
			zipcode integer
			)""")'''
def save():
	return

#create a edit function to edit a record

def edit():
	editor = Tk()
	editor.geometry("300x600")

#create a databese or connect to one

	connect = sqlite3.connect('address_book.db')


#create a cursor
	c = connect.cursor()

	record_id = delete_entry.get()

#Query the database
	c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
	records = c.fetchall()

	

#create text boxes

	first_name_editor = Entry(editor, width = 30)
	first_name_editor.grid(row = 0, column = 1, pady = (10, 0))

	last_name_editor = Entry(editor, width = 30)
	last_name_editor.grid(row = 1, column = 1)

	address_editor = Entry(editor, width = 30)
	address_editor.grid(row = 2, column = 1)

	city_editor = Entry(editor, width = 30)
	city_editor.grid(row = 3, column = 1)

	state_editor = Entry(editor, width = 30)
	state_editor.grid(row = 4, column = 1)

	zipcode_editor = Entry(editor, width = 30)
	zipcode_editor.grid(row = 5, column = 1)




#create text box labels
	first_name_label = Label(editor, text = "First Name") 
	first_name_label.grid(row = 0, column = 0, pady = (10, 0))

	last_name_label = Label(editor, text = "Last Name") 
	last_name_label.grid(row = 1, column = 0)

	address_label = Label(editor, text = "Address") 
	address_label.grid(row = 2, column = 0)

	city_label = Label(editor, text = "City") 
	city_label.grid(row = 3, column = 0)

	state_label = Label(editor, text = "State") 
	state_label.grid(row = 4, column = 0)

	zipcode_label = Label(editor, text = "Zipcode") 
	zipcode_label.grid(row = 5, column = 0)

#loop through results
	for record in records:
		first_name_editor.insert(0, record[0])
		last_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])

#creat a button to save the record

	save_button = Button(editor, text = 'Save Record', command = save)
	save_button.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)
#exit button for editor
	exit1_button = Button(editor, text = 'Exit Editor',bg = 'black', fg = 'white', command = editor.quit)
	exit1_button.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 105)

#create function to delete a record

def delete():
#create a databese or connect to one

			connect = sqlite3.connect('address_book.db')


#create a cursor
			c = connect.cursor()

#delete a record
			c.execute("DELETE from addresses WHERE oid = " + delete_entry.get())






#commit changes

			connect.commit()

#close connection

			connect.close()




#create Submit Function for Database

def submit():
#create a databese or connect to one

			connect = sqlite3.connect('address_book.db')


#create a cursor
			c = connect.cursor()

#insert into table

			c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",


		    		 	{ 
			    		    'first_name' : first_name.get(),
			    		    'last_name'  : last_name.get(),
			    		    'address'    : address.get(),
			    		    'city'       : city.get(),
			    		    'state'      : state.get(),
			    		    'zipcode'    : zipcode.get()


		    		 	})

#commit changes

			connect.commit()

#close connection

			connect.close()

#clear text boxes
			first_name.delete(0, END)
			last_name.delete(0, END)
			address.delete(0, END)
			city.delete(0, END)
			state.delete(0, END)
			zipcode.delete(0, END)


#create query function

def query():
#create a databese or connect to one

			connect = sqlite3.connect('address_book.db')


#create a cursor
			c = connect.cursor()

#Query the database
			c.execute("SELECT *, oid FROM addresses")
			records = c.fetchall()
			
			print_record = ''

			for record in records:
				print_record += str(record[0]) + " " + str(record[1]) +"\t"+ str(record[6]) +'\n'
			print_label = Label(root, text = print_record)
			print_label.grid(row = 11, column = 0, columnspan = 2)

#commit changes

			connect.commit()

#close connection

			connect.close()






#create text boxes

first_name = Entry(root, width = 30)
first_name.grid(row = 0, column = 1, pady = (10, 0))

last_name = Entry(root, width = 30)
last_name.grid(row = 1, column = 1)

address = Entry(root, width = 30)
address.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zipcode = Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)

delete_entry = Entry(root, width = 30)
delete_entry.grid(row = 8, column = 1 )


#create text box labels
first_name_label = Label(root, text = "First Name") 
first_name_label.grid(row = 0, column = 0, pady = (10, 0))

last_name_label = Label(root, text = "Last Name") 
last_name_label.grid(row = 1, column = 0)

address_label = Label(root, text = "Address") 
address_label.grid(row = 2, column = 0)

city_label = Label(root, text = "City") 
city_label.grid(row = 3, column = 0)

state_label = Label(root, text = "State") 
state_label.grid(row = 4, column = 0)

zipcode_label = Label(root, text = "Zipcode") 
zipcode_label.grid(row = 5, column = 0)

delete_label = Label(root, text = "Enrollment ID")
delete_label.grid(row = 8, column = 0)

#create buttons

submit_button = Button(root, text = "Add Record to Database", command = submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#create query buttons

query_button = Button(root, text = "Show Query", command = query)
query_button.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 133)


#create delete button
delete_button = Button(root, text = "Delete Record", command = delete)
delete_button.grid(row = 9, column = 0, columnspan = 2, pady = 10, ipadx = 130)

#create edit button

edit_button = Button(root, text = "Edit Record", command = edit)
edit_button.grid(row = 10, column = 0, columnspan = 2, pady = 10, ipadx = 136)


#create exit button
exit_button = Button(root, text = 'Exit', command = root.quit, bg = 'black', fg = 'white')
exit_button.grid(row = 12, column = 0 , columnspan = 2, pady = 20, ipadx = 100)













root.mainloop()