#!/usr/bin/env python
# coding=utf-8

import urwid


def exit_on_q(key):
    # print ('type(key)', type(key), key)
    # if type(key) is str and key in 'qQ':
    if isinstance(key, str) and key in 'qQ':
        raise urwid.ExitMainLoop()

palette = [
    ('banner', '', '', '', '#ffa', '#60d')
    , ('streak', '', '', '', 'g50', '#60a')
    , ('inside', '', '', '', 'g38', '#808')
    , ('outside', '', '', '', 'g27', '#a06')
    , ('bg', '', '', '', 'g7', '#d06')
]

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
attr_map = urwid.AttrMap(placeholder, 'bg')
attr_map.original_widget = urwid.Filler(urwid.Pile([]))
loop.widget = attr_map

div = urwid.Divider()
outside = urwid.AttrMap(div, 'outside')
inside = urwid.AttrMap(div, 'inside')
txt = urwid.Text(('banner', 'Hello World'), align='center')
streak = urwid.AttrMap(txt, 'streak')
pile = attr_map.base_widget
for item in [outside, inside, streak, inside, outside]:
    pile.contents.append((item, pile.options()))

loop.run()
