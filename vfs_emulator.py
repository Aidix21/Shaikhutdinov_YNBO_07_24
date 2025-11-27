import tkinter as tk
from tkinter import scrolledtext
import sys
import os


class VFSEmulator:
    def __init__(self, root, vfs_path=None, script_path=None):
        self.root = root
        self.root.title("VFS")

        # Параметры конфигурации
        self.vfs_path = vfs_path or os.getcwd()
        self.script_path = script_path

        self.output_area = scrolledtext.ScrolledText(root, state='disabled', height=20, width=80)
        self.output_area.pack(padx=10, pady=10)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.prompt = tk.Label(self.input_frame, text=">>>")
        self.prompt.pack(side=tk.LEFT)

        self.input_field = tk.Entry(self.input_frame, width=70)
        self.input_field.pack(side=tk.LEFT, padx=5)
        self.input_field.bind('<Return>', self.process_command)

        # Отладочный вывод параметров
        self.display_config()
        self.display_welcome()

        # Выполнение стартового скрипта если указан
        if self.script_path:
            self.execute_startup_script()

    def display_config(self):
        """Вывод параметров конфигурации"""
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, "=== Параметры конфигурации ===\n")
        self.output_area.insert(tk.END, f"VFS путь: {self.vfs_path}\n")
        self.output_area.insert(tk.END, f"Скрипт: {self.script_path}\n")
        self.output_area.insert(tk.END, "==============================\n\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)

    def display_welcome(self):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, "Добро пожаловать\n")
        self.output_area.insert(tk.END, "Введите 'exit' для выхода\n")
        self.output_area.insert(tk.END, "Введите 'conf-dump' для вывода конфигурации\n\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)

    def execute_startup_script(self):
        """Выполнение стартового скрипта"""
        try:
            with open(self.script_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, f"=== Выполнение скрипта: {self.script_path} ===\n")
            self.output_area.config(state='disabled')

            for line_num, line in enumerate(lines, 1):
                command_text = line.strip()
                if not command_text or command_text.startswith('#'):
                    continue

                # Имитация ввода пользователя
                self.output_area.config(state='normal')
                self.output_area.insert(tk.END, f">>> {command_text}\n")
                self.output_area.config(state='disabled')
                self.root.update()

                # Обработка команды
                self.process_script_command(command_text, line_num)

        except FileNotFoundError:
            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, f"Ошибка: скрипт не найден: {self.script_path}\n")
            self.output_area.config(state='disabled')
        except Exception as e:
            self.output_area.config(state='normal')
            self.output_area.insert(tk.END, f"Ошибка выполнения скрипта: {str(e)}\n")
            self.output_area.config(state='disabled')

        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, "=== Завершение выполнения скрипта ===\n\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)

    def process_script_command(self, command_text, line_num):
        """Обработка команды из скрипта"""
        if not command_text:
            return

        parts = command_text.split()
        command = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        self.output_area.config(state='normal')

        if command == "exit":
            self.output_area.insert(tk.END, "Команда exit проигнорирована в скрипте\n")
        elif command == "ls":
            self.output_area.insert(tk.END, f"ls команда выполнена с аргументами: {args}\n")
        elif command == "cd":
            self.output_area.insert(tk.END, f"cd команда выполнена с аргументами: {args}\n")
        elif command == "conf-dump":
            self.output_area.insert(tk.END, "=== Конфигурация ===\n")
            self.output_area.insert(tk.END, f"VFS путь: {self.vfs_path}\n")
            self.output_area.insert(tk.END, f"Скрипт: {self.script_path}\n")
            self.output_area.insert(tk.END, "===================\n")
        else:
            self.output_area.insert(tk.END, f"Ошибка в строке {line_num}: неизвестная команда '{command}'\n")

        self.output_area.insert(tk.END, "\n")
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
        elif command == "conf-dump":
            self.output_area.insert(tk.END, "=== Конфигурация ===\n")
            self.output_area.insert(tk.END, f"VFS путь: {self.vfs_path}\n")
            self.output_area.insert(tk.END, f"Скрипт: {self.script_path}\n")
            self.output_area.insert(tk.END, "===================\n")
        else:
            self.output_area.insert(tk.END, f"Ошибка: неизвестная команда '{command}'\n")

        self.output_area.insert(tk.END, "\n")
        self.output_area.config(state='disabled')
        self.output_area.see(tk.END)


def parse_arguments():
    """Парсинг аргументов командной строки"""
    vfs_path = None
    script_path = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--vfs-path" and i + 1 < len(sys.argv):
            vfs_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--script" and i + 1 < len(sys.argv):
            script_path = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    return vfs_path, script_path


if __name__ == "__main__":
    vfs_path, script_path = parse_arguments()

    root = tk.Tk()
    app = VFSEmulator(root, vfs_path, script_path)
    root.mainloop()
