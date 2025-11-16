import sys
sid = sys.stdin.read().strip()
print("Success" if not sid else f"Success {sid}")
