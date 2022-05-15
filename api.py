from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='./source', static_folder='./source/static')

@app.get('/account')
def account():
    get = requests.get('https://api.github.com/users/' + request.args.get('username'))

    return render_template(
        'account.html',
        username=get.json()['name'],
        biography=get.json()['bio'],
        followerCount=get.json()['followers'],
        repositoryCount=get.json()['public_repos'],
        accountPhoto=get.json()['avatar_url']
    )

@app.get('/repository')
def repository():
    get = requests.get(f'https://api.github.com/repos/{request.args.get("owner")}/{request.args.get("name")}')
    starGazers = requests.get(f'https://api.github.com/repos/{request.args.get("owner")}/{request.args.get("name")}/stargazers')

    return render_template(
        'repository.html',
        repositoryName=get.json()['name'],
        starCount=get.json()['stargazers_count'],
        forkCount=get.json()['forks_count'],
        usedLanguage=get.json()['language'],
        lastStar=starGazers.json()[0]['login']
    )

app.run()