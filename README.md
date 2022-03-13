# Git Tab
Show github statistics on web, made for Twitch overlay!<br>
It will automatically update every ten minutes and it shows the information of users and repositories.

![image](https://user-images.githubusercontent.com/70088953/158082146-8a5257c4-a075-4bbf-84c8-ba6587298691.png)

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
URL Examples:<br>
Account URL: http://localhost:5000/account?username=ZSendokame<br>
Repository URL: http://localhost:5000/repository?username=ZSendokame&name=Git-Tab

### How-to Add Twitch-Tab to OBS
1.- Right click on Sources tab.<br>
2.- Go to Add and Browser.<br>
3.- Create it and change URL text to the type you need.
