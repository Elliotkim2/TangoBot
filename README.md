# TangoBot

install playwright
run 
```
python3 scrape.py > html.txt
python3 filter.py
```
output should be the board of the day.

sql.py is a template for inserting into the database
## table in database: Boards
| *id* |  *date*  |               *board*              | *crosses* | *equals* |
|------|----------|------------------------------------|-|-|
|     1|2024-12-23|EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE| | |
### Commands
```
SELECT * FROM boards; // displays entire table
SELECT * FROM boards WHERE date="?"; // queries for what u need
```

### Current file status for webscrape
| *filename* |   *use*   |
|------------|-----------|
|     all.py|Runs scrape and feeds into filter|
|     scrape.py|Runs the webscraper and outputs HTML in an array|
|     board.py|filters through the HTML and gets necessary info into a "TangoBoard Object"|
|     mongodb.py|Has method to insert into mongodb database|
|     solve.py| Empty. Maybe put solving here, maybe do that in js unsure rn|

## FILE TREE AND DESCRIPTIONS
```
.
├── README.md
├── .github // Holds yaml files for github actions workflows.
├── cache // All old files that maybe well pull but probs not.
├── frontend // Vite-react application, might wanna switch to next; Currently only outputs simple tango board
├── planning // Bunch of random files to help me keep my thoughts whatnot;
└── webscrape // Explained above

```
## TODOS
Develop logic for actually solving the game;

Finding a way to display all this info.

