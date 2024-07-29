
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please provide a valid input.")

def show_json(obj):
    print(obj)

