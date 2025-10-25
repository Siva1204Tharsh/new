# from huggingface_hub import hf_hub_download
# import shutil
# import os

# # Define the repo and filename
# repo_id = "Ajanthan06/Email-Phishinh-faite"
# filename = "pytorch_model.bin"  # e.g., "model.bin" or "pytorch_model.bin"

# # Download the file
# downloaded_file = hf_hub_download(repo_id=repo_id, filename=filename)

# # Save it locally as .pkl
# output_path = "my_model.pkl"
# shutil.copy(downloaded_file, output_path)

# print(f"File saved as {output_path}")

from huggingface_hub import hf_hub_download
import shutil

# Download the model file
downloaded_file = hf_hub_download(
    repo_id="Ajanthan06/Email-Phishinh-faite",
    filename="pytorch_model.bin"
)

# Save it with a new name and extension
shutil.copy(downloaded_file, "email_phishing_model.pkl")

print("Model downloaded and saved as email_phishing_model.pkl")
