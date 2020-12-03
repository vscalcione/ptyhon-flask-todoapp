import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world by flask'

@app.route('/item/new', methods=['POST'])
def add_item():
	# Get item from the POST body
	request_data = request.get_json()
	item = request_data['item']

	# Add item to the list
	result_data = helper.add_to_list(item)

	# Return erorr if item not added
	if result_data is None:
		response = Response("{'error': 'Item not added - " + item + "'}", status=400, mimetype='application/json')
		return response

	# Return response
	response = Response(json.dumps(result_data), mimetype='application/json')
	return response


@app.route('/items/all')
def get_all_items():
	# Get Items from the helper
	result_data = helper.get_all_items()

	# Return response
	response = Response(json.dumps(result_data), mimetype='application/json')
	return response


@app.route('/item/status', methods=['GET'])
def get_item():
	# Get parameter from the URL
	item_name = request.args.get('name')

	# Get items from the helper
	status = helper.get_item(item_name)

	# Return 404 if item not found
	if status is None:
		response = Response("{'error': 'Item not found - %s'}" % item_name, status=404, mimetype='application/json')
		return response

	# Return status
	result_data = { 'status': status }
	response = Response(json.dumps(result_data), status=200, mimetype='application/json')
	return response


@app.route('/item/update', methods=['PUT'])
def update_status():
	# Get item from the POST body
	request_data = request.get_json()
	item = request_data['item']
	status = request_data['status']

	# Update item in the list
	result_data = helper.update_status(item, status)

	# Return error if the status could not be updated
	if request_data is None:
		response = Response("{'error': 'Error updating item - '" + item + ", " + status + "}", status=400, mimetype='application/json')
		return response
	
	# Return response
	response = Response(json.dumps(result_data), mimetype='application/json')
	return response


@app.route('/item/remove', methods=['DELETE'])
def delete_item():
	# Get item from the POST body
	request_data = request.get_json()
	item = request_data['item']

	# Delete item from the list
	result_data = helper.delete_item(item)

	# Return error if the item could not be deleted
	if result_data is None:
		response = Response("{'error': 'Error deleting item - '" + item + "}", status=400, mimetype='application/json')
		return response

	# Return response
	response = Response(json.dumps(result_data), mimetype='application/json')
	return response