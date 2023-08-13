#!/usr/bin/env python3
# coding=utf-8

import frida


def on_message(message, data):
    print("[on_message] message:", message, "data:", data)


session = frida.attach("EncodingConvert")

script = session.create_script("""
rpc.exports.enumerateModules = () => {
  return Process.enumerateModules();
};
""")
script.on("message", on_message)
script.load()

print('a haha')
# print([m["name"] for m in script.exports_sync.enumerate_modules()])
