#!/usr/bin/env python
# coding=utf-8

import urwid


def exit_on_q(key):
    if isinstance(key, str) and key in 'qQ':
        raise urwid.ExitMainLoop()


class QuestionBox(urwid.Filler):
    def keypress(self, size, key):
        if key != 'enter':
            return urwid.Filler.keypress(self, size, key)
        if len(edit.edit_text) == 0:
            pass
        else:
            self.original_widget = urwid.Text('Nice to meet you, {}.\n\nPress Q to exit.'.format(edit.edit_text))

edit = urwid.Edit('What is your name: ')
fill = QuestionBox(edit)

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)

loop.run()
