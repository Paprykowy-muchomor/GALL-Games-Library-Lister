# GALL - Games Library Lister

Simple Python tool for generating a sorted list of games stored on disk.

## Features

- Scans folders recursively
- Supports decade/year folder structure
- Sorts games alphabetically
- Creates GAME_LIST.txt
- UTF-8 output

## Expected folder structure

Drive
│
├── 1980-1989
│   ├── 1980
│   │   ├── Pac-Man
│   │   ├── Defender
│
├── 1990-1999
│   ├── 1993
│   │   ├── Doom
│   │   ├── Syndicate

## Example output

1993
------------------------------
Doom
Syndicate

## Requirements

Python 3.10+

## Usage

```bash
python gall.py
```
## Screenshoot
<img width="633" height="387" alt="image" src="https://github.com/user-attachments/assets/fdb09fee-a6b2-477b-958f-c983c72f295b" />
