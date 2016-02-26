============
wetransferpy
============
.. image:: https://travis-ci.org/predat/wetransferpy.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/predat/wetransferpy
.. image:: https://badge.fury.io/py/wetransferpy.svg
    :target: https://badge.fury.io/py/wetransferpy

Python script for uploading and downloading wetransfer files from the command line.
Inspired by `upload-wetransfer <https://github.com/kraynel/upload-wetransfer>`__ by
`kraynel <https://github.com/kraynel>`__ and `wetransfer-upload <https://github.com/creemerica/wetransfer-upload>`__
by `Spencer Cree <https://github.com/creemerica>`.

Features
--------

-  Upload files or directories of files with or without authentication

-  Download file from url

-  Show progress of upload and download


Installation
------------

.. code:: bash

    pip install wetransferpy

.. code:: bash

    git clone https://github.com/predat/wetransferpy


Usage
-----

Authenticate upload:

.. code-block:: python

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


Anonymous upload:

.. code-block:: python

    from wetransferpy import WeTransfer
    wt = Wetransfer()
    url = wt.uploadFile('thefile.mov')
    print url

