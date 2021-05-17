$('#datepicker').datepicker({
    format: 'mm/dd/yyyy',
    startDate: '-3d'
});
$("#datepicker").css("z-index",2);


// bool = true;
// if(bool){
//     $('#click_me1').click(function(){
//         $('#click_me1').css({
//           'color':'black'
//         });
//         $('.checkbox1').css({
//             'background-color':'white',
//             'border' :'1px solid black'
//           });
//         bool = false;
//       });
// }
// else{
//     $('#click_me').click(function(){
//         $('#click_me1').css({
//           'color':'teal'
//         });
//         bool = true;
//       });
// }
function click(){
    var element = document.getElementById("click_me1");
    element.classList.toggle("checkstyle");
  }