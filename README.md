# COVID-19 Dashboard
Hello there! Welcome to the corona dashboard made by team 1!

**We are live: https://share.streamlit.io/itsmesafak/covid_dashboard/main.py**

---
## Setup and installations
First of all, lets clone the repo. You can do this by opening your command prompt (terminal) and executing the following command:
```sh
git clone https://github.com/ItsMeSafak/covid_dashboard
```
This creates a copy of the project on you local machine! There may occur an error saying that 'git is unrecognized'. This means that you should install git first. 
- *Installing git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git*

So before we start into acutal coding, we have to make sure that we configure the correct environment and install the required packages. 
For starters, I highly reccomend using PyCharm. It can be a bit tricky at first, but once you setup everything your good to go! 

Open up your **Anaconda Navigator** and on the main screen you should see a program called 'PyCharm Professional' and **install** it, which looks something like this:

![Pycharm](assets/py1.PNG) 

Once you have it installed, run it so we can configure the environment and interpreter. If it asks you to import settings, you can just skip that part. You should be getting the screen that tells you to create or open an existing project. Open the **covid_dashboard** folder. Now you should be seeing a grey-ish screen. This is basically the PyCharm environment. To the left you can see a few tabs whereas we should be focussing on the **Project** tab, press it. Now we can see the folder structure of our covid_dashboard. 

Before we can actually start to run and edit the code, we need to configure the interpreter and environment we are currently working in. At the bottom right, there should be a tab name **< No Interpreter >**, press it and press the **Add interpreter...** option. This open ups a new window and at the left you can see the **Conda environment** select that one. Now you, select the **Existing environment** option and try to locate the *python.exe* file in your anaconda3 folder, mine looked something like this: `E:\MINOR\anaconda3\python.exe` . After you configured the interpreter, now you should configure the **Conda executable** which is also in the anaconda3 folder. Mine looked like this: `E:\MINOR\anaconda3\Scripts\conda.exe`. If you are still struggling, refer to these links
- https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/
- https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter

Awesome! No we are ready to go (actually not, but we can start to code). It's time to open up the magic wand aka the **Terminal**. You can locate the terminal at the tabs left-below of your screen. Open a terminal and execute the following command:
```sh 
pip install -r requirements.txt
```
It may be saying things like 'Requirements already satisfied', but thats a good thing. Once you can enter another command in the terminal, that means the installation of the packages is complete. Also in case you add new packages, add them to the requirements.txt file and rerun the same script.

---
## Project structure
Let's take a look at the project structure shall we (don't mind the funky colors):

![Project structure](assets/py2.PNG)

The main files and folder we should be focussing on are as follows:
- [components](components): this folder consists of the plots and graphs we will be creating.
- [utils](utils): the utils folder consists of handy functions and variables we may need during development.
- [data](data): the data folder consists of csv files of the datasets.
- [main.py](main.py): the main file is the starting point of our whole application.

---
## Executing the code
To run the streamlit application locally, simply execute the following command:
```sh
streamlit run main.py
```
After compiling the code, it should tell you that you can view the app in your browser at the URL *http://localhost:8501* or something like that. If not, there may have gone something wrong with the installation of packages. Perhaps rerun the command above.

---
## Commit changes
Committing changes can be a bit of a pain in the a**. But to ease it out, I made a [commit](commit.sh) script that does all the work for you. Before we get into let, let's discuss the theory. 

While working on a project, we would like to seperate the development and main or master versions of the project. In this project, there are 2 branches: development and master. All our progress should be pushed on the development branch and all that is finished and done should be pushed on the master branch. The development branch is exactly the same as master, but a bit more messy.

**IMPORTANT!** When working on the project, please stay in the **development** branch. You can do this by simply executing the following command:
```sh
git checkout development
```

Now you are allowed to break everything (but don't). Now in order to push your changes live, we need to open up the terminal again (left-below **Terminal** tab) and this time press the **down arrow** and select command prompt. Now you can execute the following command:
```sh
commit.sh [your message]
```
Note that the [your message] part should be in quotes, so you get something like 
```sh
commit.sh "this is my message"
```

In case an error pops up, please contact me or check out the following link (if you dare):
- https://www.jetbrains.com/help/pycharm/resolving-conflicts.html#distributed-version-control-systems
- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
 
 ---
 ## API/dataset usage

 ### RIVM Covid-19
 Alright so, we made use of the COVID-19 dataset, which gets delivered and updated every day by the government of the Netherlands. This open source consists of various sets of data regarding the COVI-19 cases in Holland. 
- Base url: https://data.rivm.nl/covid-19/
- Data set (both csv and json are available) example: https://data.rivm.nl/covid-19/COVID-19_Infectieradar_symptomen_per_dag.csv
- METADATA for the given dataset: https://data.rivm.nl/covid-19/COVID-19_Infectieradar_symptomen_per_dag.html. This page covers every info about the data, what it is about and what the columns represent.

We paste this url into the read_csv() function of pandas, seperated by a semicolon (;), and it immediately parses it into a dataframe. We then use this dataframe to show statistics.

*Reference to RIVM Covid-19: https://data.rivm.nl/covid-19/*

### GoogleNews
We also made use of the GoogleNews package. This package is a simple API for fetching news articles from Google. At the top of our dashboard you can see a random recent article regarding the corona virus in the Netherlands.

How the package works is as follows:
- First we instantiate the GoogleNews object and we pass in some arguments. Think of arguments such as the language, region and period of posted articles.
```py
googlenews = GoogleNews(lang='nl', region='NL', period='7d')
```
- Then we execute the search by calling the .search() method, were we pass in this case 'Corona virus' as the topic we should be searching on.
```py
googlenews.search('Corona virus')
```
- We then fetch the results, by calling the .results() function.
```py
news_dict = googlenews.result()
```
This returns a list of JSON objects looking like this:
```json
[{
   "title":"LIVE | Kabinet trekt 95 miljoen uit voor coronahulp arme landen, medicijn Merck lijkt effectief tegen alle varianten",
   "media":"De Stentor",
   "date":"3 hours ago",
   "datetime":"2021-12-12",
   "desc":"CoronavirusEen experimenteel coronamedicijn van farmaceut Merck, molnupiravir genaamd, lijkt effectief te zijn tegen alle bekende varianten van het virus.",
   "link":"www.destentor.nl/binnenland/live-kabinet-trekt-95-miljoen-uit-voor-coronahulp-arme-landen-medicijn-merck-lijkt-effectief-tegen-alle-varianten~a33336f0/",
   "img":"data:image/gif;base64,R0lGODlhAQABAIAAAP"
}, ...]
```
- The result() function returns a page of 10 articles. Every page has a maximum of 10 news articles. It is also possible to select a specific page by executing the get_page() function, where you pass the pagenumber as argument.

*Reference to GoogleNews: https://pypi.org/project/GoogleNews/*

 ---
 ## Handy links
- [Streamlit cheat sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)
- [How to actually use git properly](https://www.freecodecamp.org/news/how-to-use-git-efficiently-54320a236369/)
- [Streamlit dashboard example(s)](https://streamlit.io/gallery)


*Now you are ready to go! Happy coding :smile:!*
