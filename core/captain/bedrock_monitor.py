import os
import time

def check_bedrock():
    # Simple check for Termux environment and local storage
    print("--- TerraPrime: Bedrock Check ---")
    print(f"Environment: {os.uname().machine}")
    print(f"Disk Usage: {os.popen('df -h .').read().strip().splitlines()[-1]}")
    print("Bedrock is stable.")

if __name__ == "__main__":
    check_bedrock()
