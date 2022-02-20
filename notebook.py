"""
lab 3 task 6 module
"""
import datetime

notes_id = 0

class Note:
    """
    class for modeling note
    """
    def __init__(self, memo, tags) -> None:
        """
        initializes object
        >>> my_note = Note("hello", ["first_note"])
        >>> print(my_note.memo)
        hello
        """
        global notes_id
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        self.note_id = notes_id
        notes_id += 1
    
    def match(self, search_filter):
        """
        checks whether a sertain text appears in note text
        >>> my_note = Note("hello", ["first_note"])
        >>> print(my_note.match('he'))
        True
        """
        if search_filter in self.memo:
            return True
        return False

class Notebook:
    """
    class for modeling notebook
    """
    def __init__(self) -> None:
        """
        initializes object
        """
        self.notes = []
    
    def search(self, text):
        """
        searches for notes with particular text
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note("hello", ["first_note"])
        >>> print(my_notebook.search('e')[0].memo)
        hello
        """
        ret_lst = []
        for note in self.notes:
            if text in note.memo:
                ret_lst.append(note)
        return ret_lst
    
    def new_note(self, memo, tags):
        """
        creates new note
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note("hello", ["first_note"])
        >>> print(my_notebook.notes[0].memo)
        hello
        """
        self.notes.append(Note(memo, tags))
    
    def modify_memo(self, note_id, memo):
        """
        changes note text
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note("hello", ["first_note"])
        >>> my_notebook.modify_memo(my_notebook.notes[0].note_id, "world")
        >>> print(my_notebook.notes[0].memo)
        world
        """
        for ind in range(len(self.notes)):
            if self.notes[ind].note_id == note_id:
                self.notes[ind].memo = memo
    
    def modify_tags(self, note_id, tags):
        """
        changes note tags
        >>> my_notebook = Notebook()
        >>> my_notebook.new_note("hello", ["first_note"])
        >>> my_notebook.modify_tags(my_notebook.notes[0].note_id, ['modified'])
        >>> print(my_notebook.notes[0].tags)
        ['modified']
        """
        for ind in range(len(self.notes)):
            if self.notes[ind].note_id == note_id:
                self.notes[ind].tags = tags

class Menu:
    """
    I don't get the idea of this class
    as we haven't yet studied how to create graphical interphase
    """
    pass

class CommandOption:
    """
    I don't get the idea of this class
    as we haven't yet studied how to create graphical interphase
    in this case i don't even get the idea itself
    """
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
