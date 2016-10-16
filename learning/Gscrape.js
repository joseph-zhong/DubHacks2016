var imgs = document.getElementsByTagName('img')
var srcs = ""
for(var i = 0; i < imgs.length; i++) {
    srcs += imgs[i].src + '\n'
}
console.log(srcs)