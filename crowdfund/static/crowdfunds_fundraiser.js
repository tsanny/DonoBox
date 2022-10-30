function appendCrowdfund(id, title, fundraiser_name, collected, target, deadline) {
    $("#crowdfunds").append(`
      <div class="col-sm-6 col-md-4 p-3">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <h6 class="card-subtitle text-muted">Digalang oleh ${fundraiser_name}</h6>
            <hr>
            <ul>
              <li>${collected} terkumpul</li>
              <li>${target} dibutuhkan</li>
              <li>Batas pengumpulan: ${deadline}</li>
            </ul>
            <a href="http://localhost:8000/crowdfund/${id}/" class="btn border">Lihat Detail</a>
          </div>
        </div>
      </div>
    `)
}

$(document).ready(function() {
    $.get("http://localhost:8000/crowdfund/funds/json/myfunds/", function(crowdfunds) {
        if (crowdfunds.length != 0) {
            $("#no-crowdfunds").hide()
            for (const crowdfund of crowdfunds) {
                appendCrowdfund(
                    crowdfund["pk"],
                    crowdfund["fields"]["title"],
                    crowdfund["fields"]["fundraiser_name"],
                    crowdfund["fields"]["collected"],
                    crowdfund["fields"]["target"],
                    crowdfund["fields"]["deadline"]
                )
            }
        }
    }, "json")

    $("form").submit(function(event) {
        event.preventDefault()
        var form = {
            title: $("#title").val(),
            description: $("#description").val(),
            target: $("#target").val(),
            deadline: $("#deadline").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        }
      
        $.post("http://localhost:8000/crowdfund/funds/add/", form, function(crowdfund) {
            if (!("error" in crowdfund)) {
                $("#no-crowdfunds").hide()
                appendCrowdfund(
                    crowdfund[0]["pk"],
                    crowdfund[0]["fields"]["title"],
                    crowdfund[0]["fields"]["fundraiser_name"],
                    crowdfund[0]["fields"]["collected"],
                    crowdfund[0]["fields"]["target"],
                    crowdfund[0]["fields"]["deadline"]
                )
                $("#form").modal("hide")
                $("form").trigger("reset")
                $("#error").html(``)
            } else {
                $("#error").html(`Pastikan isian formulir memenuhi ketentuan.<br><br>`)
            }
        }, "json")

        $("#form").on("hidden.bs.modal", function() {
            $("form").trigger("reset")
            $("#error").html(``)
        })
    })
})