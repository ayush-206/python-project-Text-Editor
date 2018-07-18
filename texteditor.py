from tkinter import *
import os
import tkinter.filedialog
import tkinter.messagebox

root = Tk()
root.iconbitmap(r"C:\Users\Ayush\Desktop\sample\icons\icons\favicon.ico")

name = "TextEditor"
root.title(name)
file_name = None
root.geometry('900x500')


#functions
# File Menu
def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)
    on_content_changed()


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                    ("HTML", "*.html"), ("CSS", "*.css"),
                                                                    ("JavaScript", "*.js")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name),name))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())

    on_content_changed()


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                    
                                                                     ("JavaScript", "*.js")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name),name))
    return "break"


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"
#End of file menu

# For Edit Menu
def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"


def copy():
    content_text.event_generate("<<Copy>>")
    on_content_changed()
    return "break"


def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"


def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return "break"


def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return "break"

#End of Edit Menu
# ABOUT MENU

def display_help(event=None):
    tkinter.messagebox.showinfo(
        "Help", "this is a simple text editor like notepad",
        icon='question')


def exit_editor(event=None):
    
        root.destroy()


# Here, adding Line Numbers Functionality
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


# Here ,Adding Cursor Functionality
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


# Here, Adding Text Highlight Functionality
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


# Adding Change Theme Functionality
def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(
        background=background_color, fg=foreground_color)


# pop-up menu
def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)
    
    #End of About Menu
    


# Icons for the compound menu path
new_file_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\new_file.gif')
open_file_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\open_file.gif')
cut_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\cut.gif')
copy_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\copy.gif')
paste_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\paste.gif')
undo_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\undo.gif')
redo_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\redo.gif')
find_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\find_text.gif')
save_file_icon = PhotoImage(file=r'C:\Users\Ayush\Desktop\sample\icons\icons\find_text.gif')
#Here File Menu codes Begains
menu_bar = Menu(root) 

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0,
                      command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0,
                      command=open_file)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0,
                      command=save)
file_menu.add_command(label="Save As", accelerator='Ctrl+Shift+S', compound='left', underline=0, command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)
# End of File Menu

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left', image=undo_icon, underline=0, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, underline=0, command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, underline=0, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, underline=0, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, underline=0,
                      command=paste)
edit_menu.add_separator()

edit_menu.add_command(label="Exit",command=root.destroy)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
# End of Edit Menu


view_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_separator()
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor)
view_menu.add_separator()
view_menu.add_command(label="Exit",command=root.destroy)
themes_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)

# start of About Menu
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='Help', underline=0, command=display_help)
about_menu.add_separator()
about_menu.add_command(label="Exit",command=root.destroy)
root.config(menu=menu_bar)
#End of About Menu

# Adding top shortcut bar and left line number bar
shortcut_bar = Frame(root, height=25)
shortcut_bar.pack(expand='no', fill='x')

# Adding shortcut icons
icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(2, 2)
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, height=35, width=35, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')

line_number_bar = Text(root, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828', state='disabled',
                       wrap='none')
line_number_bar.pack(side='left', fill='y')

# adding the main context Text widget and Scrollbar Widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

# addind cursor info label
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')

# setting up the pop-up menu
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
content_text.bind('<Button-3>', show_popup_menu)

# Handling binding

content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)

content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-y>', redo)

content_text.bind('<KeyPress-F1>', display_help)

content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory2')

content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()

# END OF MENU

root.protocol('WM_DELETE_WINDOW', exit_editor)
#Root for main window
root.mainloop()