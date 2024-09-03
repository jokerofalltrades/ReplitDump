using System;
using System.Collections.Generic;

public class NotesManager
{
    private List<string> notes;

    public NotesManager()
    {
        notes = new List<string>();
    }

    public void AddNote(string note)
    {
        notes.Add(note);
    }

    public void PrintNotes()
    {
        if (notes.Count > 0)
        {
            for (int i = 0; i < notes.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {notes[i]}");
            }
        }
        else
        {
            Console.WriteLine("There are no notes to print!");
        }
    }

    public void RemoveAndEditNote(string index, string newNote, int action)
    {
        int noteIndex;
        bool isValidIndex = int.TryParse(index, out noteIndex) && noteIndex > 0 && noteIndex <= notes.Count;

        if (isValidIndex)
        {
            if (action == 1)
            {
                notes[noteIndex - 1] = newNote;
            }
            else
            {
                notes.RemoveAt(noteIndex - 1);
            }
        }
        else
        {
            Console.WriteLine("That is not a valid index, please enter the number of a note contained within the list.");
        }
    }

    public void ClearNotes()
    {
        notes.Clear();
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        NotesManager notes = new NotesManager();

        while (true)
        {
            Console.Clear();
            Console.WriteLine("Hello and Welcome to your Notes Manager!\nHere are the following actions you can peform:\n'add' - add a note\n'remove' - remove a note\n'print' - print your notes\n'edit' - edit a note\n'clear' - clears all notes\n'exit' - exit the program");
            string action = Console.ReadLine();
            Console.Clear();
            switch (action.ToLower())
            {
                case "add":
                    Console.WriteLine("What note would you like to add?");
                    string note = Console.ReadLine();
                    notes.AddNote(note);
                    break;
                case "remove":
                    notes.PrintNotes();
                    Console.WriteLine("What number note would you like to remove?");
                    string indexToRemove = Console.ReadLine();
                    notes.RemoveAndEditNote(indexToRemove, "", 0);
                    break;
                case "print":
                    notes.PrintNotes();
                    break;
                case "edit":
                    notes.PrintNotes();
                    Console.WriteLine("What number note would you like to edit?");
                    string indexToEdit = Console.ReadLine();
                    Console.WriteLine("What would you like the new note to be?");
                    string newNote = Console.ReadLine();
                    notes.RemoveAndEditNote(indexToEdit, newNote, 1);
                    break;
                case "clear":
                    notes.ClearNotes();
                    break;
                case "exit":
                    return;
                default:
                    Console.WriteLine("That is not an action.");
                    break;
            }
        }
    }
}
