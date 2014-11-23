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
