# Hoogle Search plugin for Sublime Text 3

import sublime, sublime_plugin, webbrowser
import urllib.request, json, re
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
	url     = "https://hoogle.haskell.org/?hoogle="+ query +"&mode=json"
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
	if result.get('module') == None:					# Get module name if it exists
		return ''
	else:
		modname = result.get('module').get('name') 		
		if modname == None:
			return ''

	if result.get('item') == None:						# Get type signature
		return ''
	else:
		res = result['item'].split('::')  				# split type siganture into name and type
		name = re.sub('<[^<]+?>', '', res[0])			# remove all html tags
		if len (res) == 1:                				# the type might not be included
			ret = modname + ' ' + name
		else:
			ret = modname + ' ' + name + '::' + res[1]

	return (HTMLParser().unescape (ret))   				# decode html entities


