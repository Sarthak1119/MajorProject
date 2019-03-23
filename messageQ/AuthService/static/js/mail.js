$(document).ready(function() {    
    var dialog = document.getElementById('compose');
    document.getElementById('show').onclick = function() {    
        dialog.show();

    };
    document.getElementById('hide').onclick = function() {
        dialog.close();
   };
});  
