"""OSC receiver (OSC server)

This program listens to all OSC addresses, and prints information about
received packets.
"""
import argparse
import math

from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

from typing import List, Any
from datetime import datetime

def get_type_tags(args: List[Any]) -> str:
    type_tags = ""
    for arg in args:
        if isinstance(arg, int):
            type_tags += "i"
        elif isinstance(arg, float):
            type_tags += "f"
        elif isinstance(arg, str):
            type_tags += "s"
        # blob
        elif isinstance(arg, bytes):
            type_tags += "b"
        else:
            raise ValueError(f"Unknown type {type(arg)}")
    return type_tags

def osc_handler(addr, *args: List[Any]):
    # output should be: [2024-12-12 12:12:12.333] /test 1 2 3
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    args_str = " ".join([str(a) for a in args])
    type_tags = get_type_tags(args)
    print(f"[{current_time}] {addr} {args_str} (type tags: {type_tags})")

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-ip","--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("-p","--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = Dispatcher()
  dispatcher.map("/*", osc_handler)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print(f"Listening on {args.ip}:{args.port}... (Ctrl+C to quit)")
  server.serve_forever()