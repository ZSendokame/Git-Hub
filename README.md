# Git Tab
Show github statistics on web, made for Twitch overlay!<br>
It will automatically update every ten minutes.

![image](https://user-images.githubusercontent.com/70088953/158074336-c8cd3ea5-1297-48da-93e0-b148e4097c92.png)

# How-to Install
```sh
git clone https://github.com/zsendokame/Git-Tab && cd Git-Tab && pip -r install requirements.txt
```
With that command executed, your ready to use Git-Tab.

# How-to Use
```sh
cd Git-Tab # If your not in the repository folder, run this.
python api.py # Finally, the API it's running on http://localhost:5000/.
```

To get the statistics of a user, add the query "username" with the user name as it's value.
It will return an HTML who can render on Web, OBS and more.

URL Example: http://localhost:5000/?username=ZSendokame

### How-to Add Twitch-Tab to OBS
1.- Right click on Sources tab.<br>
2.- Go to Add and Browser.<br>
3.- Create it and change URL text to "http://localhost:5000/?username=<Your GitHub Username\>".
