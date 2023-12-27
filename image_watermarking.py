from PIL import Image

class ImageWatermarking:
    def __init__(self, image_path, logo_path, result_image_path):
        self.image_path = image_path
        self.logo_path = logo_path
        self.result_image_path = result_image_path
        self.image = None
        self.logo = None

    def put_watermark(self):
        self.image = Image.open(self.image_path).convert("RGBA")
        self.logo = Image.open(self.logo_path).convert("RGBA")

        self.logo = self.logo.resize(self.image.size, Image.LANCZOS)
        alpha = int(input("Enter the warter mark transparency you want (0 is fully transparent - 255 is fully opique: )"))
        self.logo.putalpha(alpha)

        result_image = Image.alpha_composite(self.image, self.logo)
        result_image.save(self.result_image_path)

if __name__ == "__main__":
    image_path = "image.jpg"
    logo_path = "logo.png"
    result_image_path = "watermarked.png"

    image_watermarking = ImageWatermarking(image_path, logo_path, result_image_path)
    image_watermarking.put_watermark()
