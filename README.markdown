# Lattice QCD Inventory WebApp

A (probably Django based) web application to manage lattice QCD objects like:

- Ensembles
- Perambulators
- Dilution Schemes

## Develop

### Initial Setup

Development is made manageable by using a virtual Python environment. Just run
the `init-virtualenv` script. It will create a new virtual environment for
Python 3 and download the Django framework into there. This step has to be done
once only. It may fail because:

- `python3` is not installed.

- `virtualenv-3` cannot be found in the path. Perhaps it is called differently
  on Debian systems.

- `pip3` is not installed.

### Starting the Server

Just run the `start-server` script to run the server on your local machine.
Then it runs the application on http://127.0.0.1:8000/ and you can just browse
to it.

## Deployment

We have to talk about that, with Python and Django it is a bit complicated :-/.
Perhaps we go the WSGI route?

At least there are no static files because jQuery, Bootstrap, and MathJaX are
obtained via a CDN.

<!-- vim: set spell tw=79 : -->
