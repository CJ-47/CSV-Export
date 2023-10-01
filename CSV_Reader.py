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
        self.file_names_listbox.dnd_bind("<<Drop>>",self.drop_inside_list_box)
        self.file_names_listbox.bind("<Double-1>",self._display_file)


        self.search_entrybox=tk.Entry(parent)
        self.search_entrybox.place(relx=0.25,relwidth=0.75)
        self.search_entrybox.bind("<Return",self.search_table)
        
        self.data_table=DataTable(parent)
        self.data_table.place(rely=0.05,relx=0.25,relwidth=0.75,relheight=0.95)
    
    def drop_inside_list_box(self,event):
        pass
    
    def _display_file(self,event):
        pass

    def _parse_drop_files(self,filename):
        pass

    def search_table(self,event):
        pass    


    def set_dataTable(self,dataframe):
        self.stored_dataframe=(dataframe)
        self.draw_table(dataframe)

    def _draw_table(self,dataframe):
        self.delete(*self.get_children())
        columns=list(dataframe.columns)
        self.__setitem__("column",columns)
        self.__setitems__("show","headings")

        for column in columns:
            self.heading(column,text=column)

        df_rows=dataframe.to_numpy().to_list()
        for row in df_rows:
            self.insert("","end",values=row)    

        return None    

    def reset_table(self):
        self._draw_table(self.stored_dataframe)

    def find_value(self,pairs):
        new_df=self.stored_dataframe
        for key,val in pairs.items():
            qury=f"{key}.str.contains('{val}')"
            new_df=new_df.query(qury,engine="python")
        self._draw_table(new_df)    
if __name__ =="__main__":
    root=Application()
    root.mainloop()

