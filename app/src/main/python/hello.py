import asyncio
from kasa import SmartPlug

async def main():
    p = SmartPlug("127.0.0.1")

    await p.update()  # Request the update
    x = (p.alias)  # Print out the alias
    y = (p.emeter_realtime)  # Print out current emeter status

    await p.turn_off()  # Turn the device off

    return x+y

if __name__ == "__main__":
    asyncio.run(main())