
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
        labels: ['Food', 'Transport'],
        datasets: [{
            label: 'Budget',
            data: [
                food.value,
                transport.value
            ],

            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
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
    var updateValues = [food.value, transport.value];
    myChart.data.datasets[0].data = updateValues;
    
    myChart.update();

}