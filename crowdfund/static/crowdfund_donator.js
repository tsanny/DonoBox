function fillDescription(description) {
  if (description == "") {
    return "<span class=\"text-muted\">Galangan dana ini tidak memiliki deskripsi.</span>"
  }
  return description
}

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
  result = result.concat(" - ", deadline.substring(11, 19), " WIB")
  return result
}

function updateCollected(collected) {
    $("#collected").text(`${collected}`)
    $("#update").html(`<br>Donasi telah diberikan kepada penggalang. Terima kasih!`)
}

$(document).ready(function() {
    $.get(crowdfundUrl, function(fund) {
        $("head").append(`
          <title>${fund[0]["fields"]["title"]}</title>
        `)

        $("#crowdfund").prepend(`
          <h1 class="text-center">${fund[0]["fields"]["title"]}</h1>
        `)

        $("#detail").append(`
          <div class="col-md-6 col-lg-4 p-3">
            <div class="card">
              <div class="card-body">
                <h5>Informasi Lebih Lanjut</h5>
                ${fillDescription(fund[0]["fields"]["description"])}
                <div class="text-success" id="update"></div>
              </div>
            </div>
          </div>
          <div class="col-md-6 col-lg-4 p-3">
            <div class="card">
              <div class="card-body">
                <h5>Pengaju Galangan Dana</h5>
                ${fund[0]["fields"]["fundraiser_name"]}
                <br><br>
                <h5>Jumlah Dana Terkumpul</h5>
                <div id="collected">${fund[0]["fields"]["collected"]}</div>
                <br>
                <h5>Target Dana Terkumpul</h5>
                ${fund[0]["fields"]["target"]}
                <br><br>
                <h5>Batas Waktu Pengumpulan Dana</h5>
                ${fillDeadline(fund[0]["fields"]["deadline"])}
                <br><br>
                <div class="text-center">
                  <a class="btn border" data-bs-toggle="modal" data-bs-target="#form">Kumpulkan Donasi</a>
                </div>
              </div>
            </div>
          </div>
        `)
    })

    $("form").submit(function(event) {
        event.preventDefault()
        var form = {
            amount: $("#amount").val(),
            comment: $("#comment").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        }
    
        $.post(addDonationUrl, form, function(crowdfund) {
            if (!("error" in crowdfund)) {
                updateCollected(crowdfund[0]["fields"]["collected"])
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