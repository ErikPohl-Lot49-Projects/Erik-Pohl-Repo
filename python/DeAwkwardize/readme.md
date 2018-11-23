# DeAwkwardize

_**DO YOU WANT TO SEE A DECORATOR WHICH USES SOME COOL, SELF-MODIFYING CODE?**_

# WARNING!

![Under construction](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/webpageunderconstruction-1024x681.jpg)

**_DeAwkwardize_** is the working title for a project to tokenize comments and logging in Python source code and render them unobtrusive when reading the code.

The Deawk method of the class substitutes tokens for logging and comment-statements in the Python source code, writing a "deawkwardized" version of the code to file.

The logging tokens in the deawkwardized version of the code can be replaced for logging messages during runtime when applying a decorator, called "reawk_logging", to a function containing logging tokens.  This fun trick involves self-modifying code.

If you want to restore your source code to the original, comments and logging re-appear when you view code through the lens of a full reawk process.  

I use dill in conjunction with a translation file (later, this will be a database) to allow self-modifying code.
This is a demo version only.  It will become beta by the end of 2018, hopefully.

#### The impetus?  

I come from a tradition of supporting production code with heavy commenting and logging.
The heavy commenting allows ease of maintenance for developers who get pulled into a project and might be of varying skill levels.
The logging is useful for support and debugging, mostly support.  Production code without logging takes longer to support.

However, logging and comments tend to make my code look not Pythonic.

So I thought of the following substitutions:

```
def foo():
  '''docsys'''
  # comment the block
  some code
  log a critical status here
  # comment the block
  some more code
  log another critical status here
  # comment the block
  even more code
  log yet another critical status here
```  
```
def foo():
  '''docsys'''
  #1
  some code
  #@1
  #2
  some more code
  #@2
  #3
  even more code
  #@3
```
Using a decorator, we can marry the #@ codes to logging statements recorded in a data structure to create logging.
```
@DeAwkwardizeLogging
foo()
```
This would execute foo with logging in place of the #@ comments.

Using a reporting function, we can translate out the comments and logging statements
```
DeDeAwkwardizeCode(foo)
```
This would ouput the code with full comments and logging messages

### This database is potentially used by DeAwkwardize:

DeAwkwardizeBase

  Table Annotation_Apps:
  
      Annotation_app_id:  Unique ID for an annotation App
      
      Annotation_app_name:Name of the App to be annotated with DeAwkwardize
      
  Table Annotations:
  
      Annotation_id:      Unique ID for an annotation
      
      Annotation_app_id:  This identifier makes sure the annotation is applied to the correct source code
      
      Annotation_type:    Logging/Comment
      
      Annotation_text:    For a logging type, this is the contents of the logging message: 
      
                          logging.info("Hello, look at me here at,"+str(x))
                          
                          would have an Annotation_text of '"Hello, look at me here at,"+str(x)'
                          
                          For a Comment type, this is the contents of the comment:
                          
                          #This is a very long comment
                          
                          would have an Annotation_text of "This is a very long comment"
                          
      Annotation_modifier:For a logging type, this is whether it is info, critical, debug, etc.
      

# Future plans

- [ ] I want comments to be overlaid onto code, and even onto themselves, and tie into the hierarchical structure of PyJamb
  These could be revealed using TKinter or in an IDE plugin.
- [ ] Modify the tokens to be even less obtrusive using white space.
- [ ] Include a header comment not to manually modify tokenized comments.
- [ ] Make more comprehensive demos.
- [ ] Create a full regression test suite
- [ ] PEP8 lint the code and clean up
- [ ] Allow a user to designate comment types and logging types to deawkwardize rather than hard-coding.
- [ ] Address the issue of the token file delimiter possibly being part of the tokenized string.  
- [ ] Better example cases for the readme.

  
  
# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

a) A complete regression test suite.

b) Meaningful exceptions and exception-handling coverage.

c) Thoughtful, self-documenting, variable, method, and function names.

d) Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.

e) Actual docstring comments at all levels of the code.

f) Linting the code for PEP 8 standardization.

g) Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.

h) Commit statements which facilitate an understanding of code history.

## Getting Started

Download these files to corresponding folders under your Python src path.

### Prerequisites

I'll provide prereqs here.

### Installing

I will provide installation steps here.

## Running the tests

I will explain how to test the system here using the automated tests.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.

## Long-winded backstory

Of all the antonyms of "awkward", I prefer "easy".  Easy things are simple to understand.  Awkward things are less easy to understand at first glance: they do not conform to a simple pattern and are not immediately recognizable.

In social situations, "awkward" gets used for interactions which do not apply easy-to-recognize patterns.

Think of how we say "Hello" as a greeting.  It feels fairly meaningless, except as a means of initiating a conversation.

As an example, approaching even someone you know and starting out a conversation with: "Could you write us a program to find the area under a curve?" would be considered rude.

You first say, "Hello."  Ask them how their day is going.  Then make the request.  Now, it is fine.  

"Hello" is a verbal cue. In coding, the verbal cues can be comments and logging.

Some developers want to get rid of those verbal cues in their code, letting the elegance of the actual code communicate.  

So: for, example, I once heard a lead engineer say he rejects code in code-review which has comments.

Python is a beautiful language.  As a former Literature major in college, I can say it is actually poetic.

Pythonic and idiomatic Python code is elegant, not akward.  However, to a support or maintaining engineer, this elegance, this poetry, might still be seen as complex without more prosaic comments and logging messages.

I love long-winded comments and intense-amounts of logging for support reasons.  I have done support, and I loved clear explanations and explication-style logging.

How to get around this?  Elegant, poetic code without much help for support/maintenance, or prosaic code with a lot of help for support/maintenance?

Suppose I delivered code with comments like this: "#@1" 
and logging replaced with terms like: "#%2"

It has been deawkwardized.  The "Hello" greeting is not prosaic: "Hello, dear friend, how are you this fine day?"  It is short and present, but it has been cut to the essentials, allowing the rest of the code to be poetic and complex and elegant without "unnecessary" explanation.

What a build engineer sees as awkward, a support engineer might see as necessary.  

We can have both styles working together.

---------------------------------------------------------------------------------------------------------------------------
