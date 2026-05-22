import requests
import time
import json

RELAY_URL = "https://nexus-relay-production.up.railway.app"
SECRET = "pantheon_prime"

def send_strike(action, params=None):
    """Sends a direct command to the Red Magic via Nexus Relay."""
    payload = {
        "action": action,
        "params": params or {},
        "timestamp": time.time()
    }
    headers = {"X-Secret": SECRET, "Content-Type": "application/json"}
    
    print(f"🚀 IGNIS STRIKE: {action}...")
    try:
        r = requests.post(f"{RELAY_URL}/command", json=payload, headers=headers)
        r.raise_for_status()
        command_id = r.json().get("_id")
        print(f"📡 Command Queued: {command_id}")
        return command_id
    except Exception as e:
        print(f"❌ Relay Failure: {e}")
        return None

def poll_result(command_id, timeout=60):
    """Polls for the result of the strike."""
    headers = {"X-Secret": SECRET}
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(f"{RELAY_URL}/result/{command_id}", headers=headers)
            if r.status_code == 200:
                return r.json().get("result")
        except:
            pass
        time.sleep(2)
    return "TIMEOUT"

if __name__ == "__main__":
    # STRIKE 1: Launch Browser to Lee County Foreclosures
    cmd_id = send_strike("launch_app", {"package": "com.android.chrome", "url": "https://www.lee.realforeclose.com"})
    
    if cmd_id:
        print("⏳ Waiting for Ocular Link (Red Magic) to stabilize...")
        # Give the phone time to bypass the JS challenge
        time.sleep(10)
        
        # STRIKE 2: Dump UI Tree (The Harvest)
        data_cmd = send_strike("dump_ui")
        result = poll_result(data_cmd)
        
        with open("ignis_prime/raw_harvest.json", "w") as f:
            json.dump(result, f)
        print("✅ RAW SIGNAL HARVESTED. VOIDING SOURCE.")
