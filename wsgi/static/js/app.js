/**
 * Created by kperez on 21/12/15.
 */
function csrfcookie() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function () {

    window.showErrors = function(id,errors){
        $.each(errors,function(index,element){
            var selector='#'+id+' [name='+element.field+']';

            try{
                var parent=$(selector).parents('.form-group');
                $(parent).addClass('has-error');
                $(parent).find('.help-block').html(element.message);
            }catch(e){
                var parent=$(selector).parents('.form-group')[0];
                $(parent).addClass('has-error');
                $(parent).find('.help-block').html(element.message);
            }

            try{
                var children=$(selector+" + .help-block");
                $(children).html(element.message);
            }catch(e){
                var children=$(selector+" + .help-block")[0];
                $(children).html(element.message);
            }
        });
    };

    window.removeErrors = function(id){
        $('#'+id+'Message').html('');
        $('#'+id+' .help-block').html('');
        $('#'+id+' .form-group').removeClass('has-error');
    };

    window.cleanFields = function(id){
        $('#'+id+' input[type=text]').val('');
        $('#'+id+' textarea').val('');
        $('#'+id+' input[type=number]').val('');
        $('#'+id+' input[type=select]').val('');
        $('#'+id+' input[type=radio]').val('');
        $('#'+id+' input[type=checkbox]').val('');
        $('#'+id+' input[type=password]').val('');
        $('#'+id+' input[type=datetime-local]').val('');
        $('#'+id+' select option[value=""]').attr("selected",true);
    };

    $('#matchForm').submit(function () {
        var id = $(this).attr('id');
        var submit = $("#" + id + " [type='submit']")[0];
        var valueSubmit = submit.innerHTML;
        removeErrors(id);
        cleanErrors();
        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            beforeSend: function () {
                $("#" + id + " [type='submit']").attr('disabled', 'disabled').html("Making Match ...");
            },
            success: function (data) {
                if (data.hasErrors) {
                    showErrors(id, data.errors);
                }
                if (data.hasMessage) {
                    showMessage(data.message);
                }
                if (data.success) {
                    $("#match-agent-container").html(data.matchs);
                    $("#matchAgentModal").modal();
                }
            },
            complete: function (xhr, response) {
                $("#" + id + " [type='submit']").removeAttr('disabled').html(valueSubmit);
            }
        });
        return false;
    });

    $('#upload-file').submit(function (event) {
        var id = $(this).attr('id');
        var submit = $("#" + id + " [type='submit']")[0];
        var valueSubmit = submit.innerHTML;
        removeErrors(id);
        $(this).ajaxSubmit({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            beforeSend: function () {
                $("#" + id + " [type='submit']").attr('disabled', 'disabled').html("Enviando ...");
            },
            success: function (response) {

                if (response.hasMessage) {
                    showMessage(data.message)
                }
                if (response.success) {
                    cleanFields(id);
                    succesMessage(data.message);
                }
            },
            complete: function (xhr, response) {
                $("#" + id + " [type='submit']").removeAttr('disabled').html(valueSubmit);
            }
        });
        return false;
    });
});


function cleanErrors(){
    $("#output").removeClass('alert alert-success alert-danger animated fadeInUp');
}

function showMessage(error){
    $("#output").removeClass(' alert alert-success');
    $("#output").addClass("alert alert-danger animated fadeInUp").html(error);
}

function succesMessage(message){
    $("#output").addClass("alert alert-success animated fadeInUp").html(message);
    $("#output").removeClass(' alert-danger');
}