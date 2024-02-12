# OSC Tester (Python)

This is a simple tool to test the OSC communication between a client and a server.

## Requirements

- Python 3
- [python-osc](https://pypi.org/project/python-osc/)
  - `pip install python-osc`

## Usage

### OSC Receiver

(Check `python osc_receiver.py -h` for options)

```bash
$ python osc_receiver.py
# Listening on 127.0.0.1:5005...
# [2024-02-12 10:37:42.448582] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:38:41.971990] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:39:00.811072] /hoge 1 2 hoge (type tags: iis)
# [2024-02-12 10:39:05.522840] /hoge 1 2.0 hoge (type tags: ifs)
```

### OSC Sender

(Check `python osc_sender.py -h` for options)

```bash
$ python osc_sender.py /hoge 1 2.0 hoge
# Sending to 127.0.0.1:5005
# [2024-02-12 10:39:05.522620] /hoge 1 2.0 hoge (type tags: ifs)
```

### Sample sender

(Check `python sample_sender.py -h` for options)

```bash
$ python sample_sender.py
# Sending to 127.0.0.1:5005... (Ctrl+C to quit)
# [2024-02-12 10:45:16.000462] /filter 0.6610950773002804
# [2024-02-12 10:45:17.002817] /filter 0.8154223208829204
# [2024-02-12 10:45:18.004950] /filter 0.37209750414016063
# [2024-02-12 10:45:19.010492] /filter 0.46979363082349024
```
