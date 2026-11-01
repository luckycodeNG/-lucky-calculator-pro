# Lucky Calculator Pro - CLI Version
# Built by luckycodeNG from Udi, Enugu

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Error: can't divide by 0"

print("=== Lucky Calculator Pro ===")
print("From Udi, Enugu to the World!")

while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.History 6.Exit")
    ch = input("Choose: ")
    if ch=="6": 
        print("Thanks! Follow me @luckycodeNG")
        break
    if ch=="5":
        try:
            with open("lucky_history.txt","r") as f: print(f.read())
        except: print("No history yet")
        continue
    try:
        a=float(input("First number: "))
        b=float(input("Second number: "))
        if ch=="1": r=add(a,b)
        elif ch=="2": r=sub(a,b)
        elif ch=="3": r=mul(a,b)
        elif ch=="4": r=div(a,b)
        else: continue
        print(f"Result: {r}")
        with open("lucky_history.txt","a") as f: f.write(f"{a} op {b} = {r}\n")
    except Exception as e: print(f"Error: {e}")
