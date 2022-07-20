<div  align="center">
<h1  align="center">Dockerized Django Phone Number Verifier using random Code and sending Activation Code using Celery</h1>
</div>

## Installation

1. first, You should clone this Repository.<br/>
2. delete the txt file exists in db folder
3. Create an account in <a href="https://www.twilio.com">twilio<a/>
4. set Your twilio Number ACCOUNT_SID and AUTH_TOKEN at lines 136, 137 in app settings file
5. set Your twilio Number in ``` main/mixins:MessageHandler ``` line 17
6. at the sixth step, go to the Cloned Directory, then Open Terminal(CMD). <br/>
7. then, type ```docker-compose up --build ``` and Press Enter. (tip: make sure that Docker and Docker-Compose is Installed on Your Machine)
8. tip: username is ``` admin ``` and password is ``` admin ```


### Good Luck
