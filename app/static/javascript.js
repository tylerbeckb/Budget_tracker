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

function goalPage() {
    $(document).ready(function() {
        $("#GoalForm").hide();
        $("#EditGoalForm").hide();
        $("#addBtn").click(function() {
            $("#GoalForm").slideDown();
            $("#EditGoalForm").hide();
        })
        $("#editBtn").click(function() {
            $("#EditGoalForm").slideDown();
            $("#GoalForm").hide();
        })
    })
}