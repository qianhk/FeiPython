#!/usr/bin/env python
# coding=utf-8

import urwid


def show_or_exit(key):
    if key in 'qQ':
        raise urwid.ExitMainLoop()
    txt.set_text(('banner', key))


palette = [
    ('banner', '', '', '', '#ffa', '#60d')
    , ('streak', '', '', '', 'g50', '#60a')
    , ('inside', '', '', '', 'g38', '#808')
    , ('outside', '', '', '', 'g27', '#a06')
    , ('bg', '', '', '', 'g7', '#d06')
]

txt = urwid.Text(('banner', 'Hello World'), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1, 'top')
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=show_or_exit)
loop.run()
