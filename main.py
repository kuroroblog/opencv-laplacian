import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread("sample.jpg")

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# Laplacian関数 : Laplacianフィルタを用いて、画像の輝度勾配(エッジ)を検出するために利用する関数。

# 第一引数(必須) : 多次元配列(numpy.ndarray)
# 第二引数(必須) : 出力画像の型。cv2.CV_32F : 32ビット浮動小数点数。
# 第三引数(任意) : カーネルサイズ。

# 戻り値 : 多次元配列(numpy.ndarray)
img = cv2.Laplacian(img, cv2.CV_32F, ksize=3)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite("./output.png", img)
