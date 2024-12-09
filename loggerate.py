class Logger:
    def __init__(self):
        # Initialize a hashmap to store message -> timestamp
        self.message_timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If the message is not in the hashmap or it's been 10 seconds or more
        if message not in self.message_timestamps or timestamp >= self.message_timestamps[message] + 10:
            # Update the hashmap with the new timestamp
            self.message_timestamps[message] = timestamp
            return True
        else:
            return False


