from processor import SatelliteProcessor
from detector import AnomalyDetector

def run_satellite_analysis(files):
    # 1. 大規模データのプリプロセス
    proc = SatelliteProcessor(files)
    processed_data = proc.preprocess()
    
    # 2. AIによる異常検知
    detector = AnomalyDetector()
    for timestamp in processed_data.time:
        img = processed_data.sel(time=timestamp).values
        results = detector.detect(img)
        
        # 3. 動態解析（時系列画像からの流速算出）
        # 前フレームとの座標差から移動ベクトルを計算
        print(f"Timestamp {timestamp}: {len(results)} 件の漂流物を検知")

if __name__ == "__main__":
    # GCOM-C 衛星データのパス（例）
    satellite_files = "data/GCOM-C_*.nc"
    run_satellite_analysis(satellite_files)
