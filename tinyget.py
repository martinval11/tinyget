from colorama import Fore
import requests
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-g','--get', type=str, help="HTTP GET Request", required=False)
parser.add_argument('-o','--output', type=str, help="Output of the request", required=True)
parser.add_argument('-p','--post', help="HTTP POST Request", required=False)
args = parser.parse_args()

if args.post:
    res_post = requests.post(args.post, stream=True)

    if res_post:
        output_post = args.output
        with open(output_post, 'wb') as f:
            res_post.raw.decode_content = True
            shutil.copyfileobj(res_post.raw, f)
    else:
        print("Response Failed" + Fore.RED, "(", res_post.status_code, ")" + Fore.RESET)

if args.get:
    res = requests.get(args.get, stream=True)

    if res:
        output = args.output
        with open(output, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
    else:
        print("Response Failed" + Fore.RED, "(", res.status_code, ")" + Fore.RESET)