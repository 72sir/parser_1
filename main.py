import urllib2
import json

URL = 'http://betting.gg11.bet/api/sportmatch/GetMostPopular?sportID=2357'


def parse_courses():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]

    f = opener.open(URL)
    f_read = f.read()
    i = 0

    try:
        f_json = json.loads(f_read)

        while i < 10:
            print (f_json[i]["DateOfMatchLocalized"]["Value"])
            print (f_json[i]["MarketsCount"])
            print (f_json[i]["PreviewOdds"][0]["MatchID"])
            print (f_json[i]["PreviewOdds"][0]["Title"] + " - " + f_json[i]["PreviewOdds"][1]["Title"])
            print (str(f_json[i]["PreviewOdds"][0]["Value"]) + " - " + str(f_json[i]["PreviewOdds"][1]["Value"]))
            print("______________________________________________________")
            i += 1

    except ValueError:
        print("error json structure")


def main():
    parse_courses()


if __name__ == '__main__':
    main()
