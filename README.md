# wetransferpy

|PyPI version| |PyPI license|

Python script for uploading and downloading wetransfer files from the command line.
Inspired by upload-wetransfer https://github.com/kraynel/upload-wetransfer by
kraynel https://github.com/kraynel and wetransfer-upload https://github.com/creemerica/wetransfer-upload by Spencer Cree https://github.com/creemerica.

## Features

- Upload files or directories of files with or without authentication
- Download file from url
- Show progress of upload and download

## Installation

`$ pip install wetransferpy`

or

`$ git clone https://github.com/predat/wetransferpy`

## Usage

Authenticate upload:

```python
     from wetransferpy import WeTransfer

     wt = WeTransfer(username="name@example.com",
                    password="thepassword",
                    sender="sender@example.com",
                    receivers=["receiver1@example.com","receiver2@example.com"],
                    channel='',
                    message='Hello from python',
                    expire_in='3m',
                    progress=True,
     )
     wt.uploadFile('thefile.mov')
```

Anonymous upload:

```python
     from wetransferpy import WeTransfer
     wt = Wetransfer()
     url = wt.uploadFile('thefile.mov')
     print url
```
