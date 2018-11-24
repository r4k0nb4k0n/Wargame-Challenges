# 4
### First impression
Encoded string.

### Trial and error
* `YzQwMzNiZmY5NGI1NjdhMTkwZTMzZmFhNTUxZjQxMWNhZWY0NDRmMg==`.
* After base64 decode using [cryptii](https://cryptii.com/), `c4033bff94b567a190e33faa551f411caef444f2`.
* After looking up in [Hashkiller](https://hashkiller.co.uk/sha1-decrypter.aspx), `a94a8fe5ccb19ba61c4c0873d391e987982fbbd3`.
* After looking up in [Hashkiller](https://hashkiller.co.uk/sha1-decrypter.aspx), `test`.

### Solution
* `=` at the end of the string means that it could be encoded using base64.
* `40` bytes means that it could be encrypted using SHA1.