$(document).ready(function() {
    // My custom JS
    $(".vDateField").datepicker({
        showOn: "button",
        buttonText: "<span class=\"glyphicon glyphicon-calendar\"></span>",
        // buttonImageOnly: true,
        dateFormat: "yy-mm-dd",
        showButtonPanel: true
    });
});
