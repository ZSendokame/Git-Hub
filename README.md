# Git-Hub
Show github statistics on web, made for Twitch overlay!<br>
It will automatically update every ten minutes and it shows the information of users and repositories.

![image](https://user-images.githubusercontent.com/70088953/158917446-d9eff0d2-f6f9-49fa-9441-facc2955ea48.png)

# How-to Install
```sh
git clone https://github.com/zsendokame/Git-Hub && cd Git-Hub && pip -r install requirements.txt
```
With that command executed, your ready to use Git-Tab.

# How-to Use
```sh
cd Git-Hub # If your not in the repository folder, run this.
python api.py # Finally, the API it's running on http://localhost:5000/.
```

URL Examples:<br>
Account URL: http://localhost:5000/account?username=ZSendokame<br>
Repository URL: http://localhost:5000/repository?owner=ZSendokame&name=Git-Hub

### How-to Add Git-Hub to OBS
- Right click on Sources tab.<br>
- Go to Add and Browser.<br>
- Create it and change URL text to the type you need.
