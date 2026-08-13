from datetime import datetime
import os

log = ""
result = None

while True:
    error = "none"
    try:
        num1 = float(input("Enter a number : "))
        num2 = float(input("Enter another number : "))
        result = num1 / num2
    except Exception as e:
        error = e
        print(f"error : {error}")
    else:
        break
    finally:
        formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = log + str(formatted) + " : " + str(error) + "\n"

script_dir = os.path.dirname(os.path.abspath(__file__))
error_file_path = os.path.join(script_dir, "Error_log.txt")

with open(error_file_path, "w", encoding="utf-8") as error_file:
    error_file.write(log)

if result is not None:
    print(result)
else:
    print("No valid result was produced.")