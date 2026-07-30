from sympy import *
from datetime import datetime

history = []
memory = None

print("=" * 55)
print("            ADVANCED SCIENTIFIC CALCULATOR")
print("=" * 55)
print("Examples:")
print("10+5")
print("(10+5)*2")
print("sqrt(81)")
print("sin(30)")
print("cos(60)")
print("tan(45)")
print("log(100)")
print("ln(10)")
print("factorial(5)")
print("\nCommands:")
print("history        - To show history")
print("clearhistory   - Clear history")
print("time           - To show date & time")
print("MS             - To Save last answer to memory")
print("MR             - To Recall memory")
print("MC             - To Clear memory")
print("clear          - To Clear screen")
print("exit           - To Exit calculator")
print("=" * 55)

last_result = None

while True:

    expression = input("\n>>> ").strip()

    command = expression.lower()

    if command == "exit":
        print("\nThank you for using Advanced Calculator!")
        break

    elif command == "clear":
        print("\n" * 40)
        continue

    elif command == "history":
        if history:
            print("\n------ HISTORY ------")
            for item in history:
                print(item)
        else:
            print("History is empty.")
        continue

    elif command == "clearhistory":
        history.clear()
        print("History cleared.")
        continue

    elif command == "time":
        print(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        continue

    elif command == "ms":
        if last_result is not None:
            memory = last_result
            print("Memory Saved.")
        else:
            print("No result available.")
        continue

    elif command == "mr":
        if memory is not None:
            print("Memory =", memory)
        else:
            print("Memory Empty.")
        continue

    elif command == "mc":
        memory = None
        print("Memory Cleared.")
        continue

    try:
        expression = expression.replace("^", "**")

        result = sympify(expression)

        last_result = result.evalf()

        print("=", last_result)

        history.append(f"{expression} = {last_result}")

    except Exception:
        print("Invalid Expression!")
