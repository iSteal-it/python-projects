import find_internet_speed
import twitter

INTERNET = find_internet_speed.Speed()
speeds = INTERNET.get_speed()
TW = twitter.Twitter()
if float(speeds[0]) < 96 or float(speeds[1]) < 96:
    TW.login_()
    TW.tweet(speeds[0],speeds[1])

