"""
Author: Alexander Angel
Date: 06/16/2019
Time: 02:21:01 < interesting, dads bday

I've just been sitting down and I wanted to see what it'd take to import emails and then automatically filter out all the noise
so I can just read the important ones. Then, it could make me a list of things to do, based on the important emails.
I was doing some searching and came across this idea of a "daily briefing". Every morning, I grab my coffee and go to my computer to organize
my day and week. This is a time consumping process. I want to work hard, but it takes time to figure out what to work on! Let's just automate that
so I can spend all the time working and finishing tasks. A task list! But not a lame to do list, that's lame. This needs a new name.
Quest? It's a daily quest. A task. A job. Board? Like in RPG video games you go to the town's notice board to see the quests available,
the rewards they offer. Difficulty. Intersting. We'll come back to the name.

*** SIDE NOTE: Get random jobs you could do, if you choose to accept, get paid? ***

Competition:
Trello is doing almost the exact same thing. But it's boring, or it looks boring. I don't want to get on it. It looks like work. Glorified task manager.
Omnifocus, another to do app. Look's like a mess. It just looks like work! There's so many tasks all taking up space, look's like a pain to delete and manage it all... I;ll have to try it.
Things 3. Probably best "to do" list app. Award winning design, very Apple-esque. It gives you a lot of options for task management. CALENDAR VIEW <- important feature. It adds to my workload.

I NEED A NET DECREASE IN MY WORKLOAD BY USING A TASK LIST. How hard is that?

I've used an excel sheet to gauge my student work and projects, amount of time left until an exam. But this is a lot of effort. It's great but it takes valuable time. 

Defensibility:
This could be the largest concern. It's pretty simple code, or so it seems. The proprietary bleeding edge technology is in the realm of basic AI/ some great algorithims to efficiently manage a human day.
Could be some integration with blockchain technology -> especially if rewards are in the program. Why pay people to do their work? Gets more people on the platform to generate something.

Basically, I get all these bullshit noise emails that I'm just tired of reading. 90% of my email inbox is spam, and I actively remove subscriptions from companys that are spamming me. "Spam" just relates to anything not actually valuable
to me. I need to wake up, see what I have to get done, and worry about getting it done. I don't need to worry about making a list of what to get done. This can bleed over into being disciplined when learning something new.
It's hard to learn something new, which is why I like learning new things. But, I'd rather spend all the hard energy on learning deeper knowledge, not on getting initiated. If I had a task manager to manage my learning steps,
it could lead to all new heights.

Time to sleep. Will think on this.

What will the program look like?

High Level Architecture:
    Receive Email
        Parse Email
        Filter Email
        Add important emails to a task list.
        I choose which tasks to do.
        It saves my tasks and all the tasks I've done and loads them.


This is the most basic of the problem. AKA Version 1.

Main.py
    Starts program and interface.
KO.py
    Backend
    Runs processing of emails
Interface.py
    Builds the "board"
    You click what you:
        want to do
        dont want to do
        would prefer to do
        what you will do later
    You get rewarded! Addicting, like leveling up.

KO.py
    def email_parse:
        Reads email from file or whatever
        Returns text format
    def email_analyze:
        reads text format of parsed email
        and determines what is important/not important/spam
        Returns the text format of the email with a
        MARK -> marks go onto the board
    def BOARD Class:
        Initializes a board with rows/columns?
        Loads a the previously saved board onto it.
        Attributes:
            Length of height, (number of tasks to do)
            Length of width per block (importance of task)
            Value: each item on the board has a value that is
            reprensenting how much reward is given
            subject: which work/topic/sbuject the task is related to
"""