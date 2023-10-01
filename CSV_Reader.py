import tkinter as tk
from pathlib import Path
from tkinter import ttk,Label

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

    def set_data_table(self,dataframe):
        self.stored_dataframe=(dataframe)
        self._draw_table(dataframe)

    
    def save_newtable(self,name):
        new_df=self.stored_dataframe
        name+=".csv"
        csv_data = new_df.to_csv(name, index = True)

    def filter(self,cols):
        new_df=self.stored_dataframe
        new_df=new_df[cols]
        self._draw_table(new_df)
        self.stored_dataframe=new_df



    def _draw_table(self,dataframe):
        self.delete(*self.get_children())
        columns=list(dataframe.columns)
        
        self.__setitem__("column",columns)
        self.__setitem__("show","headings")

        for column in columns:
            self.heading(column,text=column)

        df_rows=dataframe.to_numpy().tolist()
        for row in df_rows:
            self.insert("","end",values=row)    

        return None    

    def reset_table(self):
        self._draw_table(self.stored_dataframe)

    def find_value(self,pairs):                 
        def srch(x):
            flg=True
            L=[]
            for key,val in pairs.items():
                if not str(x[key]).lower().__contains__(str(val).lower()):
                    flg=False
            if(flg):
                return x 
        #qury=f"{key}.str.contains('{str(val)}')"
        #qury=f"`{key}`=={str(val)} or {key}.str.contains('val')"
        #qury=str([pairs[0]]).lower().__contains__(str(pairs[1]).lower())
        #new_df=new_df.query(qury,engine="python")
        new_df=self.stored_dataframe
        new_df=new_df.apply(lambda x: srch(x),axis=1 )
        new_df=new_df.dropna()
        self._draw_table(new_df)
        self.stored_dataframe=new_df

class SearchPage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.file_names_listbox=tk.Listbox(parent,selectmode=tk.SINGLE,background="darkgray")
        self.file_names_listbox.place(relheight=1,relwidth=0.25)
        self.file_names_listbox.drop_target_register(DND_FILES)
        self.file_names_listbox.dnd_bind("<<Drop>>",self.drop_inside_list_box)
        self.file_names_listbox.bind("<Double-1>",self._display_file)


        self.search_entrybox=tk.Entry(parent)
        self.srch = Label(parent,text = "Enter to Search->").place(relx = 0.25) 
        self.search_entrybox.place(relx=0.37,relwidth=0.63)
        self.search_entrybox.bind("<Return>",self.search_table)
        self.filter_entrybox=tk.Entry(parent)
        self.filter_entrybox.bind("<Return>",self.filter_table)
        self.srch = Label(parent,text = "Enter to Filter->").place(relx = 0.25,rely=0.05)
        self.filter_entrybox.place(relx=0.37,relwidth=0.63,rely=0.05)
        self.data_table=DataTable(parent)
        self.data_table.place(rely=0.20,relx=0.25,relwidth=0.75,relheight=0.95)

        self.sv = Label(parent,text = "File Name->").place(relx = 0.25,rely=0.10) 
        self.save_entrybox=tk.Entry(parent)
        self.save_entrybox.place(relx=0.37,relwidth=0.63,rely=0.10)
        self.save_entrybox.bind("<Return>",self.save_table)

        self.path_map={}

    

    def drop_inside_list_box(self,event):
        file_paths=self._parse_drop_files(event.data)
        current_listbox_items=set(self.file_names_listbox.get(0,"end"))
        for file in file_paths:
            if file.endswith(".csv"):
                path_object=Path(file)
                file_name=path_object.name
            if file_name not in current_listbox_items:
                self.file_names_listbox.insert("end",file_name)
                self.path_map[file_name]=file

    
    def _display_file(self,event):
        file_name=self.file_names_listbox.get(self.file_names_listbox.curselection())
        path=self.path_map[file_name]
        df=pd.read_csv(path)
        self.data_table.set_data_table(df)

    def _parse_drop_files(self,filename):
        sze=len(filename)
        res=[]
        name=""
        ind=0
        while ind<sze:
            if filename[ind] =="{":
                j=ind+1
                while filename[j]!="}":
                    name+=filename[j]
                    j+=1
                res.append(name)
                name=""
                ind=j
            elif filename[ind]==" " and name !="":
                    res.append(name)
                    name=""
            elif filename[ind] !=" ":
                name+=filename[ind]
            ind+=1
        if name!="":
            res.append(name)
        return res
    
    def search_table(self,event):
            entry=self.search_entrybox.get()
            if entry=="":
                self.data_table.reset_table()
            else:
                entry_split=entry.split(",")
                column_val_pairs={}
                for pair in entry_split:
                    pair_split=pair.split("=")
                    if len(pair_split)==2:
                        col=pair_split[0]
                        lookup_val=pair_split[1]
                        column_val_pairs[col]=lookup_val
                self.data_table.find_value(column_val_pairs)        

    def filter_table(self,event):
            entry=self.filter_entrybox.get()
            if entry=="":
                self.data_table.reset_table()
            entry=entry.split(',')
            print(entry)
            self.data_table.filter(entry)    
            
    def save_table(self,event):
        entry=self.save_entrybox.get()
        self.data_table.save_newtable(entry)




        
if __name__ =="__main__":
    root=Application()
    root.mainloop()

