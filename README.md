Make datasets private
=====================

Make all datasets for a CKAN organisation private.

# Requirements

Requires Python3. You must have write access to the datasets in the CKAN instance.

# Usage

Copy config.json.TEMPLATE to config.json

Fill in the fields in config.json as follow:

* *ckanurl*: the URL or your CKAN instance, e.g. "https://data.humdata.org"
* *apikey*: your personal API key from the CKAN instance
* *organization*: the organization identifier that appears in the CKAN URL (e.g. "my-org")
* *user_agent*: (optional) a user agent string that you want sent with your requests (e.g. for analytics filtering)
* *delay*: (optional) delay in seconds between processing each dataset (to go easy on the server)

After that, ``make run`` in a Linux environment will do the work of setting up a virtual environment and running the script. All datasets for the organisation will be flagged as private.

Create 2022-04-29 by David Megginson