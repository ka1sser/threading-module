import requests
import time
import concurrent.futures

img_urls = [
    "https://images.unsplash.com/photo-1589656966895-2f33e7653819",
    "https://images.unsplash.com/photo-1564349683136-77e08dba1ef7",
    "https://images.unsplash.com/photo-1456926631375-92c8ce872def",
    "https://images.unsplash.com/photo-1474511320723-9a56873867b5",
    "https://images.unsplash.com/photo-1437622368342-7a3d73a34c8f",
    "https://images.unsplash.com/photo-1504006833117-8886a355efbf",
    "https://images.unsplash.com/photo-1493916665398-143bdeabe500",
    "https://images.unsplash.com/photo-1444464666168-49d633b86797",
    "https://images.unsplash.com/photo-1500349812227-3264f5f54181",
    "https://images.unsplash.com/photo-1551946581-f7a62cd2f00b",
]

start = time.perf_counter()

# # Without using threads
# for img_url in img_urls:
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split("/")[3]
#     img_name = f"{img_name}.jpg"

#     with open(img_name, "wb") as img_file:
#         img_file.write(img_bytes)
#         print(f"{img_name} was downloaded...")


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded...")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

finish = time.perf_counter()

print(f"Finished in {finish-start} second(s)...")
