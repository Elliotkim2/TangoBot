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
|     sql.py|has methods to insert/get into/from sqlite database|
|     mongodb.py|does not work. if we wanna do a mongo db database?|
|     print.py| prints hello world to file (for yaml testing purposes)|
|     solve.py| Empty. Maybe put solving here, maybe do that in js unsure rn|
### .github/workflows
YAML files run scripts on github to automatically do things so we dont have to.

Goal is to be able to upload them to a database. Currently jsut saves it in github actions archive. Want to at least get it to save in repo if not to database soon.

if database, choose one and go with it.

If repo:

```
    // Change names of files to dates and create new hierarchical structure but this looks like supposed yaml file to add
    - name: Configure Git
      run: |
        git config --global user.name "GitHub Actions"
        git config --global user.email "actions@github.com"

    - name: Push hello_world.txt to repository
      working-directory: ./webscrape
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        git add log.txt
        git commit -m "Add log.txt from workflow"
        git push origin main
```
Also consider: 

	1.	GITHUB_TOKEN: GitHub automatically provides a token (secrets.GITHUB_TOKEN) for authentication in workflows. It allows you to push changes to the repository.
	2.	Repository Permissions: Ensure the workflow has write permissions to the repository. You can configure this in the repository settings under Settings > Actions > Workflow permissions:
	•	Check Read and write permissions.




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
Figure out database and yaml files.

Develop logic for actually solving the game;

Finding a way to display all this info.

