# Countput 


Countput extends Python's Counter class from Collections to provide different styles of output and return values.

-------------------------------------

Is Counter perfect?  _Of course_

Is the word *perfecter* a good one?  _No, it is not.  It is not a good word._

Is Countput *perfecter* than Counter?  _Given the above statements, yes.  Sure.  It is perfecter._

![Ah Ah Ah!](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/count.jpg "Ah Ah Ah!")
*The Ah Ah Ah! to Python's Counter*



# Example usage

#### Import the Countput class
```
from Countput import Countput
```

#### Create a word list to count using Counter's native functionality
```
word_sentence = 'a b c d e f g h i a c e g i c g'
word_list = word_sentence.split(' ')
```

#### Make a Countput object, print the output as a list of formatted count values, print the list with newlines
````
MyCountput = Countput(word_list)
print(
    'return_as_list of strings : ' + str(
          MyCountput.return_topn_as_list_of_strings(
              n=2,
              delimiter=' - Value',
              prefix='[Term: ',
              suffix=' ]',
              header='Header'
          )
      )
)
````

#### Now, with fewer frills
````
print(
    'return_as_list of strings for sort_as_list_of_strings: ' + str(
          MyCountput.return_topn_as_list_of_strings(n=2)
      )
)
````

#### Now, just the output, no return list
````
MyCountput.formatted_topn_output(
    n=2,
    delimiter=' - Value:',
    prefix='[Term: ',
    suffix=" ]"
)
````

#### Just the output, with frills
````
MyCountput.formatted_topn_output(
    n=2,
    delimiter=' - Value:',
    prefix='[Term: ', suffix=" ]",
    header='Formatted Output with header:'
)
````

#### Return as a dictionary
````
print(MyCountput.return_as_dict())
````


# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] A complete regression test suite.
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
- [ ] Actual docstring comments at all levels of the code.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.


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
