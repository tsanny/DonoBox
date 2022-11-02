function fillDeadline(deadline) {
    var month
    switch (deadline.substring(5, 7)) {
        case "01":
            month = "Januari"
            break
        case "02":
            month = "Februari"
            break
        case "03":
            month = "Maret"
            break
        case "04":
            month = "April"
            break
        case "05":
            month = "Mei"
            break
        case "06":
            month = "Juni"
            break
        case "07":
            month = "Juli"
            break
        case "08":
            month = "Agustus"
            break
        case "09":
            month = "September"
            break
        case "10":
            month = "Oktober"
            break
        case "11":
            month = "November"
            break
        case "12":
            month = "Desember"
            break
    }
    var result = "".concat(deadline.substring(8, 10), " ", month, " ", deadline.substring(0, 4))
    result = result.concat(" - ", deadline.substring(11, 19))
    return result
}

function appendCrowdfund(id, title, fundraiser_name, collected, target, deadline) {
    $("#crowdfunds").append(`
      <div class="col-sm-6 col-md-4 p-3">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <h6 class="card-subtitle text-muted">Digalang oleh ${fundraiser_name}</h6>
            <hr>
            <b>${collected}</b> terkumpul - <b>${target}</b> dibutuhkan
            <br>
            hingga <b>${fillDeadline(deadline)}</b>
            <br><br>
            <a href=${crowdfundUrl.replace("1", id)} class="btn border">Lihat Detail</a>
          </div>
        </div>
      </div>
    `)
}

$(document).ready(function() {
    $.get(myFundsUrl, function(crowdfunds) {
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
      
        $.post(addFundUrl, form, function(crowdfund) {
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
    })

    $("#form").on("hidden.bs.modal", function() {
        $("form").trigger("reset")
        $("#error").html(``)
    })
})