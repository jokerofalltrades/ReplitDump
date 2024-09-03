from os import system


class NotesManager:

  def __init__(self):
    self.notes = []

  def add_note(self, note):
    self.notes.append(note)

  def print_notes(self):
    if len(self.notes) > 0:
      for i in range(len(self.notes)):
        print(str(i+1)+". "+str(self.notes[i]))
    else:
      print("There are no notes to print!")

  def remove_and_edit_note(self,index,NewNote,action):
    #action - '0' for remove note '1' for edit note
    if index.isdigit() and 0 < int(index) <= len(self.notes):
      if int(action) == 1:
        self.notes[int(index)-1] = NewNote
      else:
        del self.notes[int(index)-1]
    else:
      print("That is not a valid index.")

  def clear_notes(self):
    self.notes.clear()


def clear():
  _ = system('clear')


#Initialises Notes
Notes = NotesManager()

#Running Loop
while True:
  action = input("""Hello and Welcome to your Notes Manager!
Here are the following actions you can peform:
'add' - add a note
'remove' - remove a note
'print' - print your notes
'edit' - edit a note
'clear' - clears all notes
'exit' - exit the program
""")
  clear()
  if action.lower() == "add":
    note = input("What note would you like to add?")
    Notes.add_note(note)
  elif action.lower() == "remove":
    Notes.print_notes()
    index = input("What number note would you like to remove?")
    Notes.remove_and_edit_note(index,"",0)
  elif action.lower() == "print":
    Notes.print_notes()
  elif action.lower() == "edit":
    Notes.print_notes()
    index = input("What number note would you like to edit?")
    newNote = input("What would you like the new note to be?")
    Notes.remove_and_edit_note(index,newNote,1)
  elif action.lower() == "clear":
    Notes.clear_notes()
  elif action.lower() == "exit":
    break
  else:
    print("That is not an action.")
