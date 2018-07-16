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

Dedup works like this:
1. It reads blocks of 1024 bytes and uses a hash function (developer selects one from a dictionary of hash functions in the class) to hash the block of 1024 bytes to a hash code of 8 bytes. 
2. It saves any new hash codes and their original blocks to the deduplication file.
3. It records any matches (a hash of the same block of contents to the same hash code) and collisions (a hash of a different block of contents to a previous hash code) during this process for review later.
4. After building a hash table in the deduplication file, it then iterates through the original file, recording each 1024 bytes from the original file into 8 byte hash codes in the deduplication file.
5. It closes files and performs cleanup.

Redup works like this:
1. It reads the hash table from a deduplication file.
2. It then reads hash codes of 8 bytes from the remainder of the deduplication file and writes out their corresponding values from the hash table to a reduplication file.
3. It closes files and performs cleanup.

## Running the tests

A good way to test this at the current moment, absent a future feature of file comparison, is to select various test file algorithms in the main section of code.  Then run the process for each file creation method.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Improvements

There are a few targeted improvements I'd like to make:
1. While this employs memory windowing to keep from storing entire files (except in really bad scenarios -- completely random files in memory), I'd like to review memory usage to further optimize it.
2. I'd like to bail on files which cannot be effectively deduplicated.
3. I'd like to do multiple attempts until there are no collisions in some cases.
4. I'd like to add to in-code documentation and refactor.
5. Pretty high up there on the list is deciding on another deduplication file format.  This one works, but I'd rather use delimiter text proven not to be in the original file at all.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to those who inspired this work.
