import cloudinary
import cloudinary.uploader as uploader


cloudinary.config(
    cloud_name="dve3fvtfh",
    api_key="774516999375832",
    api_secret="9rFpVmvHLbm8wFSgDKW_nrXpmdM"

)

def get_uploader():
    return uploader