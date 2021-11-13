# chess.py
```sh
python3 chess.py -h
usage: chess.py [-h] [-u USERNAME] [-t TOURNAMENT] [-a] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        chess.com username
  -t TOURNAMENT, --tournament TOURNAMENT
                        tournament ID (ex: poulet-1484723)
  -a, --archives        game archives
  -s, --stats           user stats
```

# Usage
## Get all games and create a pgn file
```sh
python3 chess.py -a -u username > mypgnfile.pgn
```

```sh
python3 chess.py -s -u username > mystatfile.json
```

```sh
python3 chess.py -t poulet-1484723
[{'username': 'g0g0lem', 'points': 33, 'place_finish': 1}, {'username': 'frigoriste69', 'points': 31, 'place_finish': 2}, {'username': 'flomefi', 'points': 26, 'place_finish': 3}]
```
