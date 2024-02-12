"""OSC sender (OSC client)

This program sends the message given from args
"""
import argparse
import random
import time

from pythonosc import udp_client
from datetime import datetime
from distutils.util import strtobool

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-ip", "--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("-p", "--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  parser.add_argument("-t", "--type", default=None,
      help="The type string of arguments ( if not given, all arguments treated auto")
  parser.add_argument("address",
      help="The address to send")
  parser.add_argument("args", nargs="*", default=[],
      help="The arguments to send")
  args = parser.parse_args()

  osc_address = args.address
  osc_type_str = args.type
  _osc_args = args.args
  osc_args = []

  if osc_type_str is None:
    osc_type_str = ""
    for osc_arg in _osc_args:
      # if bool like, convert to bool
      # if int like, convert to int
      # if float like, convert to float
      # else, treat as string
      if osc_arg.lower() == "true" or osc_arg.lower() == "t":
        osc_args.append(1)
        osc_type_str += "i"
      elif osc_arg.lower() == "false" or osc_arg.lower() == "f":
        osc_args.append(0)
        osc_type_str += "i"
      else:
        try:
          osc_args.append(int(osc_arg))
          osc_type_str += "i"
        except ValueError:
          try:
            osc_args.append(float(osc_arg))
            osc_type_str += "f"
          except ValueError:
            osc_args.append(osc_arg)
            osc_type_str += "s"
  else:
    osc_type_list = osc_type_str.split("")
    for i, osc_arg in enumerate(_osc_args):
      if osc_type_list[i] == "i":
        osc_args.append(int(osc_arg))
      elif osc_type_list[i] == "f":
        osc_args.append(float(osc_arg))
      elif osc_type_list[i] == "s":
        osc_args.append(osc_arg)
      else:
        raise ValueError(f"Unknown type string: {osc_type_list[i]}")
          

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  print(f"Sending to {args.ip}:{args.port}")

  client.send_message(osc_address, osc_args)
  current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  print(f"[{current_time}] {osc_address} {' '.join([str(a) for a in osc_args])} (type tags: {osc_type_str})")
