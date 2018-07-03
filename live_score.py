import requests, json
from way2sms import send_msg
from bs4 import BeautifulSoup
from time import sleep
minutes_to_sleep = 2
while True:
    print('Minutes to sleep: ', minutes_to_sleep)
    sleep(minutes_to_sleep * 60)
    minutes_to_sleep = 2
    print('Preparing...')
    MATCH_URL = 'http://www.goal.com/en-in/match/uruguay-v-saudi-arabia/8t3fwwakjdrpm6cgcdhrgiacp'
    headers = {
        'Host': 'www.goal.com',
        'Referer': 'http://www.goal.com/en-in/world-cup/70excpe1synn9kadnbppahdn7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    u = MATCH_URL.split('/')
    matchToken = u[len(u) - 1]
    team = u[len(u) - 2]
    teams = team.split('-')
    team1 = teams[0]
    team2 = teams[2]
    liveFeedURL = 'http://www.goal.com/en-in/ajax/match/live-data/' + matchToken
    msg = ''

    matchFeedResponse = ''
    with requests.Session() as s:
        matchFeedResponse = s.get(liveFeedURL, headers=headers)

    matchFeed = json.loads(str(matchFeedResponse.text))
    displayData = matchFeed['displayData']
    scorers = matchFeed['scorers']
    msg = msg + '\t' + displayData['stateText'] + '\n'
    if displayData['stateText'] == 'HT' or displayData['stateText'] == 'FT':
        minutes_to_sleep = 30
    print('\t' + displayData['stateText'])
    msg = msg + team1.title() + ' ' + displayData['scoreText'] + ' ' + team2.title() + '\n'
    print(team1.title() + ' ' + displayData['scoreText'] + ' ' + team2.title())

    if '0 - 0' not in displayData['scoreText']:
        msg = msg + 'Goals: \n'
        print('Goals:')
        team1_scorers = scorers['home']
        team2_scorers = scorers['away']
        msg = msg + team1.title() + ': \n'
        print(team1.title() + ': ')
        for scorer in team1_scorers:
            print('\t' + scorer)
            msg = msg + '\t' + scorer + '\n'

        print(team2.title() + ': ')
        msg = msg + team2.title() + ': \n'
        for scorer in team2_scorers:
            print('\t' + scorer)
            msg = msg + '\t' + scorer + '\n'

    print('Commentary:')
    msg = msg + 'Commentary: \n'
    commentary = matchFeed['commentary']
    latest_comm = commentary['items'][0]
    soup = BeautifulSoup(str(latest_comm), 'html.parser')

    # comment = 
    time = soup.find('span', {'class': 'time'})
    if time is None:
        print(soup.find('span', {'class': 'text'}).text)
        msg = msg + soup.find('span', {'class': 'text'}).text + '\n'
    else:
        print(time.text + ': ' + soup.find('span', {'class': 'text'}).text)
        msg = msg + time.text + ': ' + soup.find('span', {'class': 'text'}).text + '\n'

    send_msg(msg)

    def print_scorers(team1_scorers, team2_scorers):
        bigger = team1_scorers if (len(team1_scorers) > len(team2_scorers)) else team2_scorers
        for i in range(len(bigger)):
            if (i < len(team1_scorers) and i < len(team2_scorers)): 
                print(team1_scorers[i] + ' - ' + team2_scorers[i])
            elif i >= len(team1_scorers):
                print('\t - ' + team2_scorers[i])
            else:
                print(team1_scorers[i] + '\t - ')

