$(document).ready(function(){

    // jQuery methods go here...
    $('input').on('keyup', calculate);

    function calculate(){
        let age = parseInt($('#age').val());
        let port = parseInt($('#portvalue').val());
        let contr = parseInt($('#contribution').val());
        let incr = Number(parseFloat($('#incrementrate').val()/100).toFixed(2));
        let withrate = Number(parseFloat($('#Withdrawlrate').val()/100).toFixed(2));
        let withd = parseInt($('#withd').val());
        let growth = Number(parseFloat($('#growthrate').val()/100).toFixed(2));
        let infl = Number(parseFloat($('#inflationrate').val()/100).toFixed(2));
        let retirement_sum = withd / withrate;
        let real_growth = growth - infl + 1;
        let incrate = (1 + incr);
    

        while (age < 65) {
            age++;
            port = contr + port;
    
            contr = incrate * contr;
            port = port * real_growth;
            if (port < retirement_sum) {
                continue;

            }   else {
                break;
            }

        }
        if (age > 65) {
        alert("cannot retire before 65");
        } 
        
        $('#retirementage').text(age);
        $('#retireport').text('$' + port.toFixed(2));

        


    }

  
});