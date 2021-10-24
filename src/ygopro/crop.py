import fire
from PIL import Image


def crop_pic(src_name: str, target_name: str, width: int, height: int):
    with Image.open(src_name) as img:
        img = img.convert("RGB")
        region = img.crop((0, 0, width, height))
        region.save(target_name)


if __name__ == '__main__':
    fire.Fire(crop_pic)
