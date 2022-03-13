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
        repositoryCount=get.json()['public_repos']
    )

@app.get('/repository')
def repository():
    get = requests.get(f'https://api.github.com/repos/{request.args.get("username")}/{request.args.get("name")}')

    return render_template(
        'repository.html',
        repositoryLink=get.json()['html_url'],
        repositoryName=get.json()['name'],
        starCount=get.json()['stargazers_count'],
        forkCount=get.json()['forks_count'],
        usedLanguage=get.json()['language']
    )

app.run()
