<script type="text/javascript">
    $(function (){
        $.ajax({
        type: 'GET',
        url: '/student_list',
        success: function(data){
            $.each(data, function(i, data){
                $("#student").append('<li>'+data.first_name+'</li>')
            });
        }

        });


    });
</script>
