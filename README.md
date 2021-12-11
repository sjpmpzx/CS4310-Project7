## Project Structure
```
race.py     - With race condiction (Assignment 1)
no_race.py  - Without race condiction (Assignment 2)
```

## How to Run
- Setup Python environment
- `python ./race.py` or `python ./no_race.py`

## Note
 - Uncomment line 36-38 of **race.py** to also dectect race conditions when producer is too slow.
 - **race.py** will stop when it detects a race condition
 - **no_race.py** will run forever and never report a race condition