
$(document).ready(function () {
  $('#searchform').submit(function (e) {
    e.preventDefault()
    console.log("i am alive")
    let searchterm = $('#searchterm').val()

    let url = "https://www.investopedia.com/search?q=" + searchterm.replaceAll(" ", "+")
    window.location.href = url
  });
});