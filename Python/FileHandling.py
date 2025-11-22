import os

filename = "myfile.txt"
filepath = os.path.join(os.getcwd(), filename)  # Full path in current folder

try:
    user_text = input("Write something to store in the file: ")

    with open(filepath, "a") as file:  # "a" = append mode
        file.write(user_text + "\n")

    print(f"Saved successfully! 📁 Location: {filepath}")

except Exception as e:
    print("Something went wrong:", e)
