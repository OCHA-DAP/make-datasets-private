import ckancrawler, json, sys

config = json.load(open("config.py", "rb"))

def run (ckanurl, organization, user_agent=None, apikey=None, delay=0):
    crawler = ckancrawler.Crawler(ckanurl, user_agent, apikey, delay)

    for package in crawler.packages(fq="organization:{}".format(organization)):
        print(package["name"])

if __name__ == "__main__":
    config = json.load(open("config.py", "rb"))
    run(config["ckanurl"], config["organization"], config.get("user_agent"), config.get("apikey"), config.get("delay"))
