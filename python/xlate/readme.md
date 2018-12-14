# xlate


Missing the switch from C and the case from PL/SQL, I looked and found this reason why there is no equivalent in Python:

>A quick poll during my keynote presentation at PyCon 2007 shows this proposal has no popular support. I therefore reject it.

(Courtesy: https://www.python.org/dev/peps/pep-3103/)

So I did what surely nobody in the history of Python has done, and I made a switch class.

# Features

1. Allows you to assign breaks to conditions, otherwise will fall through to the end of the switch, evaluating every clause.
2. Looks prettier than a bunch of elifs.

*And I think Pollock's abstraction is pretty*:

![Convergence](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/convergence_u-l-ehp4w0.jpg "Eye of the beholder")

# Example usage

#### Import the switch_class
```
from switch_class import switch
```

#### Set up a function which serves as a switch condition
```
def foo():
    return ['1','2']
```

#### Create a switch object with a default value
````
my_switch = switch('Not found')
````

#### Add in switch conditions to be evaluated in order
````
my_switch.add_switch_clause('2', 'Two',False)
my_switch.add_switch_clause(['2','3'], 'Three',False)
my_switch.add_switch_clause(foo(), 'X',False)
my_switch.add_switch_clause('4', 'Four',True)
my_switch.add_switch_clause('4', 'Should not get here',True)
````

#### Execute the switch condition for some compare values and output the result
````
print(my_switch.execute_switch('1'))
print(my_switch.execute_switch('2'))
print(my_switch.execute_switch('5'))
print(my_switch.execute_switch('4'))
````

#### Check the results
````
['X']
['Two', 'Three', 'X']
Not found
['Four']
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
