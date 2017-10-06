#!/usr/bin/env python
# coding=utf-8

import urwid

print ('in menu.py', __name__)


def exit_on_q(key):
    if isinstance(key, str) and key in 'qQ':
        pass
        # raise urwid.ExitMainLoop()


choice_value = ''
choice_index = -1


def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    index = 0
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, index)
        index += 1
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def item_chosen(button, index):
    print ('in menu.py item_chosen', button, index)
    global choice_value
    global choice_index
    choice_value = button.label
    choice_index = index
    exit_program(None)


def exit_program(button):
    raise urwid.ExitMainLoop()


def showMenuWithTitleAndList(title, list):
    global choice_value
    global choice_index
    choice_value = ''
    choice_index = -1
    menuList = menu(title, list)
    main = urwid.Padding(menuList, left=2, right=2)
    top = urwid.Overlay(main, urwid.SolidFill(' '),
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

