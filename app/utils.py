from datetime import datetime

def long_ago(seconds):
	if seconds < 60:
		return f"{round(seconds)} seconds ago"
	elif 60 <= seconds < 3600:
		return f"{round(seconds/60)} minutes ago"
	elif 3600 <= seconds < 86400:
		return f"{round(seconds/3600)} hours ago"
	elif 86400 <= seconds < 604800:
		if round(seconds/86400) == 1:
			return "yesterday"
		return f"{round(seconds/86400)} days ago"
	elif 604800 <= seconds < 2592000:
		if round(seconds/604800) == 1:
			return "last week"
		return f"{round(seconds/604800)} weeks ago"
	elif 2592000 <= seconds < 31556952:
		if round(seconds/2592000) == 1:
			return "last month"
		return f"{round(seconds/2592000)} months ago"
	elif seconds >= 31556952:
		if round(seconds/31556952) == 1:
			return "last year"
		return f"{round(seconds/31556952)} years ago"
