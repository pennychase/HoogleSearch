# Hoogle Search plugin for Sublime Text 3

import sublime, sublime_plugin, webbrowser
import urllib.request, json
from html.parser import HTMLParser
import pprint as pp

# Global varz
results = [];



class HoogleSearchCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Hoogle Query", "", search, None, None)

def search(inp):
	global results

	query   = urllib.parse.quote_plus(inp)
	url     = "https://www.haskell.org/hoogle/?hoogle="+ query +"&mode=json"
	data    = urllib.request.urlopen(url).read().decode()
	results = json.loads(data)
	# results = data['results']


	formatedResult = []

	if results:
		for result in results:
			formatted = format(result)
			if formatted != '':
				formatedResult.append(formatted)
	else:
		formatedResult.append("No results")

	sublime.active_window().show_quick_panel(formatedResult, on_done)


def on_done(index):
	if index != -1:
		webbrowser.open(results[index]['url'], 2)


def format (result):
	if result.get('module') == None:
		return ''
	else:
		modname = result.get('module').get('name')
		if modname == None:
			return ''
	if result.get('item') == None:
		return ''
	else:
		res = result['item'].split('::')
		name = removeHtml(res[0])
		if len (res) == 1:
			ret = modname + ' ' + name
		else:
			ret = modname + ' ' + name + '::' + res[1]
	return (HTMLParser().unescape (ret))

def removeHtml (str):
	result = ''
	inHtml = False
	for c in str:
		if c == '<':
			inHtml = True
		elif c == '>':
			inHtml = False
		else:
			if not inHtml:
				result = result + c
	return (result)


