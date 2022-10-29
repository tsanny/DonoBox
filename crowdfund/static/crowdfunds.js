function appendCrowdfund(id, title, fundraiser, collected, target, deadline) {
    $("#crowdfunds").append(`
      <div class="col-sm-6 col-md-4 p-3">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <h6 class="card-subtitle text-muted">Digalang oleh ${fundraiser}</h6>
            <hr>
            <ul>
              <li>${collected} terkumpul</li>
              <li>${target} dibutuhkan</li>
              <li>Batas pengumpulan: ${deadline}</li>
            </ul>
            <a href="http://PBP-C04.herokuapp.com/crowdfund/${id}" class="btn border">Lihat Detail</a>
          </div>
        </div>
      </div>
    `)
}

$(document).ready(function() {
    if (!"{{logged_in}}" || "{{role}}" == "Donatur") {
        if (!"{{logged_in}}") {
            $("#message").append(`
              <h5 class="text-center text-muted p-3">Login untuk melihat detail dan berdonasi kepada orang-orang yang membutuhkan</h3>
            `)
        } else {
            $("#message").append(`
              <h5 class="text-center text-muted p-3">Ayo berdonasi kepada orang-orang yang membutuhkan, {{user}}</h3>
            `)
        }

        $.get("{% url 'crowdfund:show_crowdfunds_json_ongoing' %}", function(crowdfunds) {
            for (const fund of crowdfunds) {
                appendCrowdfund(
                    fund["pk"],
                    fund["fields"]["title"],
                    fund["fields"]["fundraiser"],
                    fund["fields"]["collected"],
                    fund["fields"]["target"],
                    fund["fields"]["deadline"]
                )
            }
        }, "json")

    } else {
        $("#message").append(`
          <h5 class="text-center text-muted p-3">Berikut adalah galangan dana yang Anda ajukan, {{user}}</h3>
        `)
        $("#button").append(`
          <a class="btn border" data-bs-toggle="modal" data-bs-target="#form">Galang Dana Baru</a>
        `)
        
        $.get("{% url 'crowdfund:show_crowdfunds_json_by_me' %}", function(crowdfunds) {
            for (const fund of crowdfunds) {
                appendCrowdfund(
                    fund["pk"],
                    fund["fields"]["title"],
                    fund["fields"]["fundraiser"],
                    fund["fields"]["collected"],
                    fund["fields"]["target"],
                    fund["fields"]["deadline"]
                )
            }
        }, "json")

        $("form").submit(function(event) {
            event.preventDefault()
            var form = {
                title: $("#title").val(),
                description: $("#description").val(),
                target: $("#target").val(),
                deadline: $("#deadline").val(),
                csrfmiddlewaretoken: "{{csrf_token}}",
            }

            $.post("{% url 'crowdfund:add_crowdfund' %}", form, function(data) {
            }, "json")
        })
    }
})