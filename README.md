# Reverser Client
`reverser` is a Sample library that can be used as a module within your Python project.
## Roadmap
- [x] Simple Reverser
- [ ] Two
---------------------------

## Quickstart
First, clone the `reverser` Git repository on your local machine and change your working directory to `reverser/`:
```console
$ git clone https://github.com/tactlabs/reverser.git
$ cd reverser
```
Next, compile the `reverser` package:
```console
$ python setup.py sdist bdist_wheel
running sdist
running egg_info
writing reverser.egg-info/PKG-INFO
writing dependency_links to reverser.egg-info/dependency_links.txt
...
```
Then, install the library using `pip` by specifying the path to `.whl` file in `dist/`:
```console
$ pip install dist/reverser-*-py3-none-any.whl
Processing ./dist/reverser-0.0.7.tar.gz
Processing ./dist/reverser-0.0.7-py3-none-any.whl
...

Then, from a Python interpreter:
```python
>>> from reverser import RevClient
>>> rc = RevClient()
[...
>>> content = rc.rev_me('one')
```

To verify the location and installation of `reverser` package:
```console
$ pip show reverser
Name: reverser
Version: 0.0.2
Summary: Reverser client for Python 3.6+
Home-page: https://github.com/tactlabs/reverser.git
Author: Raja CSP Raman
Author-email: raja.csp@gmail.com
...
```