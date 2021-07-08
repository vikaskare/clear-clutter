import os

PDF_EXT = ['.pdf']
IMAGE_EXT = ['.png', '.jpg', '.jpeg']
EXE_EXT = ['.exe']
MEDIA_EXT = ['.mp4', '.mkv', 'mp3']
ZIP_EXT = ['.zip', '.rar']


def move_to_destination(folder, files):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for file in files:
        os.replace(file, f"{folder}/{file}")
    print(f"... {len(files)} {folder} moved")

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("main.py")
    # print(files)

    pdfs = [file for file in files if os.path.splitext(file)[1].lower() in PDF_EXT]
    # print(pdfs)

    images = [file for file in files if os.path.splitext(file)[
        1].lower() in IMAGE_EXT]
    # print(images)

    exes = [file for file in files if os.path.splitext(file)[1].lower() in EXE_EXT]
    # print(exes)

    medias = [file for file in files if os.path.splitext(file)[
        1].lower() in MEDIA_EXT]
    # print(medias)

    zips = [file for file in files if os.path.splitext(file)[1].lower() in ZIP_EXT]
    # print(zips)

    # extension = os.path.splitext(file)[1].lower()

    others = [file for file in files if (os.path.splitext(file)[1].lower() not in PDF_EXT and os.path.splitext(file)[1].lower() not in IMAGE_EXT and os.path.splitext(
        file)[1].lower() not in EXE_EXT and os.path.splitext(file)[1].lower() not in MEDIA_EXT and os.path.splitext(file)[1].lower() not in ZIP_EXT and os.path.isfile(file))]
    # print(others)

    move_to_destination("PDF", pdfs)
    move_to_destination("Images", images)
    move_to_destination("EXE", exes)
    move_to_destination("Media", medias)
    move_to_destination("Zip", zips)
    move_to_destination("Other", others)