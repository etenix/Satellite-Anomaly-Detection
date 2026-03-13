# src/__init__.py
"""
Satellite-Anomaly-Detection
GCOM-C衛星データを用いた大規模異常検知・動態解析パッケージ
"""

from .detector import AnomalyDetector
from .processor import SatelliteProcessor

__version__ = "1.0.0"
__author__ = "Haoran"
__description__ = "DaskとYOLOv5を統合したテラバイト級衛星データの並列処理パイプライン"

# パッケージの初期化ログや、並列処理用ライブラリのチェックをここで行うことも可能です
