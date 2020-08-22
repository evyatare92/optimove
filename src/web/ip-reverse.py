from flask import Flask, redirect, request, render_template
import redis
import os

app = Flask(__name__)

def get_reverse_ip(ip):
    split_ip = ip.split('.')
    split_ip.reverse()
    return ('.'.join(split_ip))

def save_to_redis(val):
    try:
        redis_server = os.getenv("REDIS_SERVER")
        redis_port = int(os.getenv("REDIS_PORT"))
        redis_password = os.getenv("REDIS_PASSWORD")
        redis_key = os.getenv("REDIS_KEY")
        rdb = redis.Redis(host=redis_server, port=redis_port, db=0, password=redis_password)
        rdb.set(name=redis_key, value=val)
        return "Saved successfully to redis"
    except BaseException as e:
        return e

@app.route('/',methods=['GET'])
def get_ip():
    return render_template("getip.html")

@app.route('/reverse',methods=['GET'])
def show_reverse_ip():
    ip = request.args.get('ip')
    reverse_ip = get_reverse_ip(ip)
    message = save_to_redis(reverse_ip)
    return render_template("reverse_ip.html", ip=reverse_ip, message=message)

app.run(host="0.0.0.0", port=80, debug=False)
