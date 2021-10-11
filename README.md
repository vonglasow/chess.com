# chess.py
```sh
python3 chess.py -h
usage: chess.py [-h] [-a] [-s] username

positional arguments:
  username

optional arguments:
  -h, --help      show this help message and exit
  -a, --archives  game archives
  -s, --stats     user stats
```

# Usage
## Get all games and create a pgn file
```sh
python3 chess.py -a username > mypgnfile.pgn
```

```sh
python3 chess.py -s username > mystatfile.json
```
