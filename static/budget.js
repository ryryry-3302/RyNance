
let total = $('#total')[0];
let food = $('#food')[0];
let transport = $('#transport')[0];
let leisure = $('#leisure')[0];
let groceries = $('#groceries')[0];
let others = $('#others')[0];
let savingsvalue = total.value - food.value - transport.value - leisure.value - groceries.value -others.value;



const ctx = document.getElementById('myChart');
const myChart = new Chart(ctx, {
    type: 'pie',
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
                '#004c6d',
                '#416985',
                '#6c889e',
                '#96a8b7',
                '#c0c9d1',
                '#ebebeb'
            ],
            borderColor: 'black',
            borderWidth: 1
        }]
    },
    options: {
    }
});

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