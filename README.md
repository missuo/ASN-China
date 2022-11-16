<!--
 * @Author: Vincent Young
 * @Date: 2022-11-17 02:07:33
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-11-17 03:32:10
 * @FilePath: /ASN-China/README.md
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
-->
# ASN-China
This is a Chinese ASN and IP list maintenance library.

## Features
- Automatic daily updates
- Reliable and accurate source

## Use in proxy app
### Quantumult X
```
[filter_remote]
# China ASN List
https://raw.githubusercontent.com/missuo/ASN-China/main/ASN.China.list, tag=ChinaASN, force-policy=direct, update-interval=86400, opt-parser=true, enabled=true
```

### Surge
```
[Rule]
# > China ASN List
RULE-SET, https://raw.githubusercontent.com/missuo/ASN-China/main/ASN.China.list, Direct
```


## Data Source
### ASN Information
- [bgp.he.net](https://bgp.he.net/country/CN)

### IP Information
- [cbuijs/ipasn](https://github.com/cbuijs/ipasn)

### License
MIT License

Copyright (c) 2022 Vincent Young

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


