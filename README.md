SublimeLinter-contrib-doc8
================================

[![Build Status](https://travis-ci.org/nvtkaszpir/SublimeLinter-contrib-doc8.svg?branch=master)](https://travis-ci.org/nvtkaszpir/SublimeLinter-contrib-doc8)

This linter plugin for [SublimeLinter][docs] provides an interface to [doc8](https://launchpad.net/doc8). It will be used with files that have the ``rst`` syntax.

## Installation
SublimeLinter 4 must be installed in order to use this plugin. If SublimeLinter 4 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `doc8` is installed on your system. To install `doc8`, do the following:

1. Install `doc8` by typing the following in a terminal:
   ```
   pip install doc8
   ```

You may require to use sudo.

**Note:** This plugin requires `doc8` 0.8.0 or later.

### Linter configuration
In order for `doc8` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `doc8`, you can proceed to install the SublimeLinter-contrib-doc8 plugin if it is not yet installed.

### Plugin installation

This package is not in the PackageControl, but you can use it by cloning repo:

```bash
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/nvtkaszpir/SublimeLinter-contrib-doc8
```

After that restart SublimeText.

## Settings

You should use ``doc8.ini`` file in current working directory of the project, or in your home directory.
Refer to doc8 documentation.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
