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
:CoverPage_ID_8:

This is the separated cover page


-------------------------------------

-------------------------------------
:preprocessing_ID_8.ipynb:

This is the full preprocessing procedure we decided to run on the data. 


-------------------------------------
:modeling_ID_8.ipynb:

This is the full modeling procedure we decided to run on the data.


-------------------------------------
:full_script_ID_8.py: 

This is the combination of preprocessing and modeling into one python script (if preferred to be run in a .py file).

There may be an issue with the current path, the path in the code needs to be changed before it successfully runs.

On google colab's hardware, the script took 31.241 seconds to run.


-------------------------------------
:Report_ID_8.pdf:

As the name states, this is the report created for this project.


-------------------------------------
:predictions_ID_8.csv:

This is the model predictions that we came up with. 

Dataframe of
| ucfID | increase_amt | credit_line_amount | new_credit_line |

increase_amt - our model's predicted increase amount
credit_line_amount - the user's ORIGINAL credit line amount
new_credit_line - the user's ADJUSTED credit line amount


-------------------------------------
