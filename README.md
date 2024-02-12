# OSC Tester

This is a simple tool to test the OSC communication between a client and a server.

## Requirements

- Python 3
- [python-osc](https://pypi.org/project/python-osc/)
  - `pip install python-osc`

## Usage

### OSC Receiver

```bash
$ python osc_receiver.py
# Listening on 127.0.0.1:5005...
# [2024-02-12 10:37:42.448582] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:38:41.971990] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:39:00.811072] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:39:05.522840] /hoge 1 2.0 hoge (type tags: ifs)
```

### OSC Sender

```bash
$ python osc_sender.py /hoge 1 2.0 hoge
# Sending to 127.0.0.1:5005
# [2024-02-12 10:39:05.522620] /hoge 1 2.0 hoge (type tags: ifs)
```