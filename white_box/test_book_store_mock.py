import unittest
from unittest.mock import patch, MagicMock
from white_box.book_store import BookStore, Book

class TestBookStoreMock(unittest.TestCase):

    
    
    def setUp(self):
        self.store = BookStore()
    
    @patch('white_box.book_store.Book')
    def test_add_book_with_mock(self, MockBook):
        mock_book = MagicMock()
        mock_book.isbn = '123'
        MockBook.return_value = mock_book
        
        self.store.add_book(mock_book)
        
        self.assertEqual(len(self.store.books), 1)
        self.assertIn('123', self.store.books)
    
    def test_remove_book(self):
        book = Book('Test', 'Author', '123', 10.0)
        self.store.add_book(book)
        
        result = self.store.remove_book('123')
        
        self.assertTrue(result)
        self.assertEqual(len(self.store.books), 0)
    
    def test_remove_nonexistent_book(self):
        result = self.store.remove_book('999')
        
        self.assertFalse(result)
    
    @patch('white_box.book_store.BookStore.find_book')
    def test_search_book_mock(self, mock_find):
        mock_book = MagicMock()
        mock_find.return_value = mock_book
        
        result = self.store.find_book('123')
        
        mock_find.assert_called_once_with('123')
        self.assertEqual(result, mock_book)
    
    def test_update_stock(self):
        book = Book('Test', 'Author', '123', 10.0, 5)
        self.store.add_book(book)
        
        result = self.store.update_stock('123', 10)
        
        self.assertTrue(result)
        self.assertEqual(book.stock, 15)
    
    def test_update_stock_nonexistent(self):
        result = self.store.update_stock('999', 10)
        
        self.assertFalse(result)
    
    @patch('builtins.print')
    def test_list_books_with_mock(self, mock_print):
        book1 = Book('Book1', 'Author1', '123', 10.0)
        book2 = Book('Book2', 'Author2', '456', 15.0)
        self.store.add_book(book1)
        self.store.add_book(book2)
        
        self.store.list_books()
        
        self.assertEqual(mock_print.call_count, 2)

if __name__ == '__main__':
    unittest.main()