import asyncio


async def function_1():
    await asyncio.sleep(1)
    print("I am function 1")
    return 1


async def function_2():
    await asyncio.sleep(2)
    print("I am function 2")
    return 2


async def function_3():
    await asyncio.sleep(3)
    print("I am function 3")
    return 3


async def main():
    task = await asyncio.gather(function_1(), function_2(), function_3())
    print(task)

asyncio.run(main())
