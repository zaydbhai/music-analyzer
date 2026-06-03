import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import csv
from tinytag import TinyTag

class MusicAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Analyzer Pro")
        self.root.geometry("400x250")
        
        tk.Label(root, text="Music Library Metadata Scanner", font=("Helvetica", 12, "bold")).pack(pady=20)
        
        self.btn = ttk.Button(root, text="Scan Folder & Generate CSV", command=self.scan_folder)
        self.btn.pack(pady=20)

    def scan_folder(self):
        folder = filedialog.askdirectory()
        if not folder: return
        
        output_file = "Music_Library_By_Playlist.csv"
        
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # Added 'Playlist' column (which is the parent folder name)
                writer.writerow(['Title', 'Artist', 'Album', 'Year', 'Playlist', 'Path'])
                
                for root, _, files in os.walk(folder):
                    for file in files:
                        # STRICT FILTER: Only .mp3
                        if file.lower().endswith('.mp3'):
                            path = os.path.join(root, file)
                            # Get folder name to use as "Playlist"
                            playlist_name = os.path.basename(root)
                            
                            try:
                                tag = TinyTag.get(path)
                                # Only write if there's actual metadata
                                if tag.title or tag.artist:
                                    writer.writerow([tag.title, tag.artist, tag.album, tag.year, 
                                                     playlist_name, path])
                            except:
                                continue 
            
            messagebox.showinfo("Success", "Scan complete! File saved: " + output_file)
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicAnalyzer(root)
    root.mainloop()
