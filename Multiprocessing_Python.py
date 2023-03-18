import multiprocessing
import requests


def downloadFile(URL, name):
    print(f"Started Downloading File {name}")
    response = requests.get(URL)
    file_descriptor = open(f"Images/Image_{name}.jpg", "wb")
    file_descriptor.write(response.content)
    file_descriptor.close()
    print(f"Finished Downloading File {name}")


if __name__ == "__main__":
    URL = "https://picsum.photos/2000/3000"

    processes = []
    for i in range(50):
        process = multiprocessing.Process(
            target=downloadFile, args=[URL, i + 1])
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
