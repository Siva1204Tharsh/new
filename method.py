import requests

url = "https://huggingface.co/Ajanthan06/Email-Phishinh-faite/blob/main/pytorch_model.bin"
response = requests.get(url)

with open("downloaded_model.pkl", "wb") as f:
    f.write(response.content)

print("Download complete!")
