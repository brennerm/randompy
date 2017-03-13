# randompy
### Installation
- From source
```
git clone https://github.com/brennerm/randompy
cd randompy
sudo python3 setup.py install
```
- With pip
```
pip install randompy
```
### Example use

#### String
```
>>> randompy.string(10)
'iDa7FZl7rW'
```
#### Integer
```
>>> randompy.integer(0, 100)
15
```
#### Array
```
>>> randompy.array('123456789', 5)
['7', '5', '9', '3', '2']
```
#### Datetime
```
datetime.datetime(2016, 5, 24, 16, 34, 2, 726892)
>>> randompy.datetime(
... start=datetime.datetime(year=2016, month=1, day=1),
... end=datetime.datetime(year=2016, month=12, day=31))
datetime.datetime(2016, 2, 13, 21, 34, 58, 268978)
```

#### Mail Address
```
>>> randompy.mail()
'iYpZpde@jslx4.com'
```

#### MAC Address
```
>>> randompy.mac_address()
'fe:23:1d:1d:ec:be'
```

#### IPv4 Address
```
>>> randompy.ipv4address()
'108.146.211.120'
```

#### IPv6 Address
```
>>> randompy.ipv6address()
'7dd7:c3ee:b1b6:ba15:6bb6:c908:541a:efe4'
```
