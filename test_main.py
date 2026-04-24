import unittest
from main import Agent


class TestAgent(unittest.TestCase):
    
    def test_agent_creation(self):
        agent = Agent("TestAgent", ["send", "receive"])
        self.assertEqual(agent.name, "TestAgent")
        self.assertEqual(agent.status, "online")
    
    def test_send_message(self):
        alice = Agent("Alice", ["send"])
        bob = Agent("Bob", ["receive"])
        result = alice.send_message(bob, "Hello")
        self.assertEqual(result["content"], "Hello")
        self.assertEqual(len(bob.message_history), 1)
    
    def test_get_status(self):
        agent = Agent("StatusBot", ["query"])
        status = agent.get_status()
        self.assertEqual(status["agent_name"], "StatusBot")
        self.assertIn("protocol_version", status)


if __name__ == "__main__":
    unittest.main()
