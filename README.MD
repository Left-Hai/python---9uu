1.当前分析的是加密参数

(1)该接口进行了AES/CBC/PKCS7Padding加密

(2)主页请求地址：https://alipaydatabase.com/video/lists

(3)密码：AG+BwcnekYZy$9f7X#b2zdB93brfFMmz

(4)偏移：f%Z4F+qtFh六位随机数字和随机字母

(5)随机生成的范围["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

(6)sign值进行了md5加密：devicetype=pc&page=页数&timestamp=13位的时间戳&6Bf2_kh*P?4tuB*C#@WEVf752x8beCE@uB-Z

(7)post亲求的data参数{"tag":"","timestamp":13位的时间戳,"devicetype":"pc","page":页数,"encode_sign":"sign值"}


2.当前分析的是解密参数

(1)解密的偏移值主要是还是请求，只有把请求发出去才可以获取偏移的后六位数

例如：
响应内容如下:
{
"code":0,
"msg":"\u64cd\u4f5c\u6210\u529f",//unicode转中文-->操作成功
"data":"xxxxxxxx=",
"suffix":"pvYcSk"
}
这个suffix，就是我们的解密偏移后六位数

(2)拼接出来如下-->:f%Z4F+qtFhpvYcSk

这个就是我们解密所需要的偏移了
