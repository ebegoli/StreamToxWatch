import asyncio

class Stream:
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
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Event(data={self.data})"


async def main():
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
