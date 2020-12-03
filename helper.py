import sqlite3

DB_PATH= './todo.db'
NOTSTARTED = 'Not started'
INPROGRESS = 'In progress'
COMPLETED = 'completed'

def add_to_list(item):
	try:
		connection = sqlite3.connect(DB_PATH)

		# Once a connection has been established, we use the cursor,
		# an object to execute queries
		cursor = connection.cursor()

		# Keep the initial status as Non started
		cursor.execute('insert into items(item, status) values (?,?)', (item, NOTSTARTED))

		# We commit to save the change
		connection.commit()
		return {"item": item, "status": NOTSTARTED}
	except Exception as e:
		print('Error: ', e)
		return None


def get_all_items():
	try:
		connection = sqlite3.connect(DB_PATH)
		cursor = connection.cursor()
		cursor.execute('select * from items')
		rows = cursor.fetchall()
		return { "count": len(rows), "items": rows }
	except Exception as e:
		print('Error: ', e)
		return None


def get_item(item):
	try:
		connection = sqlite3.connect(DB_PATH)
		cursor = connection.cursor()
		cursor.execute("select status from items where item='%s'" % item)
		status = cursor.fetchone()[0]
		return status
	except Exception as e:
		print('Error: ', e)
		return None


def update_status(item, status):
	# Check if the passed status is a valid value
	if (status.lower().strip() == 'not started'):
		status = NOTSTARTED
	elif (status.lower().strip() == 'in progress'):
		status = INPROGRESS
	elif (status.lower().strip() == 'completed'):
		status = COMPLETED
	else:
		print('Invalid status:' + status)
		return None

	try:
		connection = sqlite3.connect(DB_PATH)
		cursor = connection.cursor()
		cursor.execute('update items set status=? where item=?', (status, item))
		connection.commit()
		return { item: status }
	except Exception as e:
		print('Error: ', e)
		return None


def delete_item(item):  
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where item=?', (item,))
        conn.commit()
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None