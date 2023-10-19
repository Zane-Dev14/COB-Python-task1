import tkinter as tk
from tkinter import ttk
def add_words():
    addWindow = tk.Toplevel(root)
    addWindow.title("Add Words to File")

    def add_to_file():
        text_to_add = text_entry.get()
        with open("file.txt", "a") as f:
            f.write(text_to_add + " ")
        text_entry.delete(0, "end")
        addWindow.destroy()

    label = ttk.Label(addWindow, text="Enter text to add to the file:", font=("Helvetica", 12, "bold"))
    label.pack(padx=10, pady=10)

    text_entry = ttk.Entry(addWindow, font=("Helvetica", 12))
    text_entry.pack(padx=10, pady=5)

    add_button = ttk.Button(addWindow, text="Add to File", command=add_to_file, style="TButton")
    add_button.pack(pady=10)

def count_words():
    countWindow = tk.Toplevel(root)
    countWindow.title("Count Words in File")

    def count():
        count={}
        with open("file.txt", "r") as f:
            words = f.read().split()
            for word in words:
                
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        result = "\n".join([f"{word} : {count}" for word, count in count.items()])
        result_label.config(text=result)

    label = ttk.Label(countWindow, text="Counting words in the file:", font=("Helvetica", 12, "bold"))
    label.pack(padx=10, pady=10)

    result_label = ttk.Label(countWindow, text="", font=("Helvetica", 12))
    result_label.pack(padx=10, pady=10)

    count_button = ttk.Button(countWindow, text="Count Words", command=count, style="TButton")
    count_button.pack(pady=10)

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Word Tool")
root.geometry("400x300")
root.configure(background="#f2f2f2")  

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12, "bold"))

add_button = ttk.Button(root, text="Add Words to File", command=add_words, style="TButton")
add_button.pack(pady=20, fill='both', expand='yes')

count_button = ttk.Button(root, text="Count Words in File", command=count_words, style="TButton")
count_button.pack(pady=20, fill='both', expand='yes')

exit_button = ttk.Button(root, text="Exit", command=exit_program, style="TButton")
exit_button.pack(pady=20, fill='both', expand='yes')

root.mainloop()
