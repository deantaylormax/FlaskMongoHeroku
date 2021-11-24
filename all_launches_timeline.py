@app.route('/all_launches_timeline/')
def all_launches_timeline(): 
	results=mongo_db.launches.aggregate([
		{'$group': {'_id': {'year': {'$substr': ['$launch_date_utc', 0, 4]},
				    'quarter': {'$ceil': {'$divide': [{'$toInt': {'$substr': ['$launch_date_utc', 5, 2]}}, 3]}}},
			    'launches': {'$push': {'mission_patch_small': '$links.mission_patch_small', 
						   'mission_name': '$mission_name', 
						   'video_link': '$links.video_link', 
						   'wikipedia': '$links.wikipedia', 
						   'mission_patch': '$links.mission_patch'}}}}]) 
	return jsonify(list(results))