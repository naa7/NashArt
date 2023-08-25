# NashArt 
<h3> Najeeb | Andy Zheng | Sung Yi | Haad Azher </h3>

---


## Description
Welcome fellow art enthusiasts! This project links the arts and tech together by providing a chat-bot that runs in your local Discord server. Ask it questions regarding art such as history, specific pieces, styles, and more.


## Install

1. On Windows git clone repo
2. cd into NashArt
3. activate Environment using

```
 .\APIs\env\bin\Activate.ps1
```

- For Execution Policy Warning run Powershell as Administrator
- **OR** run

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope
```

4. cd into APIs
5. run

```
py -m pip install -r requirements.txt
```

6. run

```
py api1_test.py
```

**OR**
run

```
py api2_test.py
```

## Usage
A commands list is provided for you using the "/help" command. The NashArt bot currently features "/ask" to ask a question, and "/tts-ask" to ask a question with a response in "text-to-speech"
