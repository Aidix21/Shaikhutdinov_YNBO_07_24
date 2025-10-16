import tkinter as tk
from tkinter import scrolledtext


class VFSEmulator:
    def __init__(self, root):
        self.root = root
        self.root.title("VFS")

        self.output_area = scrolledtext.ScrolledText(root, state='disabled', height=20, width=80)
        self.output_area.pack(padx=10, pady=10)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.prompt = tk.Label(self.input_frame, text=">>>")
        self.prompt.pack(side=tk.LEFT)

        self.input_field = tk.Entry(self.input_frame, width=70)
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind('<Return>', self.process_command)

        self.display_welcome()

    def display_welcome(self):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, "Добро пожаловать\n")
        self.output_area.insert(tk.END, "Введите 'exit' для выхода\n\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)

    def process_command(self, event):
        command_text = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)

        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, f">>> {command_text}\n")

        if not command_text:
            self.output_area.config(state='disabled')
            self.output_area.see(tk.END)
            return

        parts = command_text.split()
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        if command == "exit":
            self.root.quit()
        elif command == "ls":
            self.output_area.insert(tk.END, f"ls команда выполнена с аргументами: {args}\n")
        elif command == "cd":
            self.output_area.insert(tk.END, f"cd команда выполнена с аргументами: {args}\n")
        else:
            self.output_area.insert(tk.END, f"Ошибка: неизвестная команда '{command}'\n")

        self.output_area.insert(tk.END, "\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = VFSEmulator(root)
    root.mainloop()
