import tkinter as tk
from pathlib import Path
from tkinter import ttk

from TkinterDnD2 import DND_FILES, TkinterDnD
import pandas as pd

class Application(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Exporter : CJ-47")
        self.main_frame =tk.Frame(self)
        self.main_frame.pack(fill="both",expand="true")
        self.geometry("800x400")
        self.search_page=SearchPage(parent=self.main_frame)

class DataTable(ttk.Treeview):
    def __init__(self,parent):
        super().__init__(parent)
        scroll_Y=tk.Scrollbar(self,orient="vertical",command=self.yview)
        scroll_X=tk.Scrollbar(self,orient="horizontal",command=self.xview) 
        self.configure(yscrollcommand=scroll_Y.set,xscrollcommand=scroll_X.set)
        scroll_Y.pack(side="right",fill="y")
        scroll_X.pack(side="bottom",fill="x")
        self.stored_dataframe=pd.DataFrame() 

class SearchPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.file_names_listbox=tk.Listbox(parent,selectmode=tk.SINGLE,background="darkgray")
        self.file_names_listbox.place(relheight=1,relwidth=0.25)
        self.file_names_listbox.drop_target_register(DND_FILES)
        self.file_names_listbox.dnd_bind("<<Drop>>")
        self.file_names_listbox.bind("<Double-1>")

        self.search_entrybox=tk.Entry(parent)
        self.search_entrybox.place(relx=0.25,relwidth=0.75)
        self.search_entrybox.bind("<Return")
        
        self.data_table=DataTable(parent)
        self.data_table.place(rely=0.05,relx=0.25,relwidth=0.75,relheight=0.95)



if __name__ =="__main__":
    root=Application()
    root.mainloop()

