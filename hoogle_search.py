# Hoogle Search plugin for Sublime Text 2
# (Hoogle query interface)
# Copyright (C) 2012 Tom Savage
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import sublime, sublime_plugin, webbrowser

class HoogleSearchCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Hoogle Query", "", search, None, None)

def search(inp):
	query = inp.replace("=", "%3d").replace(" ", "+")
	webbrowser.open("http://www.haskell.org/hoogle/?hoogle=" + query)
