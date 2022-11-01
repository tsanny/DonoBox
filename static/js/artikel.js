$(document).ready(function(){
    $.getJSON("/artikel/show_json", function(artikel){
      let users= {};
                $.each(artikel, function(index,value){
                if (index === "user"){
                  for (const iterator of value) {
                    users[iterator.pk]=iterator.username;
                  }
                }
                })
                $.each(artikel, function(index,value){
                  if (index === "artikel"){
                    for (const iterator of value) {
                      $("#artikel_containers").append(
                        `<div class="col-12 col-md-6 col-lg-4">
                            <div class="card">
                                <h3 class="card-title">${iterator.title}</h3>
                                <p class="card-text">by ${users[iterator.user_id]} posted on ${dateFormat(iterator.date)}</p>
                                <p class="card-text">${iterator.short_description}...</p>
                                <a href="${iterator.id}" class="btn submit">Read more</a>
                            </div>
                        
                            </div>` 
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
                        `<div class="col-12 col-md-6 col-lg-4">
                            <div class="card">
                                <h3 class="card-title">${resp.title}</h3>
                                <p class="card-text">by ${resp.user} posted on ${dateFormat(resp.date)}</p>
                                <p class="card-text">${resp.short_description}...</p>
                                <a href="${resp.pk}" class="btn submit">Read more</a>
                            </div>
                        
                            </div>` 
                      )
          $("#exampleModal").modal("toggle")
        });
    })
  })
  function dateFormat(date) {
    let month = {"1":"January",
    "2":"February",
    "3":"March",
    "4":"April",
    "5":"May",
    "6":"June",
    "7":"July",
    "8":"August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"};
    return(month[date.slice(5,7)] + " "  + date.slice(8,10) + ", "+ date.slice(0,4));
  }