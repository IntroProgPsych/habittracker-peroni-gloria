# 1. IMPORT MODULES
import unittest
# This imports your logic from the main file 
# (Make sure your main file is named habit_tracker.py)
from habit_tracker import interpret_score

# 2. DEFINE TESTS
class TestHabitTracker(unittest.TestCase):

    def test_interpret_high(self):
        """Test that scores 12 and above return High."""
        self.assertEqual(interpret_score(12), "High")
        self.assertEqual(interpret_score(21), "High")

    def test_interpret_moderate(self):
        """Test that scores between 6 and 11 return Moderate."""
        self.assertEqual(interpret_score(6), "Moderate")
        self.assertEqual(interpret_score(9), "Moderate")
        self.assertEqual(interpret_score(11), "Moderate")

    def test_interpret_low(self):
        """Test that scores below 6 return Low."""
        self.assertEqual(interpret_score(5), "Low")
        self.assertEqual(interpret_score(0), "Low")

# 3. TEST SUITE
def main():
    print("Starting tests suite...")
    
    # This part creates the suite and runs the tests you wrote above
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHabitTracker)
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

# 4. RUNNER (Do not change these lines)
if __name__ == "__main__":
    main()