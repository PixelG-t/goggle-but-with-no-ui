import time
import webbrowser as wb

website = input("Please enter website URL: ")

if website.lower() == "rickroll":
    wb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

print("One sec...")
time.sleep(1.5)
wb.open(website)
