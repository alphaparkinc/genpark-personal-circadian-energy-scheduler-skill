import json, sys
from client import PersonalCircadianEnergySchedulerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "personal-circadian-energy-scheduler", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "align_circadian_tasks", "description": "Aligns personal tasks to biological chronotype peaks, protecting prime analytical windows."}]}}
    elif method == "tools/call":
        client = PersonalCircadianEnergySchedulerClient()
        res = client.align_circadian_tasks()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = PersonalCircadianEnergySchedulerClient()
        print(json.dumps(client.align_circadian_tasks(), indent=2))
