let dra = document.getElementById("dw");
let dra1 = document.getElementById("dw1");
let gal = document.getElementById("gal");
let head1 = document.getElementById("head1");
let head2 = document.getElementById("head2");
const nav = document.querySelector('#header');
const footer = document.querySelector('.footr');



function drawer(){
    dra1.style.width="50%";
    dra1.style.height="90%";
    // dra1.style.backgroundColor="black";
    dra1.style.display="block";
    dra.style.display="none";        
    gal.style.display="none";    
    head1.style.display="none"; 
    head2.style.display="none";   

}
function exit(){
    dra1.style.display="none";
    dra.style.display="block";        
    gal.style.display="block";    
    head1.style.display="block"; 
    head2.style.display="block"; 
}

fetch('/header')
.then(res => res.text())
.then(data =>{
    nav.innerHTML=data;
    // footer.innerHTML=data;

})
fetch('/footer')
.then(res => res.text())
.then(data =>{
    //nav.innerHTML=data;
     footer.innerHTML=data;

})