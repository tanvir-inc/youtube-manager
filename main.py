import json

def loadData():
  try:
    with open('youtube.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def saveData(videos):
  with open('youtube.txt', 'w') as file:
    json.dump(videos, file)

def addVideo(videos):
  print("\n=============== Add Videos ===============\n")
  name = input("\nEnter Video Title: ")
  time = input("Enter Video Duration: ")
  videos.append({'Title': name, 'Duration': time})
  saveData(videos)
  print("\nVideo added successfully!")

def delVideo(videos):
  listVideo(videos)
  print("\n=============== Delete Videos ===============\n")
  index = int(input("\nEnter video number: "))
  if 1 <= index <= len(videos):
    del videos[index-1]
    saveData(videos)
    print("\nVideo Deleted Successfully.")
  else:
    print("\nInvalid Index Selected.")

def updateVideo(videos):
  listVideo(videos)
  print("\n=============== Update Videos ===============\n")
  index = int(input("\nEnter Video Number: "))
  if 1 <= index <= len(videos):
    name = input("Update Title: ")
    time = input("Update Duration: ")
    videos[index-1] = {'Title': name, 'Duration': time}
    saveData(videos)
    print("Video updated successfully!")
  else:
    print("\nInvalid Index Selected.")

def listVideo(videos):
  print("\n=============== List Of All Videos ===============\n")
  for index, video in enumerate(videos, start=1):
    print(f"{index}. {video['Title']}, {video['Duration']}")
 
def main():
  videos = loadData()
  while True:
    print("\n=============== Welcome to Youtube Manager ===============\n")
    print("1. Add Video")
    print("2. Update Video")
    print("3. Delete Video")
    print("4. Show Video List")
    print("5. Exit\n")
    choice = input("Enter your choice: ")
    match choice:
      case '1':
        addVideo(videos)
      case '2':
        updateVideo(videos)
      case '3':
        delVideo(videos)
      case '4':
        listVideo(videos)
      case '5':
        break
      case _:
        print("Invalid Choice!")

if __name__ == '__main__':
  main()
