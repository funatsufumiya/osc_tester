"""Small example OSC client

This program sends random values to the /filter address,
waiting for 1 second between each value.
"""
import argparse
import random
import time

from pythonosc import udp_client
from datetime import datetime


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-ip", "--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("-p", "--port", type=int, default=5005,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  print(f"Sending to {args.ip}:{args.port} (Ctrl+C to quit)...")

  try:
    while True:
      v = random.random()
      client.send_message("/filter", v)
      current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
      print(f"[{current_time}] /filter {v}")
      time.sleep(1)
  except KeyboardInterrupt:
    print("Exiting...")
    pass
