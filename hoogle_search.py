# Hoogle Search plugin for Sublime Text 3

import sublime, sublime_plugin, webbrowser
import urllib.request, json
import pprint as pp

# Global varz
results = [];

class HoogleSearchCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Hoogle Query", "", search, None, None)

def search(inp):
	global results;

	query   = inp.replace("=", "%3d").replace(" ", "+")
	url     = "https://www.haskell.org/hoogle/?hoogle="+ query +"&mode=json"
	data    = urllib.request.urlopen(url).read().decode();
	data 	= json.loads(data)
	results = data['results']


	formatedResult = []

	if results:
		for result in results:
			formatedResult.append(result['self'])
	else:
		formatedResult.append("No results")

	sublime.active_window().show_quick_panel(formatedResult, on_done)


def on_done(index):
	webbrowser.open(results[index]['location'], 2);