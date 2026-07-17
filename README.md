# GALL - Games Library Lister

Simple Python tool for generating a sorted list of games stored on disk.

## Backstory

I built a small Python CLI tool called GALL (Games Library Lister) — and honestly, it started as a personal necessity rather than a portfolio project.
With publishers' practices getting worse over time (rumors of physical media being phased out, entire libraries — games,
and even things like movies — sometimes disappearing from people's accounts),
I started archiving my legally-owned GOG.com installers onto external hard drives as a precaution.
The problem: after a while, the folders get huge, and it becomes hard to keep track of what's already archived. 
GALL solves that — it scans a drive following a simple Decade/Year/Game folder structure and generates a clean, sorted GAME_LIST.txt. 
Now I can check in seconds what I've already backed up before buying or downloading the next batch.
Simple tool, real problem, does exactly what it needs to.

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
## Screenshoots

CLI
<img width="633" height="387" alt="image" src="https://github.com/user-attachments/assets/fdb09fee-a6b2-477b-958f-c983c72f295b" />

OUTPUT
<img width="1175" height="1212" alt="image" src="https://github.com/user-attachments/assets/57cb3ba5-9a42-4aed-8165-a8c7b06bde3e" />

