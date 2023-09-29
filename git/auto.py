import schedule
import time
import subprocess

def push_code():
    print(f'Pushing code to git repository...')
    try:
        # Run git script
        subprocess.run(["python3", "script.py"])
        print("Code push successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# time to run
schedule.every(10).seconds.do(push_code)

# schedule continue
while True:
    schedule.run_pending()
    time.sleep(1)
