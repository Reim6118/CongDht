利用python指令執行Congdht.py檔案,在後面打上引數

-a  顯示DHT爬蟲爬到的所有hash info,並且顯示出來

-r  將爬到的hash info 利用排名演算法算出被下載50次以上的檔案並顯示出來

-d  將排名裡的檔案利用libtorrent套件做出來的downloader下載下來

爬蟲運行方式：twistd -y collectord.py

License:NCU COMM CongStudio


