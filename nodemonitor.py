from threading import Timer
import json,os,datetime,requests
from dotenv import load_dotenv
load_dotenv()

def main():
    
    node = os.environ.get("node_endpoint")
    results = requests.get(node, timeout=5)
    try:
        if results.status_code == 200:
            notification(f"{node} is down")
            logerror(node+" went down at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    except requests.exceptions.ConnectionError as httpError:
        notification(httpError)
    
    
    Timer(5,main).start()

def notification(arg):
    data = {
        "text": arg
    }

    webhook = os.environ.get("webhook_url")
    requests.post(webhook, json.dumps(data))

def logerror(error):
    file=open("/var/log/nodemonitor.log", "a+")
    file.write(error)
    file.close()


if __name__ == '__main__':
    main()