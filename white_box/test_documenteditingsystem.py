import unittest
from class_exercises import DocumentEditingSystem   

class TestDocumentEditingSystem(unittest.TestCase): 
    def setUp(self):
        self.MyDocument  = DocumentEditingSystem()

    def test___init__(self):
        self.assertEqual(self.MyDocument.state, "Editing")

    def test_save_document_stateediting(self):
        self.MyDocument.state = "Editing"
        self.assertEqual(self.MyDocument.save_document(), "Document saved successfully")
        self.assertEqual(self.MyDocument.state, "Saved")

    def test_save_document_statenotediting(self):
        self.MyDocument.state = "Saved"
        self.assertEqual(self.MyDocument.save_document(), "Invalid operation in current state")
        self.assertEqual(self.MyDocument.state, "Saved")


    def test_edit_documentstatesaved(self):
        self.MyDocument.state = "Saved"
        self.assertEqual(self.MyDocument.edit_document(),  "Editing resumed")
        self.assertEqual(self.MyDocument.state, "Editing")

    def test_edit_documentstatenotsaved(self):
        self.MyDocument.state = "editing"
        self.assertEqual(self.MyDocument.edit_document(),  "Invalid operation in current state")
        self.assertFalse(self.MyDocument.state, "Editing")