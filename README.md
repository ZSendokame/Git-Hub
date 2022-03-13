# Twitch Tab
Show github statistics on web, made for Twitch overlay!<br>
It will automatically update every ten minutes.

![image](https://user-images.githubusercontent.com/70088953/158067707-4eb38222-564e-4188-a403-66ff1141293d.png)

# How-to Install
```sh
git clone https://github.com/zsendokame/twitch-tab && pip -r install requirements.txt
```
With that command executed, your ready to use Twitch-Tab.

# How-to Use
```sh
cd twitch-tab # If your not in the repository folder, run this.
python api.py # Finally, the API it's running on http://localhost:5000/.
```

To get the statistics of a user, add the query "username" with the user name as it's value.
It will return an HTML who can render on Web, OBS and more.

URL Example: https://localhost:5000/?username=ZSendokame
