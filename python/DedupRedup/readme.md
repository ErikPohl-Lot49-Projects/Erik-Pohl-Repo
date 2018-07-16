# Dedup / Redup Example: DedupRedup

In this code, I created a DedupRedup class.  This class contains methods and attributes to experiment with file deduplication and reduplication.  Most notably, it permits addition of various methods for hashing data and various methods for creating test file scenarios to deduplicate and reduplicate.

## Getting Started

Download these files to corresponding folders under your Python project folders to try it out.  

### Prerequisites

No prerequesites.

### Installing

Once the file is installed into a folder for use with Python, it should run as-is.  With the current settings, it creates a test file, deduplicates it, then reduplicates it in the same folder as the DedupRedup.py file.

### Methodology

There are two main API methods in use here:
dedup and redup.

Dedup accepts as input an original file name/path and a deduplicated file name/path.  The process deduplicates an original file in the orginal file name/path into the deduplicated file name/path.

Redup accepts as input a deduplicated file/path and a reduplicated file name/path.  The process uses hash table data and hash codes representing an original file to rebuild a longer reduplicated version of a file from the hash table and hash codes.

In a good situation, and not all situations are good (e.g. very random files), the original file from dedup will be a one-for-one match with the reduplicated version of the file from redup.

## Running the tests

A good way to test this at the current moment, absent a future feature of file comparison, is to select various test file algorithms in the main section of code.  Then run the process for each file creation method.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* No Acknowledgements, except thanks to the interview question I received which made me want to prove this task would be trivial for me to create from scratch in a few hours for a demonstration, then refactor over time.
