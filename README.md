# 📸 Screenshot Monitor for WSL

I was using Claude Code CLI and this does not have access to your screenshot folder in the windows system. I made a quick little script that you can have running in the background that will automatically copy a screenshot from the windows screenshot folder over to the wsl side
and put it in the folder of your choosing. I added a section to rename it from the windows name with spaces and - to a more acceptable linux name. 



---

## 🔧 Requirements

- Python 3
- WSL (Windows Subsystem for Linux)
- [`watchdog`](https://pypi.org/project/watchdog/) Python package

Install it with:

```bash
pip install watchdog
If this doesn't work do sudo apt install python3-watchdog as my WSL wouldnt install it normally because its a contained environment. 
