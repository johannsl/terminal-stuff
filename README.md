# terminal-stuff
This is a guide for installing and configuring useful terminal tools for MacOSX and Raspbian.

![Terminal screenshot](https://raw.githubusercontent.com/johannsl/terminal-stuff/master/example_image.png)

# MacOSX

## Get homebrew 
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Get iterm2
```
brew cask install iterm2
```

## Get zsh and Oh My Zsh
```
brew install zsh zsh-completions
curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
chsh -s /bin/zsh 
```
Change /bin/zsh with the path to your zsh. Check this by using 
```
which zsh
```

## Get exa
```
brew install exa
```

## Use configuration files
Add .vimrc to your home directory. Keep the old version just in case. This changes the way vim looks.  
Add .zshrc to your home directory. Keep the old version just in case. This changes the way the terminal looks and works. You might want to change some parameters in this file, like perhaps the PATH variable in line 53. PATH describes where the terminal looks for binary files, which might be different on your computer. Binary files are programs that can be run from the terminal (just like zsh).

# Raspbian

## Crontab
Add the availability_write.py script to contab so that it is run on a schedule.
 ```
crontab -e
```
The availability_write.py script is configurated to run every two hours.
```
* * * * * cd path/to/terminal-stuff/ && python availability_write.py
```

## Check status
Run the availability_read.py script to see availability values.
```
python availability_read.py
```
