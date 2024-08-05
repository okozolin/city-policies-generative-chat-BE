
def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please provide a valid input.")

def show_json(obj):
    print(obj)

def show_content(obj):
    value = extract_value(obj)
    hebrew_value = reverse_hebrew_text(value)
    print(f"A: {hebrew_value}\n")

def extract_value(sync_cursor_page):
    try:
        # Access the first message in the data list
        message = sync_cursor_page.data[0]
        # Access the first content block in the message content
        content_block = message.content[0]
        # Extract the value from the text content block
        return content_block.text.value
    except (AttributeError, IndexError) as e:
        print(f"Error: {e} - The object structure might be different than expected.")
        return None

def reverse_hebrew_text(text):
    lines = text.split('\n')
    reversed_lines = [line[::-1] for line in lines]
    return '\n'.join(reversed_lines)