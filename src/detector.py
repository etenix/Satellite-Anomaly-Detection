import torch
import cv2

class AnomalyDetector:
    def __init__(self, model_path='yolov5s.pt'):
        # 訓練済みYOLOv5モデルのロード
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, image_np):
        """
        画像内の漂流物を検知し、バウンディングボックスを返す
        """
        results = self.model(image_np)
        # 検知結果（座標、信頼度、クラス）の抽出
        detections = results.pandas().xyxy[0] 
        return detections
