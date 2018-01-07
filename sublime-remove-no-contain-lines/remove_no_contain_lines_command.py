import sublime
import sublime_plugin
import sys

# print(sys.version)
# print(sys.version_info)

class RemoveNoContainLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World2!")
        # allAbc = self.view.find_all('Abc')
        whole_region = sublime.Region(0, self.view.size())
        if whole_region.empty():
            return
        contents = self.view.substr(whole_region)
        contents = contents.replace('\r\n', '\n').replace('\r', '\n')
        lines = contents.split('\n')
        newlines = []
        # print('contents = ' + contents)
        # print(lines)
        # print(type(newlines))
        for i, line in enumerate(lines):
            if 'Abc' in line:
                newlines.append(line)
        # print(newlines)
        new_contents = '\n'.join(newlines) + '\n'
        # print(new_contents)
        # sublime.status_message(new_contents)

        # self.view.begin_edit() #no need for st3
        self.view.replace(edit, whole_region, new_contents)
        # self.view.end_edit(edit)
