# Convrspy

*A tool to convert color schemes between editors.*

...

A (very) quick rewrite of convrs from rust to python.

### Features

- Hopes to enable converting color schemes between different editors and palettes.
- In the future, hope to allow better mapping from source colors to destination colors.
- Right now, support for text files spit out by http://paletton.com/ to be spit out as jEdit scheme files.


### General use

- python convrspy.py < source_file > < source_format > < destination_format >

### Example

- python convrspy monokai.tmTheme tm jedit

##### About Paletton

- www.paletton.com is a really nice website that lets you come up with color palettes.
- For use with this converter, you would create a palette with "tetrad" colors, for now, and export as text.
- Copy paste that into a text file. Including the first blank line. I plan to strip out blank lines.
- I need to pick good colors from the generated palette or the output schemes. Another feature I want to add is allowing specification of color mapping between the source and destination scheme using json IR or something.
