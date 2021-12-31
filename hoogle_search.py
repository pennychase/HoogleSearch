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

# Each Hoogle result is dictionary with the keys: docs, item, module, package, type, and url.
# To make the results look the hoogle application, create a string with module name and type signature.
# The module name is in the module dictionary and the type signature is the item string (the function name
# may be embedded in html tags). Some entries may be missing some of these elements, and we skip them.
def format (result):
	if result.get('module') == None:
		return ''
	else:
		modname = result.get('module').get('name') # get the module name if it exists
		if modname == None:
			return ''
	if result.get('item') == None:
		return ''
	else:
		res = result['item'].split('::')  # split type signature into name and type
		name = removeHtml(res[0])
		if len (res) == 1:                # the type might not be included in the entry
			ret = modname + ' ' + name
		else:
			ret = modname + ' ' + name + '::' + res[1]
	return (HTMLParser().unescape (ret))   # decode html entities

# Remove html tags by skipping over anything between < and >. There seems to be variation in the tags used
# in Hoogle entries, so this approach removes everything that isn't part of the item's name.
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


