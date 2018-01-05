import sublime
import sublime_plugin


class RemoveNoContainLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World2!")
