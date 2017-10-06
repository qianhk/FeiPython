#!/usr/bin/env python
# coding=utf-8

import urwid


def exit_on_q(key):
    if isinstance(key, str) and key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [('I say', 'default', 'default', 'bold'),]

ask = urwid.Edit(('I say', 'What is your name: '), 'KaiKai')
reply = urwid.Text('')
button = urwid.Button('Exit')
div = urwid.Divider()
pile = urwid.Pile([ask, div, reply, div, button])
top = urwid.Filler(pile, valign='top')


def on_ask_change(edit, new_edit_text):
    reply.set_text(('I say', 'Nice to meet you, {}'.format(new_edit_text)))


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

urwid.connect_signal(ask, 'change', on_ask_change)
urwid.connect_signal(button, 'click', on_exit_clicked)

loop = urwid.MainLoop(top, palette, unhandled_input=exit_on_q)
try:
    loop.run()
except KeyboardInterrupt as e:
    print ('KeyboardInterrupt', e)


