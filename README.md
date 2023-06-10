<div align="center">
  <b>Eliminate boilerplate. Enhance efficiency.</b>
  <br><br>
  <p>
    <a href="https://codecov.io/gh/GH-Syn/strlib"><img src="https://img.shields.io/codecov/c/github/GH-Syn/strlib?color=ee8695&label=coverage&style=for-the-badge"></img></a>
    <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/GH-Syn/strlib?color=ffa49a&style=for-the-badge">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/GH-Syn/strlib?color=f35e79&label=issues&style=for-the-badge">
  </p>
</div>

## Description
`strlib` is a Python library that provides mutative functionality for strings. It's purpose is to provide an alternative to existing libaries such as `re` through a comprehensive set of functions.

## Usage
```python
>>> import strlib

>>> # Parse URL and exclude periods
>>> strlib.parse_url("https%3A%2F%2Fgoogle%2Ecom", exclude=".")
>>> "https://google%2Ecom"

>>> strlib.strip_punctuation("The quick brown fox .jumped over the lazy dog.")
>>> "The quick brown fox jumped over the lazy dog"
```

<h2></h2>
<div align="center">
  <a href="https://gh-syn.github.io/strlib/">Documentation</a>  |
  <a href="https://stats.uptimerobot.com/jWk6BflM5J">Uptime</a> |
  <a href="https://github.com/GH-Syn/strlib/releases/latest">Tags</a>
</div>
