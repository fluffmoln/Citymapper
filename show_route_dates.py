import sys
import csv
import urllib
import zipfile

# Function to call the specific columns/info from specific csv/txt file
def csv_dict_reader(csvfile):
    reader = csv.DictReader(csvfile, skipinitialspace=True, dialect="excel")
    for line in reader:
        print "Service",
        print(line["service_id"]) + ":",
        print(line["start_date"]) + " -",
        print(line["end_date"])

# For the main Chicago service providers available at TransitFeeds.
# URLs that work for this specific script (since they all use similar schema):
# Smaller Metra GTFS: "http://transitfeeds.com/p/metra/169/1409025601/download"
# Larger CTA GTFS: "http://transitfeeds.com/p/chicago-transit-authority/165/download"
# Smaller Pace GTFS: "http://transitfeeds.com/p/pace/171/1408325192/download"
# When calling "python show_route_dates.py 'url'" from command line
url = sys.argv[1]
downloadzip = urllib.urlretrieve(url, "gtfs.zip")

# Perform function with specified url
if __name__ == "__main__":
    with zipfile.ZipFile('gtfs.zip') as z:
        with z.open('calendar.txt', 'r') as csvfile:
            csv_dict_reader(csvfile)
