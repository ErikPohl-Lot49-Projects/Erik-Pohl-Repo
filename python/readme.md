# This repo shows an evolution

![Tools! Tools?](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/evolu.png "Tools! Tools?")

I am quickly evolving my style now from "able to solve complex problems in Python reliably" more towards "writing Python I'd submit for a production code review".

I'm still learning, researching Python-particular coding patterns (even learning from anti-patterns), to refine my code style

The most representative work is recent work:

_JnesaisQ_

_list_of_xs_sorter_

I plan on building on these so they work together and so the list_of_Xs_sorter uses a design pattern to handle all of the different lists of Xs it can sort.
As I move forward, I will go back and refactor for style and clarity my former work, including adding the details below:

# Important disclaimer

Some of the code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] Apply this checklist to all new projects as step one
- [ ] A complete regression test suite in PyTest (until I can decide between that and unittest/Parameterized)
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Thoughtful, self-documenting, variable, method, and function names.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
  - [ ] Specifically, would this benefit from comprehensive logging?
  - [ ] Would it benefit from a results page with stats to demonstrate accurate and complete results?
  - [ ] How do I want to manage output to stdout, stderr, file, etc?
  - [ ] How do comments and outputs help and assist one another without being redundant?
- [ ] Actual docstring comments at all levels of the code.
- [ ] Linting the code for PEP 8 standardization like PEP8 or Applying a PEP formatter to the code like Project Black.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.
- [ ] Commit statements which facilitate an understanding of code history.
- [ ] Readme.md pages with more interesting usage of markdown which tell a code narrative. 
- [ ] For custom classes, create dunders as appropriate
- [ ] Make good decisions relating to
  - [ ] Exceptions versus return values
  - [ ] Using idiomatic Python versus clarity of code
  - [ ] Extend this list

**_This will also serve as a template for the starting readme to do list for any new folders created under this one._**

# I know what code smells are

![Yoda doesn't like code smells](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/code_smell.jpg "Stinks it does.")

**_I don't like code smells._**  

On the job, I'm ever-vigilant about them.

Python is not my day-job.  I taught myself Python on nights and weekends because I love the language.

This is a repo I put together after a full day of work of software engineering in PL/SQL.  On weekends, it was after a full work-week in PL/SQL.  

I do this side-work because I love Python enough to spend my leisure time getting better at it.  

_Why do I have Python code up here with bad code smells?_

I want to demonstrate I can write a rough draft of Python code to do a variety of things.

Also, I am getting much better (some of this is Yoda-aged code for me!)  I do come back periodically and clean it up.  

Some of this code is just downright experimental:

* Some code is made in such a way as to stretch out what the code does along different axis.  The early drafts are to get the code working, and the later drafts will make it conform to expectations more in how it does that thing.
* Some code was written deliberately hard in order to be a puzzle for my writing skills.  I learn from these anti-patterns: in constructing the code and recognizing why it would be difficult to maintain.

In other words, this is my sandbox.  You get a peek inside what I'm curious about.  I move very fast and break a lot of things here, since I have limited evening and weekend time to move this work forward.  I focus on getting to green, and sometimes that means the code is not refactored when you check in.

**Code is only partly measured by how it performs as expected-- it should communicate, tell a story.**  

That's what I do during my work-day.

Were Python my day-job, I'd apply the same level of ever-vigilance to it as I have over time in other languages, and I would address the code during a work day when I'm still fresh (have coffee / tea in me).  

Some of my better work is not in this repo because it is protected by an obligation to one or more companies.

Thanks in advance for holding your nose!

# Python High-Level To Do
## Design pattern gists to complete
- [x] Factory Method
- [x] Adapter
- [x] Composite	
- [x] Flyweight	
- [x] Interpreter	
- [x] Observer	
- [x] Strategy	
- [x] Template Method	
- [x] Vistor	
## Other
- [ ] Add to this list from every project
- [ ] Django Tutorial
- [ ] Design Patterns tasks -- goal: present, complete
  - [ ] Design Patterns Presentation
  - [ ] Design Patterns Wiki
  - [ ] PEP8 Design Pattern Gists
- [ ] PyJamb
  - [ ] Tools for PyJamb
- [ ] Rewrite Blister using tools (term count)
- [ ] Rewrite Velodrome using tools (ETL)
- [ ] Fast Hammer
  - [ ] Tools for Fast Hammer (Dedup/Redup)
- [ ] JnesaisQ
   - [ ] Sum/Aggregate of JnesaisQ?
   - [ ] Concurrency in JnesaisQ list query?  *Probably not.*
- [ ] Countput
  - [ ] More Countput result formats
- [ ] Machine Learning
  - [ ] Complete various tutorials on different datasets / algorithms
  - [ ] Prepare ML presentation
- [ ] Guarantee
  - [ ] Revisit Validations in Guarantee
- [ ] xlate
  - [ ] Mandatory fields and/or validations in xlate
  - [ ] xlate date format and custom field type support
    - [ ]    field_validate?  custom rules
    - [ ]    field_xlate?   custom rules
- [ ] Work on xlate list of lists sorter and countput to align them and jnesaidq
- [ ] tool driven Stopwatch (next side-project)




