$(document).ready(function(){
    $.getJSON("/artikel/show_json", function(artikel){
      let users= {};
      let time_diff = artikel["time_diff"];
                $.each(artikel, function(index,value){
                if (index === "user"){
                  for (const iterator of value) {
                    users[iterator.pk]=iterator.username;
                  }
                }
                })
                $.each(artikel, function(index,value){
                  if (index === "artikel"){
                    console.log(value);
                    for (const iterator of value) {
                      $("#artikel_containers").append(
                        `  <a href="${iterator.id}" class="list-group-item list-group-item-action mx-auto my-0">
                        <div class="d-flex w-100 justify-content-between">
                          <h5 class="mb-1">${iterator.title}</h5>
                          <small class="text-muted">${time_diff[iterator.id]}</small>
                        </div>
                        <p class="mb-1">${iterator.short_description}...</p>
                      </a>`
                      )
                    }
                  }
                })
        })
    $('#form_artikel').on('submit', function(e) {
        e.preventDefault();
        let title = $("#title").val();
        let description = $("#description").val();
        $.ajax({
          method: "POST",
          url: "/artikel/add/",
          data: {"title":title, "description":description},
        }).done(function(resp) {
          console.log(resp)
          $("#artikel_containers").prepend(
            `  <a href="${resp.pk}" class="list-group-item list-group-item-action mx-auto my-0">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">${resp.title}</h5>
              <small class="text-muted">Just now</small>
            </div>
            <p class="mb-1">${resp.short_description}...</p>
          </a>`
          )
          $("#exampleModal").modal("toggle")
        });
    })
  })