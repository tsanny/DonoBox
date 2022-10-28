$(document).ready(function() {
    $.get("{% url 'crowdfund:show_crowdfund_json' id %}", function(fund) {
        $("head").append(`
          <title>${fund[0]["fields"]["title"]}<title>
        `)

        $("body").append(`
          <h1 class="text-center p-3">${fund[0]["fields"]["title"]}</h1>
          <div class="d-flex flex-row">
            <div class="p-3 flex-fill">
              <h5>Informasi Lebih Lanjut</h5>
              ${fund[0]["fields"]["description"]}
            </div>
            <div class="p-3 flex-fill" id="info">
              <h5>Pengaju Galangan Dana</h5>
              ${fund[0]["fields"]["fundraiser"]}
              <br><br>
              <h5>Jumlah Dana Terkumpul</h5>
              ${fund[0]["fields"]["collected"]}
              <br><br>
              <h5>Target Dana Terkumpul</h5>
              ${fund[0]["fields"]["target"]}
              <br><br>
              <h5>Batas Waktu Pengumpulan Dana</h5>
              ${fund[0]["fields"]["deadline"]}
              <br><br>
            </div>
          </div>
        `)

        if ("{{role}}" == "Donatur") {
            $("#info").append(`
              <a class="btn border" data-bs-toggle="modal" data-bs-target="#form">Kumpulkan Donasi</a>
            `)

            $("form").submit(function(event) {
                event.preventDefault()
                var form = {
                    amount: $("#amount").val(),
                    comment: $("#comment").val(),
                    csrfmiddlewaretoken: "{{csrf_token}}",
                }

                $.post("{% url 'crowdfund:add_donation' id %}", form, function(data) {
                }, "json")
            })

        } else {
            $("#info").append(`
              <a class="btn border" data-bs-toggle="modal" data-bs-target="#history">Donasi Terkumpul</a>
            `)

            $.get("{% url 'crowdfund:show_donations_json_by_fund' id %}", function(donations) {
                for (const donation in donations) {
                    $("#donations").append(`
                      <h6>${donation["fields"]["donator"]} mendonasikan ${donation["fields"]["amount"]}</h6>
                      <p>${donation["fields"]["comment"]}</p>
                    `)
                }
            }, "json")
        }
    }, "json")
})