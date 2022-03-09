from colorama import Fore
import requests
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g","--get", type=str, help="HTTP GET Request", required=False)
    parser.add_argument("-o","--output", type=str, help="Output of the request", required=True)
    parser.add_argument("-p","--post", help="HTTP POST Request", required=False)
    args = parser.parse_args()

    # Color Aliases
    RESET = Fore.RESET
    RED   = Fore.RED
    GREEN = Fore.GREEN

    if args.post:
        print("Resolving URL...")
        try:
            res_post = requests.post(args.post, stream=True)

            if res_post:
                output_post = args.output
                with open(output_post, "wb") as f:
                    res_post.raw.decode_content = True
                    shutil.copyfileobj(res_post.raw, f)
                print(GREEN + "The request has been successful!" + RESET)
            else:
                print("Response Failed" + RED, "(", res_post.status_code, ")" + RESET)

        except requests.exceptions.ConnectionError:
            print(RED + "Failed to establish a new connection (Temporary failure in name resolution)" + RESET)

    if args.get:
        try:
            print("Resolving URL...")
            res = requests.get(args.get, stream=True)
            
            if res:
                output = args.output
                with open(output, "wb") as f:
                    res.raw.decode_content = True
                    shutil.copyfileobj(res.raw, f)
                print(GREEN + "The request has been successful!" + RESET)
            else:
                print("Response Failed" + RED, "(", res.status_code, ")" + RESET)

        except requests.exceptions.ConnectionError:
            print(RED + "Failed to establish a new connection (Temporary failure in name resolution)" + RESET)
main()