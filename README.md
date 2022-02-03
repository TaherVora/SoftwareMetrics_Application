# CECS-543
```prettier
> Python GUI with PyQt
```

### Command to run designer 
```commandline
/usr/lib/x86_64-linux-gnu/qt5/bin/designer
```

### Convert ui file to py code
```commandline
pyuic5 gui/mainwindow.ui -o pyui/main_window.py
```

### Create EXE from python code using pyinstaller
```commandline
pyinstaller --onefile main.py
```