import sys
from PIL import Image,ImageOps
def main():
    extensions = [
        ".png",
        ".jpeg",
        ".jpg"
    ]
    if not len(sys.argv) == 3:
        print("number of arguments are not correct")
        sys.exit(1)
    input_extention = sys.argv[1][sys.argv[1].rfind("."):].lower()
    output_extention = sys.argv[2][sys.argv[2].rfind("."):].lower()
    if not input_extention in extensions or not output_extention in extensions or not input_extention == output_extention:
        print("extention not correct")
        sys.exit(1)
    try:
        with open(sys.argv[1], "r"):
            pass
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    try:
        image = Image.open(sys.argv[1])
        #sys.argv[2].append(image)
    except FileNotFoundError:
        sys.exit(1)
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt,shirt)
    image.save(sys.argv[2])




if __name__ == "__main__":
    main()