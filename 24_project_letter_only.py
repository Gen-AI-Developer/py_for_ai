import string
def is_letter_only(text:str)-> None:
    alphabet:str = string.ascii_letters + ' '
    for char in text:
        if char not in alphabet:
            raise ValueError("Text must contain only letters and spaces.")
    print(f"Text: {text} is Letters-only, good job!")

def main() -> None:
    user_input = input("Enter some text(): ")
    try:
        is_letter_only(user_input)
    except ValueError:
        print("ValueError: Text must contain only letters and spaces.")
    except Exception as e:
        print(f"An unknown error occurred: {type(e).__name__}")
    else:
        print("No errors occurred.")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    main()
