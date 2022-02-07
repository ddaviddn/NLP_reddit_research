Purpose Statement: Compare and Contrast language used in far-left/far-right political pages.

# NLP_reddit_research

May 5th, 2021


 ________________
< NLP_reddit README >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

README
-------------------------------------
In this semester project, I will be using a Reddit database to analyze the language used

in politically-focused subreddits. Specifically striving to compare and contrast the language

used in politically right/left reddit community pages. Applying different methods of Natural

Language Processing techniques that I learned starting from the beginning of the research,

these techniques will assist in getting a better understanding of the words used and help

us find any distinctions in the language for these two opposing political spectrums. From

learning how to extract and query from the database, to learning about one of the most

important steps in the NLP workflow–the text processing phase, and later on learning how to

turn comments into numerically-represented vectors. Each of these newly acquired methods

led to the opportunity to analyze and extract valuable information through our open-source

social network database.

------------
The hardware specifications are (Lenovo	T450s):

GPU: 2.3 GHz core_i7

CPU: Intel HD Graphics 5500

RAM: 8 GB DDR3L Available

------------





FILES

-------------------------------------
:Final_Project_(Left).ipynb:

This is the processing of politically left subreddit pages as well as the word representations 

of politically left subreddit pages.


-------------------------------------

-------------------------------------
:Final_Project_(Right).ipynb:

This is the processing of politically right subreddit pages as well as the word representations 

of politically right subreddit pages.


-------------------------------------
:compiled_excel.xlsx:

Outputting results into a single excel file. Also has visualizations of each vector representation. 

Will show 10 most similar words for each word of interest.


-------------------------------------
:query-builder.py: 

Connecting to MongoDB and acquiring the data from the database. Taking in user input for 

looping through the different file paths.


-------------------------------------
:text-processor.py:

This is the text preprocessing techniques used on the textual data

-------------------------------------
