""" Make all datasets for an organisation private

See README.md for info on setting up the config.json file.
"""

import ckancrawler, json, sys

def run (ckanurl, organization, user_agent=None, apikey=None, delay=0):
    """ Process the datasets
    """
    
    crawler = ckancrawler.Crawler(ckanurl, user_agent=user_agent, apikey=apikey, delay=delay)

    for package in crawler.packages(fq="organization:{}".format(organization)):
        print("Processing", package["name"], "...")
        package["private"] = True
        crawler.ckan.call_action('package_update', package)        

# Run from the command line (no args)
if __name__ == "__main__":
    config = json.load(open("config.json", "rb"))
    run(
        config["ckanurl"],
        config["organization"],
        user_agent=config.get("user_agent"),
        apikey=config.get("apikey"),
        delay=config.get("delay", 0)
    )
