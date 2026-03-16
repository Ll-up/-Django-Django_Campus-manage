document.addEventListener('DOMContentLoaded', function() {
    var img = document.querySelectorAll('img');
    console.log(img);
    var tex =document.getElementById("l")
    tex.textContent="很高兴遇见你"
    //轮播图
    var nextb=document.querySelector(".next")
    console.log(nextb)
    var preb=document.querySelector(".pre")
    var page=document.querySelector(".page")  
    var indx=0
    function updatepage () {
        page.textContent=indx+1
    }
    nextb.addEventListener('click',function() {
        img[indx].className=""
        indx++
        if(indx>3)
            indx=0
        img[indx].className="active"
        updatepage()
    })
    preb.addEventListener('click',function() {
        img[indx].className=""
        indx--
        if(indx<0)
            indx=3
        img[indx].className="active"
        updatepage()
    })
});