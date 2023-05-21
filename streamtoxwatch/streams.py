import asyncio

class Stream:
    """ class contains an asyncio Queue to hold the Event objects. \
    The process_events method is an async method that runs in an infinite loop,\ 
    continuously processing events by calling the handle_event method for each event. \
    The enqueue_event method is used to add events to the queue. """
    def __init__(self):
        self.queue = asyncio.Queue()

    async def process_events(self):
        while True:
            event = await self.queue.get()
            await self.handle_event(event)

    async def handle_event(self, event):
        # Process the event logic here
        print("Processing event:", event)

    def enqueue_event(self, event):
        self.queue.put_nowait(event)


class Event:
    """ The Event class represents an event object and can be customized \
    based on your specific needs. In this example, it has a data attribute\
    and a __repr__ method to provide a string representation of the event. """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Event(data={self.data})"


async def main():
    """ Example for basic handling. """
    stream = Stream()
    event1 = Event("Event 1")
    event2 = Event("Event 2")
    event3 = Event("Event 3")

    stream.enqueue_event(event1)
    stream.enqueue_event(event2)
    stream.enqueue_event(event3)

    asyncio.create_task(stream.process_events())

    await asyncio.sleep(1)  # Wait for events to be processed

if __name__ == "__main__":
    asyncio.run(main())
