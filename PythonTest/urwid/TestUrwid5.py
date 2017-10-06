#!/usr/bin/env python
# coding=utf-8

import urwid


def exit_on_q(key):
    if isinstance(key, str) and key in 'qQ':
        raise urwid.ExitMainLoop()


def question():
    return urwid.Pile([urwid.Edit(('I say', 'What is you name: '))])


def answer(name):
    return urwid.Text(('I say', 'Nice to meet you, {}'.format(name)))


class ConversationListBox(urwid.ListBox):

    def __init__(self):
        self.body = urwid.SimpleFocusListWalker([question()])
        urwid.ListBox.__init__(self, self.body)

    def keypress(self, size, key):
        key = urwid.ListBox.keypress(self, size, key)
        if key != 'enter':
            return key
        focus = self.focus
        name = focus[0].edit_text
        if not name:
            raise urwid.ExitMainLoop()
        # replace or add response
        focus.contents[1:] = [(answer(name), focus.options())]
        pos = self.focus_position
        # add a new question
        self.body.insert(pos + 1, question())
        self.focus_position = pos + 1


palette = [('I say', 'default', 'default', 'bold'),]


loop = urwid.MainLoop(ConversationListBox(), palette, unhandled_input=exit_on_q)
try:
    loop.run()
except KeyboardInterrupt as e:
    print ('KeyboardInterrupt', e)


