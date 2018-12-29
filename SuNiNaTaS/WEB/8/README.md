# 8

## Inspection
* `<!-- Hint : Login 'admin' Password in 0~9999 -->`

## Solution
* [`brute_force.py`](./brute_force.py)
	- `POST` 파라미터로 전송한다.
		+ `id` : `admin`
		+ `pw` : `0`~`9999`
	- `Password Incorrect`가 보이지 않으면 맞는 것으로 간주한다.
	- Auth key가 뜬다.