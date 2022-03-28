$(document).ready(function(){

    // jQuery methods go here...
    $('input').on('keyup', calculate);

    function calculate(){
        let age = parseInt($('#age').val());
        let port = parseInt($('#portvalue').val());
        let contr = parseInt($('#contribution').val());
        let incr = parseFloat($('#incrementrate').val()/100).toFixed(2);
        let withrate = parseFloat($('#Withdrawlrate').val()/100).toFixed(2);
        let withd = parseInt($('#withd').val());
        let growth = parseFloat($('#growthrate').val()/100).toFixed(2);
        let infl = parseFloat($('#inflationrate').val()/100).toFixed(2);
        
        let retirement_sum = withd / withrate;
        let real_growth = growth - infl + 1;

        while (age < 65) {
            age++;
            port += contr;
            contr *= (1 + incr);
            port *= real_growth;
            if (port < retirement_sum) {
                continue;
            }   else {
                alert(age);
                break;
            }

        }
        
        setTimeout(function(){
            if (age > 65) {
            alert("cannot retire before 65");
            } 
        }, 5000);


    }

  
});