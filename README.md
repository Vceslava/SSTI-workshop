# SSTI-workshop


## Requirenments

1. Unix OS (Ubuntu, kali, etc)
2. Python 2.7
3. Flask

## How to install flask and configure app

1. Install virtualenv

```
$ sudo pip install virtualenv
or 
$ sudo apt-get install python-virtualenv 
```
[more info](http://flask.pocoo.org/docs/0.12/installation/)

2. create folder

```
$ mkdir ssti
$ cd ssti
```

3. copy "app" folder and paste it into ssti

```
-ssti
  |-app
    |-ssti.py
    |-templates
      |-base.html
      |-index.html
      
```
4. Create virtual environment

```
$ virtualenv ssti
$ . ssti/bin/activate
```

5. Install Flask

```
$ pip install Flask
```

## Start the app
```
$ python ssti.py
```


