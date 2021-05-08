import aiohttp
import asyncio
import time
import os


async def _run_json(url, n):
    async def main():
        async def fetch_json():
            async with aiohttp.ClientSession() as session:
                async with session.get(f"http://{url}") as response:
                    text = await response.text()
                    # print(text)
        for i in range(n):
            await fetch_json()
    await main()


def run_json(url, n):
    start = time.time()
    asyncio.run(_run_json(url, n))
    stop = time.time()
    print(f'{n} reqs / {stop - start} s = {round(n / (stop - start), 2)} reqs/second')
    output = round(n / (stop - start), 2)
    return str(output)


if __name__ == '__main__':
    output = run_json(os.environ['container_url'], 100)