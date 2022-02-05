Hoogle Search
===============

[Hoogle](https://hoogle.haskell.org/), the Haskell API search engine, integrated into Sublime Text.


## Installation

Install using [Package Control](https://packagecontrol.io):

1. Run the `Package Control: Install Package` command
2. Search for `Hoogle Search` and install


## Usage

Perform a Hoogle search by:

1. Run `Hoogle Search: Search` in the command palette
2. Enter a Hoogle search query in the query panel (e.g., a function name, a data type, or a type signature). 
3. Select a function or data type from the results
4. Press Enter to see the full documentation from Hackage in your browser

Note that you can restrict searches to specific packages or modules, or exclude specific packages or modules, by prefixing the search with a +[package|module] or -[package|module] E.g., `+base [a] -> [a]` only searches base and `-base [a] -> [a]` excludes base from the search.

Search Hoogle on selected text by:

1. Select some text or place the cursor in a word
2. Run `Hoogle Search: Search Selection` in the command palette
3. Select a function or data type from the results
4. Press Enter to see the full documentation from Hackage in your browser

## Key Bindings

You may want to create key bindings to run these commands. Add a setting like this to your .sublime-keymap file by choosing `Preferences > KeyBindings` or running `Preferences: Key Bindings` in the command palette:
```json
[
     { "keys": ["primary-alt+shift+h"], 
       "command": "hoogle_search"},
       
     { "keys": ["alt+shift+h"], 
       "command": "hoogle_search_selection"}
]
```

## Demo
![How to](https://raw.githubusercontent.com/s4wny/HoogleSearch/master/howto.gif "How to")

## Credits

Original author: [S4wny](https://github.com/s4wny/)
Current maintainer: [Penny Chase](https://github.com/pennychase)


## Support

If there are any problems or you have suggestions, [open an issue](https://github.com/s4wny/HoogleSearch/issues).
