# D7046E-DeltaBot
A ANN based chatbot project for the course D7046E.

---------------------------------------------------------
07-03-2023 Meeting Agenda

Participants: Lukas, Tobbe, Anders, Jeremy

-Status report
  -Model training 
    -Stuck with constant accuracy over epochs
    -Code review on validation accuracy (Tobbe)
  -Model modifications (Anders)
    -add layers 
    -remove stemmer in preprocessing (try changing to wordnet lemmatizer) (Jeremy)
    -change optimizer 
    -change embedder 
    -later -> add regularization (dropout, regularization L1 & L2)
  -Move to CPU version

-Process user input
  -connect existing trash model to cli (Lukas)
  -show the certitude to the user
About the presentation (09-03-2023)
  -start tomorrow 
Book next working session and room if needed
  -from 8:15 to 12:00 - 13:00 to 17:00 (room booked)

-------------------------------------------------------------------------
28-2-2023 Meeting Agenda

Participants: Lukas, Tobbe, Anders, Jeremy

- Status report
  - Preprocess
    - In progress, the base structure is there.
  - Load dataset and verify
    - Loading is working
    - Need to implements sampling -> (distinguish good and bad reviews)
 - Constructing a training method early stopping, saving best and store model
  - Not here yet
- Question about project scope
  - User inputs text, chatbot responds with suggestions based on
    - too simple
    - swear words
    - incoherent
    - repetitive
- Python type hinting
- Push parser
  - done
- Look up at least 1 NLP project
  - done
- Define clearly what the chatbot should do
  - Input text -> Analyze text -> Hard coded input
- Book next working session (if we want one)

- Book next weekly sprint meeting
  - Done
- Other
  - Crunch?
    - Tuesday 28-2, 13:00 -> 17:00
    - Wednesday 1-3, 13:00 -> 17:00
    - Friday 3-3, 8:00 -> 11:30, 13:00 -> 17:00 (DISCORD - ROOM BOOKED)
    - Monday 6-3, 9:00 -> 11:30 (discord)
    - Tuesday 7-3, 13:00 -> 17:00 (ROOM BOOKED)
    
-------------------------------------------------------------------------

21-2-2023 Meeting Agenda

Participants: Lukas, Tobbe, Anders, Jeremy

- Status report
  - Documentation
    - Requirements tbd
    - PR (Lukas)
  - Dataset
    - Amazon Fine Food Reviews : https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
- Begin distributing work.
  - Preprocess (Together)
  - Load dataset and verify (Together)
  - Constructing a training method early stopping, saving best and store model (Together)
- Group work, time slots?
  - 02/24 Friday 8.15. Discord.
- Book the next meeting.
  - Book next weekly sprint meeting (Tobbe)
- Other
- Send email asking about project scope to Karl (Tobbe)
  - Ask at weekly class meeting for the project if there is no answer before.
- Python type hinting (Anders)
- Push parser (Jeremy)
- Look up at least 1 NLP project (Lukas, Tobbe, Anders, Jeremy), look for methods.

---------------------------------------------------------

14-2-2023 Meeting Agenda and minutes

Participants: Anders, Tobias, Jeremy, Lukas

- Status report
  - Status off ANN 2
    - Most are done
  - Individual environments
    - Wip 
  - Project breakdown
    - Parser
      - Strip extra signs “. , ‘ / ! ?”
      - Lower case everything
      - Base word form, cats -> cat etc
    - Skip-gram
- Create documentation for setting up our environment, Anders, until thursday.
- Dataset
  - Everyone looks through the github until thursday and picks out a few (2-5) datasets that sound interesting.
- Other

---------------------------------------------------------

10-2-2023 Meeting Agenda and minutes

Participating members: Anders, Tobias, Jeremy, Lukas

- Introductions etc.
- Workflow: How do we prefer to work?
  - Github, discord, 
- PR
  - Review 
- Development environment.
  - plain python (no jupyter), OOP, 
- Project goal, what do we want as a finished product?
  - Initial MVP
  - Second iteration 
    - Generate responses
    - Better interpretation
- Set up a sprint. (decide what should be completed at specific dates)
    - Try to get as far as possible with ANN 2 until tuesday. 
    - Set up the local environment in anaconda.
    - Look through the description and think about a break-down.
- Recurring meetings? 
  - Tuesdays 13:00
- Other
