# DeAwkwardize
 
This is the working title for a project to abbreviate comments and logging in Python source code.
Logging would be activated using a decorator function.
Comments and logging would output when the code is reported on using a translation function.

The impetus?  I come from a tradition of supporting production code with heavy commenting and logging.
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

### This database is used by DeAwkwardize:

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

  I want comments to be overlaid onto code, and even onto themselves, and tie into the hierarchical structure of PyJamb
  These could be revealed using TKinter or in an IDE plugin
  
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
