
let total = $('#total')[0];
let food = $('#food')[0];
let transport = $('#transport')[0];
let leisure = $('#leisure')[0];
let groceries = $('#groceries')[0];
let others = $('#others')[0];
let savingsvalue = total.value - food.value - transport.value - leisure.value - groceries.value -others.value;


$('#savings').text('$' + savingsvalue);

const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Food', 'Transport', 'Leisure' ,'Groceries', 'Others', 'Savings'],
        datasets: [{
            label: 'Budget',
            data: [
                food.value,
                transport.value,
                leisure.value,
                groceries.value,
                others.value,
                savingsvalue

            ],

            

            backgroundColor: [
                '#003366',
                '#02234D',
                '#030F33',
                '#000000',
                '#17021A',
                '#2B0933'
            ],
            borderColor: 'black',
            borderWidth: 1,
            hoverOffset: 20,
            hoverBorder: 3,
            hoverBorderColor: 'white'
        }]
    },
    options: {

    }
});


Chart.defaults.color = 'white';

function updatechart(){
    console.log("imchanging");

    savingsvalue = total.value - food.value - transport.value - leisure.value - groceries.value -others.value;
    $('#savings').text('$' + savingsvalue);
    var updateValues = [
        food.value,
        transport.value,
        leisure.value,
        groceries.value,
        others.value,
        savingsvalue
    ];
    myChart.data.datasets[0].data = updateValues;
    
    myChart.update();

}