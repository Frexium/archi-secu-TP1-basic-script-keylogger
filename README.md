 # KeyLogger Python Scripts

This repository contains three scripts: `keylogger.py`, `keylogger_to_txt.py` and `keylogger_++.py` . These scripts allow you to create a basic keylogger that records keystrokes, logs them into a file, and provides some level of customization for your logging needs.

## WARNING: FOR EDUCATIONAL PURPOSES ONLY

These scripts are intended solely for educational and research purposes. Misusing this keylogger in any way that violates privacy laws, security policies, or ethical guidelines is strictly prohibited.

## Prerequisites

To use these scripts, ensure you have Python 3.x installed on your system. You can download the latest version from [official Python website](https://www.python.org/downloads/) or install it using package managers like apt-get (Debian-based systems) or homebrew (macOS).

Once you have Python installed, run `pip install pynput` to install the necessary library for capturing keyboard events.

## keylogger.py

This simple script records keystrokes and send the value of the key in the terminal.

### Usage:

```
python keylogger.py
```

## keylogger_to_txt.py

This script records keystrokes and logs them into a text file named "log.txt" on your Desktop. The file's repository can be changed by inputting the wanted path in the `path` variable. The log file is created if it doesn't exist, or appended to if it does. 

The logging interval can be adjusted by modifying the timer in the `report()` function.

### Usage:

```
python keylogger_to_txt.py
```

## keylogger_++.py

This script is a better version of the previous one. It send the logs either in a remote web server using an HTTP request, or save it locally. To choose wich option you prefer, either input the server's address, or "local" in the `server` variable.

The logging interval can be adjusted by modifying the timer in the `report()` function, and the file's repository can be changed by inputting the wanted path in the `path` variable.

### Usage:

```
python keylogger_++.py
```

### Log File Format:

The logs are saved as plain text, with each line representing a single keystroke or key event. Keystrokes are represented by their corresponding ASCII characters, while non-printable characters (such as function keys) are represented by their names. Special characters like space, enter, and backspace are also included in the log file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy using your KeyLogger scripts!
