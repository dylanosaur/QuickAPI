import aiohttp
import asyncio
import time


def run_google(n):
    start = time.time()

    async def main(n):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://google.com/search?q=json") as response:
                for i in range(n):
                    html = await response.text()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(n))

    stop = time.time()
    print(f'{n} reqs / {stop - start} s = {round(n / (stop - start), 2)} reqs/second')
    return round(n / (stop - start), 2)

# run_google(1000000)
