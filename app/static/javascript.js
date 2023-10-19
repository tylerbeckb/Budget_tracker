function inExPage() {
    $(document).ready(function() {
        $("#inForm").slideUp();
        $("#exForm").slideUp();
        $("#inEditForm").slideUp();
        $("#exEditForm").slideUp();
        $(".inForm").click(function() {
            $("#inForm").slideDown();
        })
        $(".exForm").click(function() {
            $("#exForm").slideDown();
        })
        $(".inEditForm").click(function() {
            $("#inEditForm").slideDown();
        })
        $(".exEditForm").click(function() {
            $("#exEditForm").slideDown();
        })
    })
}