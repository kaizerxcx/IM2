





/*source: https://www.mynotepaper.com/add-or-remove-input-fields-dynamically-using-jquery */


$(document).ready(function() {
var max_fields = 15; //maximum input boxes allowed
var wrapper = $(".after-add-more"); //Fields wrapper
var add_button = $(".add-more"); //Add button ID
var x = 1; //initlal text box count
$(add_button).click(function(e){ //on add input button click
e.preventDefault();
if(x < max_fields){ //max input box allowed
x++; //text box increment
$(wrapper).append( '<div class="control-group input-group" style="margin-top:10px" id="inputFormRow" >'+
'            <input type="text" name="cast[]" id="cast" class="form-control" placeholder="Firstname, Lastname" maxlength="500">'+
'            <div class="input-group-btn"> '+
'              <button class="btn btn-danger remove" type="button" id=removeRow>'+
'                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-dash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">'+
'            <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 0 1h-7A.5.5 0 0 1 4 8z"/>'+
'          </svg>'+
'              </button>'+
'            </div>'+
'         '+
'                    </div>'); //add input box
}
});
 $(document).on('click', '#removeRow', function () {
        $(this).closest('#inputFormRow').remove();
    })
});








$("#cast").change(function () {
      $.ajax({
           type: "POST",
           url: "dvdRegistration.html",
           // data: $(this).parent().serialize(), // changed
           // data: $('#cast').val(),
            data: $('#cast').serialize(),
            contentType: false,
           success: function(data) {
               console.log(data); // show response from the php script.
           },
    });
    return false; // avoid to execute the actual form submission.
    });




$("#files").change(function () {
      $.ajax({
           type: "POST",
           url: "dvdRegistration.html",
           // data: $(this).parent().serialize(), // changed
           // data: $('#cast').val(),
            data: $('#files').serialize(),
            contentType: false,
           success: function(data) {
               console.log(data); // show response from the php script.
           },
    });
    return false; // avoid to execute the actual form submission.
    });









/*sa add more images  */
$(document).ready(function() {
  if (window.File && window.FileList && window.FileReader) {
    $("#files").on("change", function(e) {
      var files = e.target.files,
        filesLength = files.length;
      for (var i = 0; i < filesLength; i++) {
        var f = files[i]
        var fileReader = new FileReader();
        fileReader.onload = (function(e) {
          var file = e.target;
          $("<span class=\"pip\">" +
            "<img name =\"dvdImage\" class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
            "<br/><span class=\"removes\"> <svg width=\"2em\" height=\"2em\" viewbox=\"0 0 16 16\" class=\"bi bi-trash text-danger\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\">"+
                                                "<path d=\"M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z\"/>"+
                                                "<path fill-rule=\"evenodd\" d=\"M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z\"/>"+
                                           "</svg></span>" +
            "</span>").insertAfter("#files");    
          $(".removes").click(function(){
            $(this).parent(".pip").remove();
          });
          
          // Old code here
          /*$("<img></img>", {
            class: "imageThumb",
            src: e.target.result,
            title: file.name + " | Click to remove"
          }).insertAfter("#files").click(function(){$(this).remove();});*/
          
        });
        fileReader.readAsDataURL(f);
      }
      console.log(files);
    });
  } else {
    alert("Your browser doesn't support to File API")
  }
});


