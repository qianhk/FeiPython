#!/usr/bin/env python
# coding=utf-8

import urwid


def exit_on_q(key):
    if isinstance(key, str) and key in 'qQ':
        pass
        # raise urwid.ExitMainLoop()


choices = u'选项1 选项2 选项3 选项4 选项5 选项6'.split()


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button, choice):
    response = urwid.Text(['You chose ', choice, '\n'])
    done = urwid.Button('Ok')
    urwid.connect_signal(done, 'click', exit_program)
    main.original_widget = urwid.Filler(urwid.Pile(
        [response, urwid.AttrMap(done, None, focus_map='reversed')]))


def exit_program(button):
    raise urwid.ExitMainLoop()


menuList = menu('请选择', choices)
main = urwid.Padding(menuList, left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill('\N{MEDIUM SHADE}'),
                    align='center', width=('relative', 60),
                    valign='middle', height=('relative', 60),
                    min_width=20, min_height=9)
# top = urwid.Overlay(main, urwid.SolidFill(' '),
#                     align='left', width=('relative', 50),
#                     valign='top', height=('relative', 30))

loop = urwid.MainLoop(top, palette=[('reversed', 'standout', '')], unhandled_input=exit_on_q)
try:
    loop.run()
except KeyboardInterrupt as e:
    print ('KeyboardInterrupt', e)
