Added fix for "line 313, in _read_loop line = buf.read_line().strip()AttributeError: 'NoneType' object has no attribute 'strip'"

Replace streaming.py file with this updated version of it or simply add the fix manually into the tweepy streaming.py file.

Fix replaces:
line = but.read_line().strip()
with 	
line = buf.read_line()
if line:
    line = line.strip()