from ultralytics import YOLO

def main():
    model = YOLO('./runs/detect/train/weights/best.pt')
    model.track(source='./videos_for_testing/bali.mp4', show=True)

if __name__ == "__main__":
    main()