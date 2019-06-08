import sys
import argparse
from github import Github
import time

banner = """

        ██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗████████╗
        ██╔══██╗╚██╗██╔╝██╔════╝ ██╔════╝ ██║╚══██╔══╝
        ██║  ██║ ╚███╔╝ ██║█████╗██║  ███╗██║   ██║
        ██║  ██║ ██╔██╗ ██║╚════╝██║   ██║██║   ██║
        ██████╔╝██╔╝ ██╗╚██████╗ ╚██████╔╝██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝   ╚═╝
                                    daleybee@pm.me
         help: {} -h  
         
   Please be aware of GitHub rate limits. Use in intervals.                      
""".format(sys.argv[0])

print(banner)
# so users can read warning about rate limits in banner


# tools arguments
parser = argparse.ArgumentParser()
parser.add_argument("-dxc", "--dxc", help="scan for dxc assets",
                    action="store_true")
parser.add_argument("-csc", "--csc", help="scan for csc assets",
                    action="store_true")
parser.add_argument("-hpe", "--hpe", help="scan for hpe assets",
                    action="store_true")
parser.add_argument("-io", "--io", help="scan for dxcdigital.io assets",
                     action="store_true")
parser.add_argument("-full", "--full", help="scan for all assets",
                    action="store_true")

args = parser.parse_args()

# to search through all public repos, we must first authenticate to github
github_key = input(" Enter GitHub access token: ")

time.sleep(5)

if args.io:
    print(" Loading endpoints and initializing Git client..")
    # auth
    g = Github(github_key)
    #load endpoints
    with open('dxc_io_endpoints.config') as f:
        for line in f:
            repositories = g.search_code(query=line)
            for repo in repositories:
                response = repo.html_url
                print("\n [!] Potentially sensitive data found: " + response)  

if args.dxc:
    print(" Loading endpoints and initializing Git client...")
    # auth
    g = Github(github_key)
    # load endpoints
    with open('dxc_endpoints.config') as f:
        for line in f:
            repositories = g.search_code(query=line)
            for repo in repositories:
                response = repo.html_url
                print("\n [!] Potentially sensitive data found: " + response)

if args.csc:
    print(" Loading endpoints and initializing Git client...")
    # auth
    g = Github(github_key)
    # load endpoints
    with open('csc_endpoints.config') as f:
        for line in f:
            repositories = g.search_code(query=line)
            for repo in repositories:
                response = repo.html_url
                print("\n [!] Potentially sensitive data found: " + response)

if args.hpe:
    print(" Loading endpoints and initializing Git client...")
    # auth
    g = Github(github_key)
    # load endpoints
    with open('hpe_endpoints.config') as f:
        for line in f:
            repositories = g.search_code(query=line)
            for repo in repositories:
                response = repo.html_url
                print("\n [!] Potentially sensitive data found: " + response)

if args.full:
    print(" Loading endpoints and initializing Git client...")
    # auth
    g = Github(github_key)
    # load endpoints
    with open('all_endpoints.config') as f:
        for line in f:
            repositories = g.search_code(query=line)
            for repo in repositories:
                response = repo.html_url
                print("\n [!] Potentially sensitive data found: " + response)

