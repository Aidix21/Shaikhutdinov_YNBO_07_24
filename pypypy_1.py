import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class VFSEmulator:
    def __init__(self, master):
        self.master = master
        self.master.title("VFS")
        self.create_widgets()
        # Можно добавить текущую директорию, если потребуется, но пока без функциональности файловой системы
        self.current_directory = "/"

    def create_widgets(self):
        # Область вывода результатов
        self.output_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, height=20, width=80)
        self.output_area.pack(padx=10, pady=10)

        # Поле для ввода команд
        self.entry = tk.Entry(self.master, width=80)
        self.entry.pack(padx=10, pady=(0,10))
        self.entry.bind("<Return>", self.execute_command)

        # Фокус на поле ввода
        self.entry.focus()

    def execute_command(self, event=None):
        raw_input = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        if not raw_input:
            return  # ничего не вводили

        # Разделение команды и аргументов
        parts = raw_input.split()
        cmd = parts[0]
        args = parts[1:]

        # Вызов соответствующей команды
        if cmd == "ls":
            self.cmd_ls(args)
        elif cmd == "cd":
            self.cmd_cd(args)
        elif cmd == "exit":
            self.cmd_exit()
        else:
            self.display_output(f"Ошибка: неизвестная команда '{cmd}'\n")

    def cmd_ls(self, args):
        # Заглушка — выводим команду и аргументы
        self.display_output(f"ls {' '.join(args)}\n")

    def cmd_cd(self, args):
        # Заглушка — выводим команду и аргументы
        if not args:
            self.display_output("Ошибка: команда 'cd' требует аргумент.\n")
        else:
            self.display_output(f"cd {' '.join(args)}\n")
            # Можно добавить проверку существования директории и смену текущей директории

    def cmd_exit(self):
        self.master.quit()

    def display_output(self, text):
        self.output_area.insert(tk.END, text)
        self.output_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VFSEmulator(root)
    root.mainloop()
