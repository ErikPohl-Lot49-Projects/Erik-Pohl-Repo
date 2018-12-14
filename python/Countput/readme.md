# Countput 


Countput extends Pythons Counter class from Collections to provide different styles of output and return values.

Is Counter perfect?  _Of course_

Is the word *perfecter* a good one?  _No, it is not.  It is not a good word._

Is Countput *perfecter* than Counter?  _Given the above statements, yes.  Sure.  It is **perfecter**._



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
print(MyCountput.return_list(2, ' - '))
MyCountput.output_topn(2, ' - ')
````


# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] A complete regression test suite.
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
