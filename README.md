# tinyget
A Minimal HTTP Requester

<p align="center">
<img src="https://github.com/martinval11/tinyget/blob/main/example/example.gif"/>
</p>

## Installation

```console
$ git clone https://github.com/martinval11/tinyget/
$ cd tinyget
$ bash install.sh
```

## Usage

```console
$ tinyget -h
usage: tinyget [-h] [-g GET] -o OUTPUT [-p POST]

options:
  -h, --help            show this help message and exit
  -g GET, --get GET     HTTP GET Request
  -o OUTPUT, --output OUTPUT
                        Output of the request
  -p POST, --post POST  HTTP POST Request
```

To get an image
```
tinyget -g 'https://picsum.photos/id/237/536/354' -o 'AnImage.jpg'
```
Info: Works with any type of file
