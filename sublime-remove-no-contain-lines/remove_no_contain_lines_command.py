import sublime
import sublime_plugin


# print(sys.version)
# print(sys.version_info)

class RemoveNoContainLinesTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        print('TextCommand args')
        print(args)
        keep_word = args['keep_word']
        # print(keep_word)

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
            if keep_word in line:
                newlines.append(line)
        # print(newlines)
        new_contents = '\n'.join(newlines) + '\n'
        # print(new_contents)
        # sublime.status_message(new_contents)

        # self.view.begin_edit() #no need for st3
        self.view.replace(edit, whole_region, new_contents)
        # self.view.end_edit(edit)


class RemoveNoContainLinesCommand(sublime_plugin.WindowCommand):

    def run(self):
        # window = sublime.active_window()
        # self.tmpEdit = edit
        self.window.show_input_panel('请输入需包含的字符串', '', self.on_done, None, self.on_cancel)
        # print('after show_input_panel')

    def on_cancel(self):
        self.edit_token = None
        self.args = None
        sublime.status_message('cancel operation')

    def on_done(self, input):
        # self.view.insert(edit, 0, "Hello, World2!")
        # allAbc = self.view.find_all('Abc')
        if len(input) == 0:
            sublime.status_message('没有输入，取消操作')
            return
        view = self.window.active_view()
        view.run_command('remove_no_contain_lines_text', {'keep_word': input})
