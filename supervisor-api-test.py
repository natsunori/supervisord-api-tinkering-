from flask import Flask, jsonify
from xmlrpc.client import ServerProxy

app = Flask(__name__)

@app.route('/val', methods=['GET'])
def get_valheim_server_info():
    server = ServerProxy('http://admin:testing@192.168.1.97:9001/RPC2')
    try:
        # Get process info for 'valheim-server'
        process_info = server.supervisor.getProcessInfo('valheim-server')
        
        if process_info['statename'] != 'RUNNING':
            return jsonify({"error": "Server not running"}), 418
        
        return jsonify(process_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)