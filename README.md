simplebit
=========

simplebit adalah module untuk memkonversi string dan file atau numerik list ke sebuah representasi bit. lebih spesifik lagi hal ini bisa membantu Anda untuk bermain dengan Algoritma SHA1 jika tidak menggunakan endian.

## Cara Install
```C:\> python setup.py install```

## Cara Menggunakan
module simplebit memiliki 6 fungsi utama yang masing-masing memiliki teknik untuk mengkonversi bit.

##### fungsi numb2Bit(int num)
```
>>> from simplebit import *
>>> numb2Bit(1564567)
```
hasilnya :
```
>>> 
0101111101111110010111
```

##### fungsi listNum2Bit(int num)
```
>>> from simplebit import *
>>> listNum2Bit([232, 54, 21])
```
hasilnya :
```
>>> 
['011101000', '0110110', '010101']
```

##### fungsi string2Bit(string)
```
>>> from simplebit import *
>>> string2Bit("Pythonizam")
```
hasilnya :
```
>>>
[ '01010000', '01111001', '01110100', 
  '01101000', '01101111', '01101110', 
  '01101001', '01111010', '01100001', 
  '01101101' ]
```
##### fungsi file2Bit(filename)
```
>>> from simplebit import *
>>> file2Bit('D:/Folder.jpg')
```
```
>>> 
[
  '01100111', '01101111', '00101101', '011011010', 
  '00010101', '01110100', '01110100', '011110011', 
  '01001110', '00100110', '010000011', '011100111', 
  '01001001', '010110111', '01000100', '010010010', 
  '010100010', '00010100', '01010001', '01000000', 
  '00011111', '011111111', '011011001' ]
```
