from tkinter import *
import tkinter.scrolledtext as ScrolledText 
import os
from tkinter.filedialog import *
import tkinter.messagebox	

  
root=Tk()
root.iconbitmap(r"C:\Users\Ayush\Desktop\sample\icons\icons\favicon.ico")
root.title("Text Editor")
textArea=ScrolledText.ScrolledText(root,width=2000,height=1000)
text=Text(root,width=350,height=100)
text.grid()
menu=Menu(root)
root.config(menu=menu)

def new(event=None):
	root.title("untitled")
	global file_name
	file_name=None
	text.delete(1.0,END)



def open():
    askopenfilename()



def save():

    filename = asksaveasfilename()

    if filename:

        alltext = text.get(1.0, END)                      

        open(filename, 'w').write(alltext) 

def Saveas(self, app, pad):
        """
        saves the contents in pad to file
        to specified filename
        """
        save_file = asksaveasfilename(parent=app)
        data = pad.get('1.0', GUI.END)[:-1]
        f = open(save_file, 'w')
        f.write(data)
        f.close()
        x = save_file
        if platform.system() == 'Windows':
            x = x.replace('/', '\\')
            File.filename(map(str, x.split('\\'))[-1])
        else:
            pass
        File.filepath(x)
        app.title(File.name)

def cut():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)






def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 

def paste():

    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Errore","Gli appunti sono vuoti!")

def undo():
	if not stack:
		return
	previous = stack.pop()
	previous.undo()

def help(event=None):
    tkinter.messagebox.showinfo(
        "Help", "this is basic a notes making pad made by python",
        icon='question')

def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output

def on_content_changed(event=None):
    update_line_numbers()
    update_cursor()


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')


# Adding Cursor Functionality
def show_cursor():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)

#Adding Text Highlight Functionality
def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add(
        "active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()

# ICONS for the compound menu
new_file_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\new_file.gif')
open_file_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\open_file.gif')
cut_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\cut.gif')
copy_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\copy.gif')
paste_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\paste.gif')
undo_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\undo.gif')
redo_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\redo.gif')
find_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\find_text.gif')

#for file in the menu bar 
fileMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="new",accelerator='ctrl+N',compound='left',image=new_file_icon,command=new)
fileMenu.add_command(label="open",accelerator='ctrl+O',compound='left',image=open_file_icon,command=open)
fileMenu.add_command(label="save",accelerator='ctrl+S',compound='left',command=save)
fileMenu.add_command(label="save as",accelerator='ctrl+sht+S',command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=root.destroy)

#for open  in the menu bar
EditMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=EditMenu)
EditMenu.add_command(label="undo",accelerator='ctrl+U',compound='left',image=undo_icon,command=new)
EditMenu.add_command(label="cut",accelerator='ctrl+X',compound='left',image=cut_icon,command=cut)
EditMenu.add_command(label="copy",accelerator='ctrl+C',compound='left',image=copy_icon,command=copy)
EditMenu.add_command(label="paste",accelerator='ctrl+V',compound='left',image=paste_icon,command=paste)
EditMenu.add_separator()
EditMenu.add_command(label="Exit",command=root.destroy)

#for view in the menu bar
ViewMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="view",menu=ViewMenu)
ViewMenu.add_command(label="status bar",command=new) 
ViewMenu.add_command(label="hide menu",command=new)
ViewMenu.add_command(label="enter full screen",command=new)
ViewMenu.add_separator()
ViewMenu.add_command(label="Exit",command=root.destroy)

#for about in menu bar
aboutMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="about",menu=aboutMenu)
aboutMenu.add_command(label="help",command=help)
aboutMenu.add_separator()
aboutMenu.add_command(label="Exit",command=root.destroy)


root.mainloop()




