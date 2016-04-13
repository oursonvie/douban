'<div id="info" class="ckd-collect">\n<span>\n<span class="pl">\n                            \xe8\xa1\xa8\xe6\xbc\x94\xe8\x80\x85:\n                                    \n                                    <a href="/search?q=Jamie%20XX&amp;sid=26354131">Jamie XX</a>\n</span>\n</span>\n

<br />\n<span class="pl">\xe6\xb5\x81\xe6\xb4\xbe:</span>&nbsp;\xe7\x94\xb5\xe5\xad\x90\n    

<br />\n<span class="pl">\xe4\xb8\x93\xe8\xbe\x91\xe7\xb1\xbb\xe5\x9e\x8b:</span>&nbsp;\xe4\xb8\x93\xe8\xbe\x91\n    

<br />\n<span class="pl">\xe4\xbb\x8b\xe8\xb4\xa8:</span>&nbsp;CD\n    

<br />\n<span class="pl">\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4:</span>&nbsp;2015-06-01\n    

<br />\n<span>\n<span class="pl">\n                            \xe5\x87\xba\xe7\x89\x88\xe8\x80\x85:\n                                    \n                                    
<a href="/search?q=Young%20Turks&amp;sid=26354131">Young Turks</a>\n</span>\n</span>\n<br />\n<span class="pl">\xe5\x94\xb1\xe7\x89\x87\xe6\x95\xb0:</span>&nbsp;1\n    <br />\n<span class="pl">\xe6\x9d\xa1\xe5\x9e\x8b\xe7\xa0\x81:</span>&nbsp;4582214511832\n    <br />\n<span class="pl">\xe5\x85\xb6\xe4\xbb\x96\xe7\x89\x88\xe6\x9c\xac:</span>&nbsp;\n            <a href="https://music.douban.com/subject/26354165/">In Colour</a>\n            \xef\xbc\x88<a href="/albums/109738">\xe5\x85\xa8\xe9\x83\xa8</a>\xef\xbc\x89\n            <br />\n</div>'


b.find('<br />\n<span class="pl">\xe6\xb5\x81\xe6\xb4\xbe:</span>&nbsp;')+len('<br />\n<span class="pl">\xe6\xb5\x81\xe6\xb4\xbe:</span>&nbsp;')

b.find('<br />\n<span class="pl">\xe4\xb8\x93\xe8\xbe\x91\xe7\xb1\xbb\xe5\x9e\x8b:</span>&nbsp;')

## 专辑类型
print b[b.find('<br />\n<span class="pl">\xe6\xb5\x81\xe6\xb4\xbe:</span>&nbsp;')+len('<br />\n<span class="pl">\xe6\xb5\x81\xe6\xb4\xbe:</span>&nbsp;'):b.find('<br />\n<span class="pl">\xe4\xb8\x93\xe8\xbe\x91\xe7\xb1\xbb\xe5\x9e\x8b:</span>&nbsp;')]
电子

print b[b.find('流派:</span>&nbsp;')+len('流派:</span>&nbsp;'):b.find('流派:</span>&nbsp;')+len('流派:</span>&nbsp;')+6]

## 发行时间
print b[b.find('发行时间:</span>&nbsp;') + len('发行时间:</span>&nbsp;'):b.find('发 行时间:</span>&nbsp;') + len('发行时间:</span>&nbsp;')+10]


b.find('<br />\n<span class="pl">\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4:</span>&nbsp;') + len('<br />\n<span class="pl">\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4:</span>&nbsp;')

b.find('<br />\n<span>\n<span class="pl">\n                            \xe5\x87\xba\xe7\x89\x88\xe8\x80\x85:\n')

print b[b.find('<br />\n<span class="pl">\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4:</span>&nbsp;') + len('<br />\n<span class="pl">\xe5\x8f\x91\xe8\xa1\x8c\xe6\x97\xb6\xe9\x97\xb4:</span>&nbsp;'):b.find('<br />\n<span>\n<span class="pl">\n                            \xe5\x87\xba\xe7\x89\x88\xe8\x80\x85:\n')]

## 出版者

