import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import requests
from io import BytesIO
from scrapping import start

def suggest_mobile():
    price_min = int(price_min_entry.get())
    price_max = int(price_max_entry.get())
    priority_1 = priority_var_1.get()
    priority_2 = priority_var_2.get()
    priority_3 = priority_var_3.get()
    a = start(price_min, price_max, priority_1, priority_2, priority_3)
    # Placeholder data for demonstration
   
    suggestions = a[0]
    specifications = a[1]
    image_urls = a[2]
    buy_links = a[3]

# Clear the existing suggestions in the listbox
    suggestion_listbox.delete(0, tk.END)

# Display each suggestion and its corresponding image
    for i in range(len(suggestions)):
        suggestion = suggestions[i]
        specification = specifications[i]
        image_url = image_urls[i]
        buy_link = buy_links[i]

        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)


        suggestion_listbox.insert(tk.END, suggestion)
        suggestion_listbox.image_list.append(photo)
        suggestion_listbox.specification_list.append(specification)
        suggestion_listbox.buy_links.append(buy_link)


def on_suggestion_select(event):
    index = suggestion_listbox.curselection()[0]
    photo = suggestion_listbox.image_list[index]
    specification = suggestion_listbox.specification_list[index]
    buy_link = suggestion_listbox.buy_links[index]

    suggestion_listbox.selection_clear(0, tk.END)
    suggestion_listbox.selection_set(index)
    specification_label.config(text=specification)
    image_label.config(image=photo)
    image_label.image = photo

    # Update the buy link button
    buy_button.config(command=lambda: webbrowser.open_new_tab(buy_link))
    buy_button.config(state=tk.NORMAL)


# Create the main window
window = tk.Tk()
window.title("Mobile Suggest System")

# Set window dimensions and position
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="white")

price_label = tk.Label(window, text="Price Range:",
                       bg="white", font=("Arial", 12))
price_label.place(x=50, y=50)

price_min_label = tk.Label(window, text="Min:", bg="white", font=("Arial", 12))
price_min_label.place(x=200, y=50)
price_min_entry = tk.Entry(window, bg="white", font=("Arial", 12))
price_min_entry.place(x=250, y=50)

price_max_label = tk.Label(window, text="Max:", bg="white", font=("Arial", 12))
price_max_label.place(x=400, y=50)
price_max_entry = tk.Entry(window, bg="white", font=("Arial", 12))
price_max_entry.place(x=450, y=50)


# Create the priorities labels and dropdown menus
priority_label_1 = tk.Label(
    window, text="First Priority:", bg="white", font=("Arial", 12))
priority_label_1.place(x=50, y=100)

priority_var_1 = tk.StringVar()
priority_var_1.set("Performance")  # Set a default value

priority_menu_1 = tk.OptionMenu(
    window, priority_var_1, "Performance", "Camera", "Battery")
priority_menu_1.config(bg="white", font=("Arial", 12))
priority_menu_1.place(x=200, y=100)

priority_label_2 = tk.Label(
    window, text="Second Priority:", bg="white", font=("Arial", 12))
priority_label_2.place(x=50, y=150)

priority_var_2 = tk.StringVar()
priority_var_2.set("Camera")  # Set a default value

priority_menu_2 = tk.OptionMenu(
    window, priority_var_2, "Performance", "Camera", "Battery")
priority_menu_2.config(bg="white", font=("Arial", 12))
priority_menu_2.place(x=200, y=150)

priority_label_3 = tk.Label(
    window, text="Third Priority:", bg="white", font=("Arial", 12))
priority_label_3.place(x=50, y=200)

priority_var_3 = tk.StringVar()
priority_var_3.set("Battery")  # Set a default value

priority_menu_3 = tk.OptionMenu(
    window, priority_var_3, "Performance", "Camera", "Battery")
priority_menu_3.config(bg="white", font=("Arial", 12))
priority_menu_3.place(x=200, y=200)


# Create the suggest button
suggest_button = tk.Button(window, text="Suggest", command=suggest_mobile,
                           bg="lightblue", font=("Arial", 12))
suggest_button.place(x=50, y=250)

# Create the suggestion listbox
suggestion_listbox = tk.Listbox(window, width=30, height=10)
suggestion_listbox.place(x=50, y=300)
suggestion_listbox.bind("<<ListboxSelect>>", on_suggestion_select)
suggestion_listbox.image_list = []
suggestion_listbox.specification_list = []
suggestion_listbox.buy_links = []

# Create the suggestion details section
image_label = tk.Label(window, width=200, height=200, bg="white")
image_label.place(x=400, y=300)
specification_label = tk.Label(
    window, width=30, height=5, wraplength=300, bg="white")
specification_label.place(x=600, y=300)

# Create the Buy Now button
buy_button = tk.Button(window, text="Buy Now", state=tk.DISABLED, bg="green", fg="white",
                       font=("Arial", 12))
buy_button.place(x=400, y=550)

# Start the main event loop
window.mainloop()