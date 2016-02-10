# PyTasc
A generic Python Tool for Assembling Source Code written in Python

This is a Python port of [tasc](https://github.com/hcpss-banderson/tasc) which
is written in PHP. I wrote this because I needed to asseble projects on servers
that did not have PHP installed. I found Python to be a more commonly installed.

## Requirements

You need Git, Python, PIP and the packages in `requirements.txt`. You can get 
them by running:

```
$ pip install -r ./requirements.txt
```

## Usage

### Create a Manifest File

PyTasc assembles projects bases on a YAML formatted manifest file. This file
contains all the information about where to find code and where to put it in
assembling our project:

```yml
---
# Code to fetch and assemble.
projects:
  - 
    # What provider are we going to use to fetch the code. 
    # Options are git and zip.
    provider: git
    
    # For git, we want the http URI of the git repo.
    source: "https://github.com/moodle/moodle.git"
    
    # "tag" can be a git tag or a branch name or even a commit hash.
    tag: v2.9.3
    
    # We are going to omit the "destination" option. That means that this
    # project our root project. It will be installed in the root of the 
    # destination
    # destination: "/"
    
  - provider: git
    source: "https://github.com/HCPSS/moodle-theme_vision.git"
    tag: v1.0.2
    
    # Where do we want to put this code relative to the project root? This is a
    # Moodle example and the previous project would have created a "theme" 
    # folder. That's where we want to put this theme
    destination: theme
    
    # If I were to clone this repo, it would create a folder called
    # "moodle-theme_vision" but I want it to just be called "vision". I can
    # rename it here. In combination with the destination specified above, the
    # vision theme will be placed in /theme/vision
    rename: vision
    
  - provider: git
    rename: mandatory
    
    # In this example, we construct a basic oauth request URI so that we can
    # access private repos. We will provide a value for the github_access_token
    # placeholder later when we run PyTasc.
    source: "https://{github_access_token}:x-oauth-basic@github.com/HCPSS/moodle-enrol_mandatory.git"
    tag: v1.0.0
    destination: enrol
    
  - 
    # Sample that uses the zip provider.
    provider: zip
    rename: rss_plus
    source: "https://moodle.org/plugins/download.php/9385/block_rss_plus_moodle29_2015092400.zip"
    destination: blocks
    
# Patch the code (optional)
patches:
  - 
    # patch_file is the only patch type supported at the time of this writing.
    type:         patch_file
    source:       patches/mod_forum_lib.php.patch
    destination:  mod/forum/lib.php
```

### Create Patches (optional)

Patch files are specified in the manifest relative to itself:

```
project_manifest/
  manifest.yml
  patches/
    mod_forum_lib.php.patch
    blocks_rss_plus_block_rss_plus.php.patch
```

### Run It!

When you run PyTasc, you need to specify the manifest file and where you would 
like the sources assembled. For example:

```
$ py_tasc.py --manifest=./manifest.yml --destination=./application
```

You can also specify any replacement tokens in your manifest by specifying
a `--extra-parameters` option. Parameters should be specified in JSON format. In 
the above example manifest, we have a token for github_access_token:

```
$ py_tasc.py --manifest=./manifest.yml --destination=./application --extra-parameters='{"github_access_token": "MY_TOKEN"}'
```

**Important:** Note the quotation sequence in the JSON string. This works 
'{"foo": "bar"}' but this does not "{'foo': 'bar'}". I believe that these are 
both valid JSON formatted strings, but python does not like the 2nd one.

## License

PyDev is released under the MIT license.
