function Day_night(self){
    if (self.value==='day') {
        document.querySelector('body').style.backgroundColor = 'white';
        document.querySelector('body').style.color = 'black';
        document.querySelector('#night_day').value = 'night';
        Setcolor("blue");
    } else {
        document.querySelector('body').style.backgroundColor = 'black';
        document.querySelector('body').style.color = 'white';
        document.querySelector('#night_day').value = 'day';
        Setcolor("powderblue");
    }
}
function Setcolor(co){
    var alist = document.querySelectorAll('a'); 
    var i=0;
    while(i < alist.length) {
        alist[i].style.color = co;
        i=i+1;
    }
}