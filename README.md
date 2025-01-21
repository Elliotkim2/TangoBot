# TangoBot
Go to [tangobot.vercel.app](https://tangobot.vercel.app/)

### Current file status for webscrape
| *filename* |   *use*   |
|------------|-----------|
|     all.py|Runs scrape and feeds into filter|
|     scrape.py|Runs the webscraper and outputs HTML in an array|
|     board.py|filters through the HTML and gets necessary info into a "TangoBoard Object"|
|     solve.py| Has code with notes to solve tango board|
|     mongodb.py|Has method to insert into mongodb database|

## FILE TREE AND DESCRIPTIONS
```
.
├── README.md
├── .github // Holds yaml files for github actions workflows.
├── cache // All old files that maybe well pull but probs not.
├── frontend // Vite-react application, for easy testing purposes
├── planning // Bunch of random files to help me keep my thoughts whatnot;
└── webscrape // Explained above
```