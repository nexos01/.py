class Tk:
    def __init__(self):
        self.title_text = ""
        self.widgets = []

    def title(self, title):
        self.title_text = title

    def mainloop(self):
        print(f"Tkinter event loop started for window: {self.title_text}")

    def add_widget(self, widget):
        self.widgets.append(widget)

class Frame:
    def __init__(self, master=None):
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Frame packed")

class Label:
    def __init__(self, master=None, text=""):
        self.master = master
        self.text = text

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Label packed with text: {self.text}")

class Button:
    def __init__(self, master=None, text="", command=None):
        self.master = master
        self.text = text
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Button packed with text: {self.text}")

class Entry:
    def __init__(self, master=None):
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Entry packed")
        
        
        # Extension: Configurable Mixin Class
class Configurable:
    def __init__(self, **kwargs):
        self.config(**kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Base Module: Tkinter Classes
class Tk(Configurable):
    def __init__(self):
        super().__init__()
        self.title_text = ""
        self.widgets = []

    def title(self, title):
        self.title_text = title

    def mainloop(self):
        print(f"Tkinter event loop started for window: {self.title_text}")

    def add_widget(self, widget):
        self.widgets.append(widget)

class Frame(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Frame packed")

class Label(Configurable):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Label packed with text: {self.text}")

class Button(Configurable):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Button packed with text: {self.text}")

class Entry(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Entry packed")
        
        # Extension: Configurable Mixin Class
class Configurable:
    def __init__(self, **kwargs):
        self.config(**kwargs)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Base Module: Tkinter Classes
class Tk(Configurable):
    def __init__(self):
        super().__init__()
        self.title_text = ""
        self.widgets = []

    def title(self, title):
        self.title_text = title

    def mainloop(self):
        print(f"Tkinter event loop started for window: {self.title_text}")

    def add_widget(self, widget):
        self.widgets.append(widget)

class Frame(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Frame packed")

class Label(Configurable):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Label packed with text: {self.text}")

class Button(Configurable):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Button packed with text: {self.text}")

class Entry(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Entry packed")
        
        # Extension: Text Area
class TextArea(Configurable):
    def __init__(self, master=None, text="", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print(f"Text Area packed with text:\n{self.text}")

# Extension: Image Widget
class ImageWidget(Configurable):
    def __init__(self, master=None, image=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.image = image

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Image Widget packed")
        
        
        
        
        
        # Extension: Event Handling
class EventMixin:
    def bind(self, event, callback):
        # Placeholder for event binding
        pass
        
        # Extension: Menu
class Menu(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Menu packed")

class MenuItem(Configurable, EventMixin):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_item(self)
        print(f"Menu Item added: {self.text}")

    def click(self):
        if self.command:
            self.command()

# Add methods to Tk class for managing widgets and menu items
class Tk(Configurable):
    def __init__(self):
        super().__init__()
        self.title_text = ""
        self.widgets = []
        self.menus = []

    def title(self, title):
        self.title_text = title

    def mainloop(self):
        print(f"Tkinter event loop started for window: {self.title_text}")

    def add_widget(self, widget):
        self.widgets.append(widget)

    def add_item(self, item):
        self.menus.append(item)
        
        
        # Extension: Frame with Scrollbar
class ScrollableFrame(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = None
        self.scrollbar = None

    def pack(self, **kwargs):
        super().pack(**kwargs)
        self.canvas = Canvas(self, **kwargs)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.inner_frame = Frame(self.canvas, **kwargs)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        def on_mouse_wheel(event):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

        self.canvas.bind_all("<MouseWheel>", on_mouse_wheel)


# Extension: Tabbed Frame
class TabbedFrame(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.notebook = None

    def pack(self, **kwargs):
        super().pack(**kwargs)
        self.notebook = Notebook(self, **kwargs)
        self.notebook.pack(fill="both", expand=True)

    def add_tab(self, title, content):
        self.notebook.add(content, text=title)
        
        


# Extension: Treeview
class Treeview(Configurable):
    def __init__(self, master=None, columns=(), **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.columns = columns
        self.data = []

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Treeview packed")

    def add_item(self, item):
        self.data.append(item)

    def clear(self):
        self.data = []

    def show(self):
        for item in self.data:
            print(item)

    def set_columns(self, columns):
        self.columns = columns
        
        
        
        # Extension: Progress Bar
class ProgressBar(Configurable):
    def __init__(self, master=None, value=0, maximum=100, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.value = value
        self.maximum = maximum

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Progress Bar packed")

    def set_value(self, value):
        self.value = value
        print(f"Progress Bar value set to: {self.value}")

    def set_maximum(self, maximum):
        self.maximum = maximum
        print(f"Progress Bar maximum set to: {self.maximum}")

# Extension: Listbox
class Listbox(Configurable):
    def __init__(self, master=None, items=(), **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.items = list(items)

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Listbox packed")

    def add_item(self, item):
        self.items.append(item)

    def clear(self):
        self.items.clear()

    def show(self):
        for item in self.items:
            print(item)
            
            


# Extension: Image Button
class ImageButton(Configurable):
    def __init__(self, master=None, image=None, command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.image = image
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Image Button packed")

    def click(self):
        if self.command:
            self.command()
            
            
            # Extension: Check Button
class CheckButton(Configurable):
    def __init__(self, master=None, text="", variable=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.variable = variable

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Check Button packed")

    def click(self):
        if self.variable:
            self.variable.set(not self.variable.get())


# Extension: Radio Button
class RadioButton(Configurable):
    def __init__(self, master=None, text="", variable=None, value=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.variable = variable
        self.value = value

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Radio Button packed")

    def click(self):
        if self.variable and self.value is not None:
            self.variable.set(self.value)
            
     
                   
            
            
            
            # Extension: Spinbox
class Spinbox(Configurable):
    def __init__(self, master=None, from_=0, to=10, increment=1, variable=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.from_ = from_
        self.to = to
        self.increment = increment
        self.variable = variable

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Spinbox packed")

    def set_value(self, value):
        if self.variable:
            self.variable.set(value)
            
            
            # Extension: Text Entry Field
class EntryField(Configurable):
    def __init__(self, master=None, text="", variable=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.text = text
        self.variable = variable

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Entry Field packed")

    def get_value(self):
        if self.variable:
            return self.variable.get()
        else:
            return self.text

    def set_value(self, value):
        if self.variable:
            self.variable.set(value)
            
            # Extension: Canvas
class Canvas(Configurable):
    def __init__(self, master=None, width=200, height=200, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.width = width
        self.height = height

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Canvas packed")

    def draw_rectangle(self, x0, y0, x1, y1, **kwargs):
        print(f"Rectangle drawn at ({x0}, {y0}) to ({x1}, {y1})")

    def draw_circle(self, x, y, radius, **kwargs):
        print(f"Circle drawn at ({x}, {y}) with radius {radius}")

    def draw_line(self, x0, y0, x1, y1, **kwargs):
        print(f"Line drawn from ({x0}, {y0}) to ({x1}, {y1})")

# Extension: Menu
class Menu(Configurable):
    def __init__(self, master=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.items = []

    def add_command(self, label, command):
        self.items.append(("command", label, command))

    def add_separator(self):
        self.items.append(("separator",))

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Menu packed")

    def show(self):
        for item in self.items:
            if item[0] == "command":
                print(f"Menu item: {item[1]}")
            elif item[0] == "separator":
                print("Menu separator")

# Extension: MenuItem
class MenuItem(Configurable):
    def __init__(self, master=None, label="", command=None, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.label = label
        self.command = command

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Menu Item packed")
        
        
        
            
            # Extension: Scrollbar
class Scrollbar(Configurable):
    def __init__(self, master=None, orientation="vertical", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.orientation = orientation

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Scrollbar packed")

    def scroll(self, amount):
        print(f"Scrollbar scrolled by {amount}")
        
        # Extension: Scrollbar
class Scrollbar(Configurable):
    def __init__(self, master=None, orientation="vertical", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.orientation = orientation

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Scrollbar packed")

    def scroll(self, amount):
        print(f"Scrollbar scrolled by {amount}")
        
        # Extension: DialogBox
class DialogBox(Configurable):
    def __init__(self, master=None, title="", message="", buttons=[], **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.title = title
        self.message = message
        self.buttons = buttons

    def pack(self, **kwargs):
        if self.master:
            self.master.add_widget(self)
        print("Dialog Box packed")

    def show(self):
        print(f"Dialog Box: {self.title}")
        print(f"Message: {self.message}")
        print("Buttons:")
        for button in self.buttons:
            print(f"- {button}")
            
            
        # Extension: Tooltip
class Tooltip(Configurable):
    def __init__(self, master=None, widget=None, text="", **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.widget = widget
        self.text = text

    def bind_tooltip(self):
        if self.widget:
            self.widget.bind("<Enter>", self.show_tooltip)
            self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        print(f"Tooltip: {self.text}")

    def hide_tooltip(self, event):
        print("Tooltip hidden")
        
        # Define default styling options for each widget type
DEFAULT_STYLES = {
    'button': {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)},
    'label': {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)},
    'frame': {'bg': 'white'}
}

# Define the Tk class
class Tk:
    def __init__(self):
        pass

    def title(self, title):
        print(f"Window title set to: {title}")

    def mainloop(self):
        print("Tkinter event loop started")

# Define the Frame class
class Frame:
    def __init__(self, master=None, **kwargs):
        self.master = master
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_frame(self)
        print("Frame packed")

# Define the Label class
class Label:
    def __init__(self, master=None, text="", **kwargs):
        self.master = master
        self.text = text
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_label(self)
        print(f"Label packed with text: {self.text}")

# Define the Button class
class Button:
    def __init__(self, master=None, text="", command=None, **kwargs):
        self.master = master
        self.text = text
        self.command = command
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_button(self)
        print(f"Button packed with text: {self.text}")


# Define the Tk class
class Tk:
    def __init__(self):
        pass

    def title(self, title):
        print(f"Window title set to: {title}")

    def mainloop(self):
        print("Tkinter event loop started")

# Define the Frame class
class Frame:
    def __init__(self, master=None, **kwargs):
        self.master = master
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_frame(self)
        print("Frame packed with kwargs:", self.kwargs)

# Define the Label class
class Label:
    def __init__(self, master=None, text="", **kwargs):
        self.master = master
        self.text = text
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_label(self)
        print(f"Label packed with text: {self.text}, kwargs: {self.kwargs}")

# Define the Button class
class Button:
    def __init__(self, master=None, text="", command=None, **kwargs):
        self.master = master
        self.text = text
        self.command = command
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_button(self)
        print(f"Button packed with text: {self.text}, kwargs: {self.kwargs}")

# Define default styling options for each widget type
DEFAULT_STYLES = {
    'button': {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)},
    'label': {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)},
    'frame': {'bg': 'white'}
}

# Define a function to apply styling options to widgets
def apply_style(widget, widget_type, **kwargs):
    style = DEFAULT_STYLES[widget_type].copy()
    style.update(kwargs)
    widget.kwargs.update(style)

# Update the pack method in each widget class to apply styling options
def add_frame(self, frame):
    apply_style(frame, 'frame', **frame.kwargs)

def add_label(self, label):
    apply_style(label, 'label', **label.kwargs)

def add_button(self, button):
    apply_style(button, 'button', **button.kwargs)

# Update the Tk class to include methods for adding widgets
Tk.add_frame = add_frame
Tk.add_label = add_label
Tk.add_button = add_button


# Define the Button class
class Button:
    def __init__(self, master=None, text="", command=None, **kwargs):
        self.master = master
        self.text = text
        self.command = command
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_button(self)
        print(f"Button packed with text: {self.text}, kwargs: {self.kwargs}")

    # Extension: Method to bind a command to the button click event
    def bind_click(self, command):
        self.command = command

    # Extension: Method to handle button click events
    def handle_click(self):
        if self.command:
            self.command()

# Usage example:
# Define a function to be executed when the button is clicked
def button_click():
    print("Button clicked!")

# Create a Tk instance
root = Tk()

# Create a Button instance
button = Button(root, text="Click me")

# Bind the button click event to the button_click function
button.bind_click(button_click)

# Pack the button
button.pack()


# Define the Label class
class Label:
    def __init__(self, master=None, text="", **kwargs):
        self.master = master
        self.text = text
        self.kwargs = kwargs

    def pack(self, **kwargs):
        if self.master:
            self.master.add_label(self)
        print(f"Label packed with text: {self.text}, kwargs: {self.kwargs}")

    # Extension: Method to bind a command to the label click event
    def bind_click(self, command):
        self.command = command

    # Extension: Method to handle label click events
    def handle_click(self):
        if self.command:
            self.command()

# Usage example:
# Define a function to be executed when the label is clicked
def label_click():
    print("Label clicked!")

# Create a Tk instance
root = Tk()

# Create a Label instance
label = Label(root, text="Click me")

# Bind the label click event to the label_click function
label.bind_click(label_click)

# Pack the label
label.pack()

# Define the Entry class (with the bind_key and handle_key methods)
class Entry:
    def __init__(self, master=None):
        self.master = master
        self.key_bindings = {}

    # Extension: Method to bind a command to the entry field's key press event
    def bind_key(self, key, command):
        if key in self.key_bindings:
            self.key_bindings[key].append(command)
        else:
            self.key_bindings[key] = [command]

    # Extension: Method to handle entry field key press events
    def handle_key(self, key):
        if key in self.key_bindings:
            for command in self.key_bindings[key]:
               command()
                
                
# Define the Tk class
class Tk:
    def __init__(self):
        pass

    def title(self, title):
        print(f"Window title set to: {title}")

    def mainloop(self):
        print("Tkinter event loop started")

# Define the Entry class (with the bind_key and handle_key methods)
class Entry:
    def __init__(self, master=None):
        self.master = master
        self.key_bindings = {}

    # Extension: Method to bind a command to the entry field's key press event
    def bind_key(self, key, command):
        if key in self.key_bindings:
            self.key_bindings[key].append(command)
        else:
            self.key_bindings[key] = [command]

    # Extension: Method to handle entry field key press events
    def handle_key(self, key):
        if key in self.key_bindings:
            for command in self.key_bindings[key]:
                command()

# Usage example:
# Define a function to be executed when a key is pressed in the entry field
def key_press():
    print("Key pressed!")

# Create a Tk instance
root = Tk()

# Create an Entry instance
entry = Entry()

# Bind the key press event to the key_press function
entry.bind_key("<KeyPress>", key_press)

# Simulate a key press event (for demonstration purposes)
entry.handle_key("<KeyPress>")

# Output:
# Key pressed!


# Define the Frame class
class Frame:
    def __init__(self, master=None):
        self.master = master

    def pack(self, **kwargs):
        if self.master:
            self.master.add_frame(self)
        print("Frame packed")

# Define the Entry class
class Entry:
    def __init__(self, master=None):
        self.master = master
        self.key_bindings = {}

    # Extension: Method to bind a command to the entry field's key press event
    def bind_key(self, key, command):
        if key in self.key_bindings:
            self.key_bindings[key].append(command)
        else:
            self.key_bindings[key] = [command]

    # Extension: Method to handle entry field key press events
    def handle_key(self, key):
        if key in self.key_bindings:
            for command in self.key_bindings[key]:
                command()

    def pack(self, **kwargs):
        if self.master:
            self.master.add_entry(self)
        print("Entry packed")
        

