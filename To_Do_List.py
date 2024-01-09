import tkinter as tk
from tkinter import simpledialog

class Todo_List:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.master.geometry("500x500")
        self.master.configure(bg="pink")
        

        self.tasks = []

        self.task_listbox = tk.Listbox(self.master,bd='5',selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.master,text ="Create Task",bd='5',command = self.create_task)
        self.add_button.pack(pady=5)

        self.add_button = tk.Button(self.master,text ="Update Task",bd='5',command = self.update_task)
        self.add_button.pack(pady=5)

        self.add_button = tk.Button(self.master,text ="View Task",bd='5',command = self.view_task)
        self.add_button.pack(pady=5)

        self.add_button = tk.Button(self.master,text ="Complete Task",bd='5',command = self.complete_task)
        self.add_button.pack(pady=5)

        self.add_button = tk.Button(self.master,text ="Count Task",bd='5',command = self.show_task_count)
        self.add_button.pack(pady=5)

        self.add_button = tk.Button(self.master,text ="Save Task",bd='5',command = self.save_to_file)
        self.add_button.pack(pady=5)


    def create_task(self):
        task_name = simpledialog.askstring("Input","Enter Task Name:")
        if task_name:
            self.tasks.append(task_name)
            self.task_listbox.insert(tk.END,task_name)

    def view_task(self):
        if not self.tasks:
            simpledialog.messagebox.showinfo("To-do List","No Task in to-do list")
        else:
            task_index=self.task_listbox.curselection()
            if task_index:
                selected_task=self.task_listbox.get(task_index)
                simpledialog.messagebox.showinfo("To-do List",f"selected task{selected_task}")

    def complete_task(self):
        task_index=self.task_listbox.curselection()
        if task_index:            
            completed_task=self.task_listbox.get(task_index)
            self.task_listbox.delete(task_index)
            simpledialog.messagebox.showinfo("To-do List",f"Task '{completed_task}'marked as completed.")
 
    def update_task(self):
        task_index=self.task_listbox.curselection()
        if task_index:
           old_task=self.task_listbox.get(task_index)
           new_task=simpledialog.askstring("Input",f"update Task'{old_task}':" , initialvalue=old_task)
           if new_task:
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(tk.END,new_task)
            simpledialog.messagebox.showinfo("To-do List",f"Task Updated '{new_task}'")

    def save_to_file(self):
        filename = simpledialog.askstring("Input","Enter File name to Save.")
        if filename:
            with open (filename, "w")as file:
                for task in self.tasks:
                    file.write(task + "\n")
            simpledialog.messagebox.showinfo("To-do List", f"To-do list saved to {filename}.")   

    def show_task_count(self):
        task_count = len(self.tasks)
        simpledialog.messagebox.showinfo("To-do List", f"Total tasks: {task_count}")                      
    

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = Todo_List(root)
    root.mainloop()








