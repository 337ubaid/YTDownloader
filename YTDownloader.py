import tkinter as tk
from pytube import YouTube

#windows configuration
windows = tk.Tk()
windows.geometry('500x200')
windows.title('Youtube Downloader')

heading = tk.Label(windows, text='Youtube Downloader', font=('arial', 20, 'bold'))
heading.pack()

#link
link = tk.StringVar()
text_link = tk.Label(windows, text='Link :')
entry_link = tk.Entry(textvariable=link, width=50)
text_link.pack()
entry_link.pack()

#path
# path = tk.StringVar()
# text_path = tk.Label(windows, text='Path :')
# entry_path = tk.Entry(textvariable=path, width=50)
# text_path.pack()    
# entry_path.pack()

#download function
def download():
    yt = YouTube(link.get())
    yd = yt.streams.get_highest_resolution()
    yd.download('D:/Downloads/Videos')

#button download
button_download = tk.Button(windows,
                            text='Download', 
                            command=download)
button_download.pack()

windows.mainloop()