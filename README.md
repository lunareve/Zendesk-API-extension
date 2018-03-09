# Zendesk-API-extension

This ticket viewer uses the Zendesk API to retrieve a user's tickets and display them via the browser.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Tested in a Vagrant environment.
You will need your Zendesk credentials and subdomain to authenticate.

### Installing

Mac OS specific instructions

Create a new virtual environment and install prerequisites from requirements.txt.

```
$ virtualenv/env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

Start the server and access in the browser from ```localhost:5000```.

```
$ python server.py
```

Enter your Zendesk credentials and subdomain in the fields provided.
The viewer should then redirect to a list of all the user's tickets.
Click on a specific ticket to drill down into the ticket properties.
